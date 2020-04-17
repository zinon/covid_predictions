import proc as xp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tools as xt
def smooth(inputdata, w, imax):
    """
    Smooths data for growth factor
    """
    data = 1.0*inputdata
    data = data.replace(np.nan, 1)
    data = data.replace(np.inf, 1)
    
    smoothed = 1.0*data
    normalization = 1
    for i in range(-imax, imax+1):
        if i==0:
            continue
        smoothed += (w**abs(i))*data.shift(i, axis=0)
        normalization += w**abs(i)
    smoothed /= normalization
    return smoothed

def growth_factor(confirmed):
    confirmed_iminus1 = confirmed.shift(1, axis=0)
    confirmed_iminus2 = confirmed.shift(2, axis=0)
    return (confirmed-confirmed_iminus1)/(confirmed_iminus1-confirmed_iminus2)

def growth_ratio(confirmed):
    confirmed_iminus1 = confirmed.shift(1, axis=0)
    return (confirmed/confirmed_iminus1)

def plot_view(df : pd.DataFrame(), col : str, country : str, show : bool):
    # horizontal line at growth rate 1.0 for reference
    x_coordinates = [1, 100]
    y_coordinates = [1, 1]
    odir = 'images/factor_analysis'
    print(df)

    #fig, ax = plt.subplots(figsize=(10, 7))
    df[col+'GF'].plot(title=col+' Growth Factor '+ country)
    plt.plot(x_coordinates, y_coordinates) 
    plt.ylabel("Growth Factor")
    fig=plt.gcf()
    xt.save(plt, xt.name(odir, "growth_factor_"+country ))
    if show: plt.show()

    df[col+'K'].plot(title=col+' Growth Rate ' + country)
    plt.plot(x_coordinates, y_coordinates) 
    plt.ylabel("Growth Rate")
    fig=plt.gcf()
    xt.save(fig, xt.name(odir, "growth_rate1_"+country ))
    if show: plt.show()

    df[col+'k'].plot(title=col+' Growth Rate (k) ' + country)
    plt.plot(x_coordinates, y_coordinates) 
    plt.ylabel("Growth Rate (k)")
    fig=plt.gcf()
    xt.save(fig, xt.name(odir, "growth_rate2_"+country ))
    if show: plt.show()
    

    df[col+'T'].plot(title=col+' Doubling Time (T) ' + country, grid = True, ylim=(0,50))
    plt.plot(x_coordinates, y_coordinates) 
    plt.ylabel("Doubling time (T)")
    fig=plt.gcf()
    xt.save(fig, xt.name(odir, "doubling_time_"+country ))
    if show: plt.show()
    
    df[col+'GR'].plot(title=col+' Growth Ratio ' + country)
    plt.plot(x_coordinates, y_coordinates) 
    plt.ylabel("Growth Ratio")
    fig=plt.gcf()
    xt.save(fig, xt.name(odir, "growth_ratio_"+country ))
    if show: plt.show()
    
    df[col+'D2'].plot(title=col+' 2nd Derivative ' + country)
    plt.plot(x_coordinates, y_coordinates)
    plt.ylabel("2nd Derivative")
    fig=plt.gcf()
    xt.save(fig, xt.name(odir, "second_derivative_"+country ))
    if show: plt.show()
    
    
    
    #df[col+'GR'].plot(title=col+' Growth Rate')




def country_view(df : pd.DataFrame(), country:str):

    #df = df[ df['Confirmed'] > 100 ]
    
    # Date becomes an index of the dataframe after the group_by operation.
    df = df[df['Country'] == country].groupby('Date', as_index = True)[['Confirmed',
                                                                        'Deaths',
                                                                        'Recovered',
                                                                        'Active']].sum()


    #df.index = pd.to_datetime(df.index)

    df['Death Rate'] = df['Deaths'] / df['Confirmed'] * 100


    return df

def augment_view(df : pd.DataFrame(), col : str):

    w = 0.5
    #growth rate or first derivative on log of exponential growth, defined as k in the logistic function
    df[col+'K'] = np.gradient(np.log(df[col]))
    df[col+'K'] = smooth(df[col+'K'], w, 3)

    #growth rate or first derivative on log of exponential growth, defined as k in the logistic function
    df[col+'k'] = np.gradient(df[col]) / df[col]
    df[col+'k'] = smooth(df[col+'k'], w, 3)

    #doubling time
    df[col+'T'] = np.log(2) / df[col+'k']
    #df.loc[df[col+'T'] > 100, col+'T'] = 0
    
    # 2nd Derivative
    df[col+'D2'] = np.gradient(np.gradient(df[col]))
    df[col+'D2'] = smooth(df[col+'D2'], w, 5)
    
    #growth factor
    df[col+'GF'] = growth_factor(df[col])
    df[col+'GF'] = smooth(df[col+'GF'], w, 3)

    # df[i]/df[i-1] = growth ratio
    df[col+'GR'] = growth_ratio(df[col])
    df[col+'GR'] = smooth(df[col+'GR'], w, 5)


    return df

##
country = "Germany"
top = 10
ld = xp.DataLoader(top=top)
df = ld.covid_data
cv = country_view(df, country)
cv = augment_view(cv, "Confirmed")
plot_view(cv, "Confirmed", country, True)
print(country, "\n", cv)

