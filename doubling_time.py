from scipy import optimize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import proc as xp
import xquery as xq
import tools as xt

# fit function
def fitfunc1(x, a, b):
    return a * np.exp(b * x)

def fitfunc2(x, a, b, c):
    return a * np.exp(b * x + c * x**2)

def error_prop1(x, a, da, b, db):
    return fitfunc(x, a, b) * np.sqrt( (da/a)**2 + x**2 * db**2 )

def error_prop2(x, a, da, b, db, c, dc):
    return fitfunc(x, a, b, c) * np.sqrt( (da/a)**2 + x**2 * db**2 + x**4 * dc**2 )

def perrors(params_cov):
    return np.sqrt(np.diag(params_cov))

def errors(params_cov):
    """
    The variance of parameters are the diagonal elements
    of the variance-co variance matrix,
    The standard error is the square root of it. np.sqrt(np.diag(pcov))
    """
    
    params_err = perrors(params_cov)
    return np.sqrt(np.diag(params_cov))

def fit(country = '',
        query_raw = None,
        query_der = None,
        do_1st_order = True, do_2nd_order = False, show = True):
    odir = 'images/doubling_time'
    y_data_label = 'Confirmed All'
    _countries = []
    _countries.append(country)
    print(_countries)
    dloader = xp.DataLoader(query = query_raw, countries = _countries)
    df = dloader.leaders.query( query_der.query )

    print("Fit:", df.head())

    x_data = np.flip( df['Days'].to_numpy() )
    y_data = np.flip( df[y_data_label].to_numpy() )

    for i in range(0, len(x_data)):
        print( x_data[i], y_data[i])

    nstd = 1 # to draw 5-sigma intervals
    
    #plot
    fig, ax = plt.subplots(figsize=(15,7))

    if do_1st_order:
        params_opt1, params_cov1 = optimize.curve_fit(f = fitfunc1,
                                                      xdata = x_data,
                                                      ydata = y_data,
                                                      p0=[1, 0.1])


        a1, b1     = params_opt1[0], params_opt1[1]
        params_err1   = perrors(params_cov1)
        da1, db1      = errors(params_cov1)

        params_opt_up1   = params_opt1 + nstd * params_err1
        params_opt_down1 = params_opt1 - nstd * params_err1
        
        fit_nom1  = fitfunc1(x_data, *params_opt1)
        fit_up1   = fitfunc1(x_data, *params_opt_up1)
        fit_down1 = fitfunc1(x_data, *params_opt_down1)

        #doubling times
        r = np.log(2) / b1
        dr = r * db1 / b1

        print("1st order")
        print("Opt params", params_opt1)
        print("Opt param errors", da1, db1)
        print("Opt params up", params_opt_up1)
        print("Opt params down", params_opt_down1)
        print("Doubling time with 1st order")
        print("%.2f +/- %.2f"%(r, dr))

        ax.fill_between(x = x_data,
                        y1 = np.array(fit_up1),
                        y2 = np.array(fit_down1),
                        alpha = .25,
                        color = 'red',
                        label = "%d-$\sigma$ interval"%(nstd))

        plt.plot(x_data,
                 fit_nom1,
                 label='fit: a=%5.3f, b=%5.3f' % tuple(params_opt1),
                 color = 'red')

    if do_2nd_order:
        params_opt2, params_cov2 = optimize.curve_fit(f = fitfunc2,
                                                      xdata = x_data,
                                                      ydata = y_data,
                                                      p0=[1, 0.1, 0.001],
                                                      maxfev=1000)


        a2, b2, c2 = params_opt2[0], params_opt2[1], params_opt2[2]
        params_err2   = perrors(params_cov2)
        da2, db2, dc2 = errors(params_cov2)

        params_opt_up2   = params_opt2 + nstd * params_err2
        params_opt_down2 = params_opt2 - nstd * params_err2


        fit_nom2  = fitfunc2(x_data, *params_opt2)
        fit_up2   = fitfunc2(x_data, *params_opt_up2)
        fit_down2 = fitfunc2(x_data, *params_opt_down2)

        r1 = (-a2 + np.sqrt(a2**2 + 4*b2*np.log(2)) ) / (2*b2)
        r2 = (-a2 - np.sqrt(a2**2 + 4*b2*np.log(2)) ) / (2*b2)

        print("2nd order")
        print("Opt params", params_opt2)
        print("Opt param errors", da2, db2, dc2)
        print("Opt params up", params_opt_up2)
        print("Opt params down", params_opt_down2)
        print("Doubling times with 2nd order")
        print(r1)
        print(r2)


        ax.fill_between(x = x_data,
                        y1 = np.array(fit_up2),
                        y2 = np.array(fit_down2),
                        alpha = .25,
                        color = 'blue',
                        label = "%d-$\sigma$ interval"%(nstd))


        plt.plot(x_data,
                 fit_nom2,
                 label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(params_opt2),
                 color = 'blue')

    plt.scatter(x_data,
                y_data,
                label="Data",
                color = 'black')


    plt.ylabel(y_data_label)
    plt.xlabel('Day')
        
    plt.legend(loc='best')


    plt.legend(loc='upper left',fontsize=18)
    plt.tight_layout()
    xt.save(fig, xt.name(odir, country.replace(" ", "_") ))
    if show:
        plt.show()
    plt.close('all')

    return r, dr

