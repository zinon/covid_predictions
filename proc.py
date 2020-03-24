import pandas as pd
import numpy as np

class DataLoader():
    def __init__(self):
        self.__covid_data = None
        self.__country_data = None
        self.__table = None
        self.__leaders = None
        self.__grouped = None
        self.__mortality = None
        self.__train_ds_confirmed = None
        self.__train_ds_deaths = None
        self.__train_ds_mortality = None
        #
        self.__confirmed_floor = 0
        self.__confirmed_population = 250000 *2
        self.__deaths_floor = 0
        self.__deaths_population = 25000
        #
        self.__loaded = self.loader()
        self.__processed = self.processor() if self.__loaded else False
        self.__modelled = self.modeller() if self.__processed else False
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
    def mortality(self):
        return self.__mortality if self.__status else None

    @property
    def train_ds_confirmed(self):
        return self.__train_ds_confirmed

    @property
    def train_ds_deaths(self):
        return self.__train_ds_deaths

    @property
    def train_ds_mortality(self):
        return self.__train_ds_mortality

    @property
    def confirmed_floor(self):
        return self.__confirmed_floor

    @property
    def confirmed_population(self):
        return self.__confirmed_population

    @property
    def deaths_floor(self):
        return self.__deaths_floor

    @property
    def deaths_population(self):
        return self.__deaths_population

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
        print("covid shape", self.__covid_data.shape)
        print("country shape", self.__country_data.shape)

        #get rid of unessecary columns
        self.__covid_data = self.__covid_data.drop(['SNo',
                                                    'Last Update'],
                                                   axis=1)

        self.__covid_data = self.__covid_data.rename(columns={'Country/Region' : 'Country',
                                                              'Province/State' : 'State',
                                                              'ObservationDate':'Date'})

        self.__covid_data["Date"] = pd.to_datetime(self.__covid_data["Date"])
        
        print("\ncovid:", self.__covid_data.head())
        # check null values
        print("Null covid data values", self.__covid_data.isnull().sum() )
        print("Null country data values", self.__country_data.isnull().sum() )

        #sort
        self.__covid_data = self.__covid_data.sort_values(['Date','Country','State'])

        # Add column of days since first case
        self.__covid_data['first_date'] = self.__covid_data.groupby('Country')['Date'].transform('min')
        self.__covid_data['days'] = (self.__covid_data['Date'] -
                                     self.__covid_data['first_date']).dt.days

        
        #countries
        pd_col = 'Pop. Density (per sq. mi.)'
        self.__country_data[pd_col] = self.__country_data[pd_col].str.replace(",","").astype(float)
        #self.__country_data =  self.__country_data.apply(lambda x : x.str.replace(',','.'))
        #self.__country_data["population_density"] = self.__country_data[].astype(float)
        
        #Note: a place may have reported data more than once per day.
        # We convert the data into daily.
        # If the data for the latest day is not available, we will fill it with previous available data.
        #This creates a table that sums up every element in the Confirmed, Deaths, and recovered columns.
        self.__table = self.__covid_data.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].sum()
        #Reset index coverts the index series, in this case date, into an index value. 
        self.__table = self.__table.reset_index()
        self.__table = self.__table.sort_values('Date', ascending=False)
        print("\ntable:", self.__table.head())

        #leaders
        countries = ['Mainland China', 'Italy', 'Germany', 'Iran', 'US', 'Spain']
        self.__leaders = self.__covid_data[self.__covid_data['Country'].isin(countries)]
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
        self.__mortality = self.__covid_data[self.__covid_data['Country'].isin(countries)]
        self.__mortality = self.__mortality.groupby(['Date',
                                                     'Country']).agg({'Deaths': ['sum'],
                                                                      'Recovered': ['sum'],
                                                                      'Confirmed': ['sum']})
        self.__mortality.columns = ['Deaths', 'Recovered', 'Confirmed']
        self.__mortality = self.__mortality.reset_index()
        self.__mortality = self.__mortality[self.__mortality.Deaths != 0]
        self.__mortality = self.__mortality[self.__mortality.Confirmed != 0]

        self.__mortality['mortality_rate'] = self.__mortality.apply(lambda row :
                                                                    ((row.Deaths)/self.if_null((row.Confirmed)))*100,
                                                                    axis=1)


        self.__mortality['dense_normed'] = self.__mortality.apply(lambda row :
                                                                  ((row.Deaths)/self.if_null( row.Confirmed )),
                                                                  axis=1)
        
        return True

    def reporter(self):
        latest = self.__covid_data[self.__covid_data['Date'] == self.__covid_data['Date'].max()]
        print('Last update: ' + str(self.__covid_data["Date"].max()))
        print('Total confirmed cases: %.d' %np.sum(latest['Confirmed']))
        print('Total death cases: %.d' %np.sum(latest['Deaths']))
        print('Total recovered cases: %.d' %np.sum(latest['Recovered']))
        print('Death rate %%: %.2f' % (np.sum(latest['Deaths'])/np.sum(latest['Confirmed'])*100))

        cty = latest.groupby('Country').sum()
        cty['Death Rate'] = cty['Deaths'] / cty['Confirmed'] * 100
        cty['Recovery Rate'] = cty['Recovered'] / cty['Confirmed'] * 100
        cty['Active'] = cty['Confirmed'] - cty['Deaths'] - cty['Recovered']
        cty = cty.drop('days',axis=1).sort_values('Confirmed', ascending=False)

        print("\n", cty.head(10).to_markdown(showindex=True))
        
        #print(tabulate(df, tablefmt="pipe", headers="keys"))
        
    def modeller(self):
        # Prophet requires columns to be labelled ds and y.
        # For the logaritmic model a cap rate and a floor is nessecary.
        # These are inserted into the pandas dataframe.
        # Use a constant cap rate. Right now it's assumed to be constant.
        
        #Modelling total confirmed cases 
        self.__train_ds_confirmed = pd.DataFrame(self.__covid_data.groupby('Date')['Confirmed'].sum().reset_index()).rename(columns={'Date': 'ds', 'Confirmed': 'y'})
        #confirmed_training_dataset.insert(0,'floor',1)
        self.__train_ds_confirmed['floor'] = self.__confirmed_floor
        self.__train_ds_confirmed['cap'] = self.__confirmed_population

        #Modelling mortality rate
        self.__train_ds_mortality = pd.DataFrame(self.__mortality.groupby('Date')['mortality_rate'].mean().reset_index()).rename(columns={'Date': 'ds', 'mortality_rate': 'y'})

        #Modelling deaths
        self.__train_ds_deaths = pd.DataFrame(self.__covid_data.groupby('Date')['Deaths'].sum().reset_index()).rename(columns={'Date': 'ds', 'Deaths': 'y'})
        self.__train_ds_deaths['floor'] = self.__confirmed_floor
        self.__train_ds_deaths['cap'] = self.__deaths_population


