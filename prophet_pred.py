
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
    fig = plt.figure(facecolor='w', figsize=(10, 7))
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

    
    xt.save(train_fig, xt.name(odir, fn+"_prediction" + "_changepoints" if add_chpts else ""), c_txt)

    ### components
    train_comp_fig = train.model.plot_components(train.forecast)
    ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
    xt.save(train_comp_fig, xt.name(odir, fn+"_components"))
    
    ### MAPE
    if add_cv:
        train_cv_mape = train.cv_mape_fig()
        ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
        xt.save(train_cv_mape, xt.name(odir, fn+"_cv_mape"))

    
    plt.tight_layout()
    if plot: plt.show()

    plt.close('all')
#
plot = False
confirmed_logistic = True
confirmed_linear = True
deaths_logistic = True
deaths_linear = True
active_logistic = True
active_linear = True
recovered_logistic = True
recovered_linear = True
mortality_linear = True

#case, floor, cap
logparams = op.LogParams()
logparams += op.LogParam("Confirmed", 0, 900e3)
logparams += op.LogParam("Deaths", 0, 100e3)
logparams += op.LogParam("Active", 0, 900e3)
logparams += op.LogParam("Recovered", 0, 300e3)
logparams += op.LogParam("Mortality", 0, 100e3)
print(logparams)

#output dir
odir = 'images/predictions'

#queries - cuts
q0 = xq.Query("All Period", "Confirmed > 0 and Date < '2021-01-01'")
q1 = xq.Query("Subperiod", "Confirmed > 0 and Date > '2020-02-15' and Date < '2021-01-01'")
q2 = xq.Query("Subperiod", "Confirmed > 0 and Date > '2020-02-20' and Date < '2021-01-01'")

#data loader
dloader = xp.DataLoader(query = q0, logistic_params = logparams)

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

    plotter(train, "Confirmed cases", "Logistic Model", "prophet_logistic_confirmed", plot = plot, add_chpts = False)

#prediction for confirmed - linear
if confirmed_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.5,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Confirmed", param, dloader)

    plotter(train, "Confirmed cases", "Linear Model", "prophet_linear_confirmed", plot = plot, add_chpts = False)

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

    plotter(train, "Deaths", "Logistic Model", "prophet_logistic_deaths", plot = plot, add_chpts = False)


#prediction for confirmed - logistic
if deaths_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Deaths", param, dloader)

    plotter(train, "Deaths", "Linear Model", "prophet_linear_deaths", plot = plot, add_chpts = False)


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

    plotter(train, "Active", "Logistic Model", "prophet_logistic_active", plot = plot, add_chpts = False)

#prediction for active - linear
if active_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Active", param, dloader)

    plotter(train, "Active", "Linear Model", "prophet_linear_active", plot = plot, add_chpts = False)


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

    plotter(train, "Recovered", "Logistic Model", "prophet_logistic_recovered", plot = plot, add_chpts = False)

#prediction for recovered - linear
if recovered_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Recovered", param, dloader)

    plotter(train, "Recovered", "Linear Model", "prophet_linear_recovered", plot = plot, add_chpts = False)

    
if mortality_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = periods,
                     cpps = 0.5,
                     iw = 0.95,
                     is_rate = True)

    train =  pt.ProphetTrainer("Mortality", param, dloader)

    plotter(train, "Mortality", "Linear Model", "prophet_linear_mortality", plot = plot, add_cv = False)