#########################################################################

## query on initial data
q0 = xq.Query("All Period", "Confirmed > 0 and Date < '2021-01-01'")
q3 = xq.Query("Germany", " 'Confirmed All' > 0 and Country == 'Germany'")
q4 = xq.Query("Basic", "Date < '2021-01-01'")
q5 = xq.Query("Basic", "Date < '2020-03-30'")


qbase = xq.Query("Base", "Date > '2020-01-01'")
qkink = xq.Query("Base", "Date > '2020-02-15'")
q1 = xq.Query("Basic", "Date < '2020-03-15'")
q2 = xq.Query("Basic", "Date < '2020-03-30'")
q3 = xq.Query("Basic", "Date < '2021-01-11'")


#query = qkink + q3
qRaw = qbase
print("Raw Query", qRaw)

## query on derived data
qDer = xq.Query("Recent", "RecentDays <=15 ")
print("Derived Query", qDer)


asia = ['Mainland China', 'South Korea', 'Iran']
europe = ['Germany',  'UK', 'Italy', 'Spain', 'France', 'Greece']#, 'Cyprus']
amerika = ['US']
countries = europe + amerika # + asia

doubling_time = []
doubling_time_error = []

show = False




for country in countries:
    print("Doubling time", country)
    t, dt = fit(country = country,
                query_raw = qRaw,
                query_der = qDer,
                do_1st_order = True, do_2nd_order = False, show = show)
    doubling_time.append(t)
    doubling_time_error.append(dt)


results = { 'Country' : countries, 'Doubling Time' : doubling_time, 'Doubling Time Error' : doubling_time_error}
df = pd.DataFrame(results)
df.sort_values(by=['Doubling Time'], ascending=False, inplace = True)

print(df.to_markdown(showindex=True))

#set ticks and labels
#x_labels = sorted([ str(x).strip('00:00:00').strip() for x in df[self.__x].tolist() ])
#print(x_labels)
#plt.xticks(np.arange(min(x_data), max(x_data)+1, 1.0))
#ax.set_xticklabels(labels = x_labels,
#                   rotation = 45 )

#predictions
#df[y_data_label+'Pred'] = fitfunc(x_data, a, b, c)
#df[y_data_label+'PredErr'] = fitfunc(x_data, a, b, c) * np.sqrt( (da/a)**2 + x_data**2 * db**2 + x_data**4 * dc**2 )

        
#alternative
#delta_func = error_prop(x_data, a, da, b, db, c, dc)
#fit_up = fit_nom + delta_func
#fit_down = fit_nom - delta_func

#description






#print( "Target Variable\n", df[y_data_label] )    
#print( df[y_data_label].describe())
#specific prediction
#xpredictions = [11, 23, 35, 47, 59]
#for xpred in xpredictions:
#    print("%i month:"%(xpred),
#          a + b * xpred,
#          np.sqrt(da**2 + db**2 * xpred) )
        





