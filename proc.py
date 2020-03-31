import pandas as pd
import numpy as np

class DataLoader(object):
    def __init__(self, **kwargs):
        self.__top = kwargs.get('top', 10)
        self.__query = kwargs.get('query', None)
        self.__logistic_params  = kwargs.get('logistic_params', None)
        #
        self.__covid_data = None
        self.__country_data = None
        self.__table = None
        self.__leaders = None
        self.__states = None
        self.__grouped = None
        self.__mortality = None
        self.__latest = None
        self.__cty_data = None
        #
        self.__train_ds_confirmed = None
        self.__train_ds_deaths = None
        self.__train_ds_active = None
        self.__train_ds_recovered = None
        self.__train_ds_mortality = None
        #
        self.__countries = ['Mainland China', 'Italy', 'Germany', 'Iran', 'US', 'Spain']
        self.__country_states = ['Germany']
        #
        self.__loaded = self.loader() if len(kwargs) else False
        self.__processed = self.processor() if self.__loaded else False
        self.__modelled = self.modeller() if self.__processed and self.__logistic_params else False
        #last status in chain
        self.__status = self.__processed
        
        
    @property
    def table(self):
        return self.__table if self.__status else None

    @property
    def grouped(self):
        return self.__grouped if self.__status else None
    
    @property
    def leaders(self):
        return self.__leaders if self.__status else None

    @property
    def states(self):
        return self.__states if self.__status else None

    @property
    def mortality(self):
        return self.__mortality if self.__status else None

    @property
    def train_ds_confirmed(self):
        return self.__train_ds_confirmed

    @property
    def train_ds_deaths(self):
        return self.__train_ds_deaths

    @property
    def train_ds_active(self):
        return self.__train_ds_active

    @property
    def train_ds_recovered(self):
        return self.__train_ds_recovered

    @property
    def train_ds_mortality(self):
        return self.__train_ds_mortality

    @property
    def logistic_params(self):
        return self.__logistic_params


    @property
    def cty_data(self):
        return self.__cty_data
    
    def loader(self):
        
        self.__covid_data = pd.read_csv('data/covid_19_data.csv',
                                        parse_dates = ['ObservationDate','Last Update'])

        self.__country_data = pd.read_csv("data/countries of the world.csv")

        print("Shape:", self.__covid_data.shape)
        return True

    #prevent division by zero
    def if_null(self, x):
        return x if x != 0 else 1.
    
    def processor(self):
        # countries
        print("country shape", self.__country_data.shape)
        pd_col = 'Pop. Density (per sq. mi.)'
        self.__country_data[pd_col] = self.__country_data[pd_col].str.replace(",","").astype(float)
        #self.__country_data =  self.__country_data.apply(lambda x : x.str.replace(',','.'))
        #self.__country_data["population_density"] = self.__country_data[].astype(float)
        #Note: a place may have reported data more than once per day.
        
        # covid data
        print("covid shape", self.__covid_data.shape)

        #get rid of unessecary columns
        self.__covid_data = self.__covid_data.drop(['SNo',
                                                    'Last Update'],
                                                   axis=1)

        self.__covid_data = self.__covid_data.rename(columns={'Country/Region' : 'Country',
                                                              'Province/State' : 'State',
                                                              'ObservationDate':'Date'})

        #make sure again that this is a datetime
        self.__covid_data["Date"] = pd.to_datetime(self.__covid_data["Date"])

        #add active
        self.__covid_data['Active'] = self.__covid_data['Confirmed'] - self.__covid_data['Deaths'] - self.__covid_data['Recovered']


        #print
        print("\ncovid:", self.__covid_data.head())

        # check null values
        print("Null covid data values", self.__covid_data.isnull().sum() )
        print("Null country data values", self.__country_data.isnull().sum() )

        # Clean up rows with zero cases
        if self.__query:
            self.__covid_data = self.__covid_data.query( self.__query.query )
            #self.__covid_data[(self.__covid_data['Confirmed']>0) &
         #                                     (self.__covid_data['Date'] > '2020-02-15') &
         #                                     (self.__covid_data['Date'] < '2021-01-01') ]


        #sort
        self.__covid_data = self.__covid_data.sort_values(['Date','Country','State'])

        # Add column of days since first case
        self.__covid_data['first_date'] = self.__covid_data.groupby('Country')['Date'].transform('min')
        self.__covid_data['days'] = (self.__covid_data['Date'] -
                                     self.__covid_data['first_date']).dt.days
        

        # We convert the data into daily.
        # If the data for the latest day is not available, we will fill it with previous available data.
        #This creates a table that sums up every element in the Confirmed, Deaths, and recovered columns.
        self.__table = self.__covid_data.groupby('Date')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum()

        #Reset index coverts the index series, in this case date, into an index value. 
        self.__table = self.__table.reset_index()
        self.__table = self.__table.sort_values('Date', ascending=False)
        print("\ntable:", self.__table.head())

        #leaders
        self.__leaders = self.__covid_data[self.__covid_data['Country'].isin(self.__countries)]
        self.__leaders = self.__leaders.groupby(['Date', 'Country']).agg({'Confirmed': ['sum']})
        self.__leaders.columns = ['Confirmed All']
        self.__leaders = self.__leaders.reset_index()
        print("\nlead:", self.__leaders)
        
        #groups
        self.__grouped = self.__covid_data.groupby(['Date']).agg({'Deaths': ['sum'],
                                                                  'Recovered': ['sum'],
                                                                  'Confirmed': ['sum']})
        self.__grouped.columns = ['Deaths_All',
                                  'Recovered_All',
                                  'Confirmed_All']
        
        self.__grouped = self.__grouped.reset_index()
        self.__grouped['Difference_world'] = self.__grouped['Confirmed_All'].diff().shift(-1)

        self.__grouped['Deaths_All_Frac'] = self.__grouped.apply(lambda row :
                                                              ((row.Deaths_All)/(row.Confirmed_All))*100 , axis=1)
        self.__grouped['Recovered_All_Frac'] = self.__grouped.apply(lambda row :
                                                                 ((row.Recovered_All)/(row.Confirmed_All))*100 , axis=1)
        self.__grouped['World_growth_rate'] = self.__grouped.apply(lambda row :
                                                                   row.Difference_world/row.Confirmed_All*100, axis=1)
        self.__grouped['World_growth_rate'] = self.__grouped['World_growth_rate'].shift(+1)

        print("grouped:", self.__grouped.head())

        #mortality
        self.__mortality = self.__covid_data[self.__covid_data['Country'].isin(self.__countries)]
        self.__mortality = self.__mortality.groupby(['Date',
                                                     'Country']).agg({'Deaths': ['sum'],
                                                                      'Recovered': ['sum'],
                                                                      'Confirmed': ['sum']})
        self.__mortality.columns = ['Deaths', 'Recovered', 'Confirmed']
        self.__mortality = self.__mortality.reset_index()
        self.__mortality = self.__mortality[self.__mortality.Deaths != 0]
        self.__mortality = self.__mortality[self.__mortality.Confirmed != 0]

        self.__mortality['Mortality'] = self.__mortality.apply(lambda row :
                                                               ((row.Deaths)/self.if_null((row.Confirmed)))*100,
                                                               axis=1)
        

        self.__mortality['MortalityNormed'] = self.__mortality.apply(lambda row :
                                                                     ((row.Deaths)/self.if_null( row.Confirmed )),
                                                                     axis=1)
        
        #latest
        self.__latest = self.__covid_data[self.__covid_data['Date'] == self.__covid_data['Date'].max()]

        # covid by country
        self.__cty_data = self.__latest.groupby('Country').sum()
        self.__cty_data['Death Rate'] = self.__cty_data['Deaths'] / self.__cty_data['Confirmed'] * 100
        self.__cty_data['Recovery Rate'] = self.__cty_data['Recovered'] / self.__cty_data['Confirmed'] * 100
        self.__cty_data['Active'] = self.__cty_data['Confirmed'] - self.__cty_data['Deaths'] - self.__cty_data['Recovered']
        self.__cty_data = self.__cty_data.drop('days', axis=1).sort_values('Confirmed', ascending=False)

        #states
        self.__states = self.__covid_data[self.__covid_data['Country'].isin(self.__country_states)]
        self.__states = self.__states.groupby(['Date', 'Country', 'State']).agg({'Confirmed': ['sum']})
        self.__states.columns = ['Confirmed']
        self.__states = self.__states.reset_index()
        print("\nstates:", self.__states)

        return True

    def reporter(self):

        if self.__processed:
            print('- Last update: ' + str(self.__covid_data["Date"].max()))
            print('- Total confirmed cases: %.d' %np.sum(self.__latest['Confirmed']))
            print('- Total death cases: %.d' %np.sum(self.__latest['Deaths']))
            print('- Total active cases: %.d' %np.sum(self.__latest['Active']))
            print('- Total recovered cases: %.d' %np.sum(self.__latest['Recovered']))
            print('- Death rate %%: %.2f' % (np.sum(self.__latest['Deaths'])/np.sum(self.__latest['Confirmed'])*100))
            
            print("\n", self.__cty_data.head(self.__top).to_markdown(showindex=True))
        else:
            print("Unable to print makrdown table -- empty DF.")
    def get_covid_group(self, col = ''):
        return pd.DataFrame(self.__covid_data.groupby('Date')[col].sum().reset_index()).rename(columns={'Date': 'ds', col: 'y'})

    def get_mortality_group(self, col = ''):
        return pd.DataFrame(self.__mortality.groupby('Date')[col].mean().reset_index()).rename(columns={'Date': 'ds',
                                                                                                        'Mortality': 'y'})

    def set_log_params(self, df = None, col = ''):
        df['floor'] = self.__logistic_params[col].floor
        df['cap'] = self.__logistic_params[col].cap
        
    def modeller(self):
        # Prophet requires columns to be labelled ds and y.
        # For the logaritmic model a cap rate and a floor is nessecary.
        # These are inserted into the pandas dataframe.
        # Use a constant cap rate. Right now it's assumed to be constant.
        
        #Modelling total confirmed cases 
        self.__train_ds_confirmed = self.get_covid_group("Confirmed")
        self.set_log_params(self.__train_ds_confirmed, "Confirmed")

        #Modelling deaths
        self.__train_ds_deaths = self.get_covid_group("Deaths")
        self.set_log_params(self.__train_ds_deaths, "Deaths")

        #Modelling active
        self.__train_ds_active = self.get_covid_group("Active")
        self.set_log_params(self.__train_ds_active, "Active")

        #Modelling recovered
        self.__train_ds_recovered = self.get_covid_group("Recovered")
        self.set_log_params(self.__train_ds_recovered, "Recovered")

        #Modelling mortality rate
        self.__train_ds_mortality = self.get_mortality_group("Mortality")
        self.set_log_params(self.__train_ds_mortality, "Mortality")


