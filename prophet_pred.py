
import matplotlib.pyplot as plt
import numpy as np

from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot

from sklearn.metrics import mean_squared_error,r2_score
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

import proc as xp
import tools as xt
import prophet_trainer as pt
import optparam as op
import xquery as xq

import matplotlib.dates as mdates
import matplotlib.ticker as plticker

    
def plotter(train = None, title = "", ylabel = "", fn = "test", plot = True, add_chpts = False, add_cv = True):
#figure
    fig = plt.figure(facecolor='w', figsize=(12, 7))
    ax = fig.add_subplot(111)
    plt.title(title, fontsize=18, y = 1.05)

    ### train result
    train_fig = train.model.plot(train.forecast,  ax = ax, xlabel = "Date", ylabel = ylabel)
    if add_chpts:
        cpts = add_changepoints_to_plot(train_fig.gca(), train.model, train.forecast)
    ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
    c_txt = "RMSE=%.1f MAPE=%.1f%%"%(train.param.rmse, train.cv_metrics.manual_mape)

    #format date
    myFmt = mdates.DateFormatter('%d-%m')
    ax.xaxis.set_major_formatter(myFmt)

    #ticks -  locator puts ticks at regular intervals
    xloc = plticker.MultipleLocator(base=3.0) 
    ax.xaxis.set_major_locator(xloc)

    ## Rotate date labels automatically
    fig.autofmt_xdate()

    
    xt.save(train_fig, xt.name(odir, fn+"_prediction" + ("_changepoints" if add_chpts else "") ), c_txt)

    ### components
    train_comp_fig = train.model.plot_components(train.forecast)
    ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
    xt.save(train_comp_fig, xt.name(odir, fn+"_components"))
    
    ### MAPE
    if add_cv:
        train_cv_mape = train.cv_mape_fig()
        ax = plt.gca()
        ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
        xt.save(train_cv_mape, xt.name(odir, fn+"_cv_mape"))

    
    plt.tight_layout()
    if plot: plt.show()

    plt.close('all')
#
plot = True
confirmed_logistic = False
confirmed_linear = False
deaths_logistic = False
deaths_linear = False
mortality_linear = False

active_logistic = False
active_linear = False
recovered_logistic = True
recovered_linear = False


#case, floor, cap
logparamsGlobal = op.LogParams()
logparamsGlobal += op.LogParam("Confirmed", 0, 3.5e6) #
logparamsGlobal += op.LogParam("Deaths", 0, 250e3) #
logparamsGlobal += op.LogParam("Active", 0, 2.5e6)
logparamsGlobal += op.LogParam("Recovered", 0, 1e6)
logparamsGlobal += op.LogParam("Mortality", 0, 500e3)
print(logparamsGlobal)

logparamsGerm = op.LogParams()
logparamsGerm += op.LogParam("Confirmed", 0, 175e3) #
logparamsGerm += op.LogParam("Deaths", 0, 8e3) #
logparamsGerm += op.LogParam("Active", 0, 2e6)
logparamsGerm += op.LogParam("Recovered", 0, 1e6)
logparamsGerm += op.LogParam("Mortality", 0, 500e3)
print(logparamsGerm)


#output dir
odir = 'images/predictions'

#queries - cuts
q1 = xq.Query("Subperiod", "Confirmed > 0 and Date > '2020-02-15' and Date < '2021-01-01'")

qMort = xq.Query("Subperiod", "Confirmed > 0 and Date > '2020-02-20' and Date < '2021-01-01'")
qAll = xq.Query("All Period", "Confirmed > 0 and Date < '2021-01-01'")
qGerm = xq.Query("Germany", "Confirmed > 0 and Country == 'Germany'")

#tag = ""; query = qMort; logparams = logparamsGlobal
tag = ""; query = qAll; logparams = logparamsGlobal
#tag = "Germany"; query = qGerm; logparams = logparamsGerm

#data loader
dloader = xp.DataLoader(query = query, logistic_params = logparams, prophet = True)

#forecasting periods
periods = 21

#prediction for confirmed - logistic
if confirmed_logistic:
    param = op.Param(growth = 'logistic',
                     floor = logparams['Confirmed'].floor,
                     cap =  logparams['Confirmed'].cap,
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)
 
    train =  pt.ProphetTrainer("Confirmed", param, dloader)

    plotter(train, "Confirmed cases", "Logistic Model", "prophet_logistic_confirmed" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)

#prediction for confirmed - linear
if confirmed_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.5,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Confirmed", param, dloader)

    plotter(train, "Confirmed cases", "Linear Model", "prophet_linear_confirmed"  + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)

#prediction for confirmed - logistic
if deaths_logistic:
    param = op.Param(growth = 'logistic',
                     floor = logparams['Deaths'].floor,
                     cap =  logparams['Deaths'].cap,
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Deaths", param, dloader)

    plotter(train, "Deaths", "Logistic Model", "prophet_logistic_deaths" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)


#prediction for confirmed - logistic
if deaths_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Deaths", param, dloader)

    plotter(train, "Deaths", "Linear Model", "prophet_linear_deaths" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)


#prediction for active - logistic
if active_logistic:
    param = op.Param(growth = 'logistic',
                     floor = logparams['Active'].floor,
                     cap =  logparams['Active'].cap,
                     smode = "additive",
                     periods = periods,
                     cpps = 0.9,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Active", param, dloader)

    plotter(train, "Active", "Logistic Model", "prophet_logistic_active" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)

#prediction for active - linear
if active_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Active", param, dloader)

    plotter(train, "Active", "Linear Model", "prophet_linear_active" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)


#prediction for recovered - logistic
if recovered_logistic:
    param = op.Param(growth = 'logistic',
                     floor = logparams['Recovered'].floor,
                     cap =  logparams['Recovered'].cap,
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Recovered", param, dloader)

    plotter(train, "Recovered", "Logistic Model", "prophet_logistic_recovered" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)

#prediction for recovered - linear
if recovered_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Recovered", param, dloader)

    plotter(train, "Recovered", "Linear Model", "prophet_linear_recovered" + ("_" + tag if tag else ""),
            plot = plot, add_chpts = False)

    
if mortality_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.5,
                     iw = 0.95,
                     is_rate = True)

    train =  pt.ProphetTrainer("Mortality", param, dloader)

    plotter(train, "Mortality", "Linear Model", "prophet_linear_mortality" + ("_" + tag if tag else ""),
            plot = plot, add_cv = False)

