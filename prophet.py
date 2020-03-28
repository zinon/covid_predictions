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

def plotter(train = None, title = "", ylabel = "", fn = "test", add_chpts = False):
#figure
    fig = plt.figure(facecolor='w', figsize=(10, 7))
    ax = fig.add_subplot(111)
    plt.title(title, fontsize=18, y = 1.05)

    #train result
    train_fig = train.model.plot(train.forecast,  ax = ax, xlabel = "Date", ylabel = ylabel)
    if add_chpts:
        cpts = add_changepoints_to_plot(train_fig.gca(), train.model, train.forecast)
    ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
    c_txt = "RMSE=%.1f MAPE=%.1f%%"%(train.param.rmse, train.cv_metrics.manual_mape)
    xt.save(train_fig, xt.name(odir, fn+"_prediction"), c_txt)

    #components
    train_comp_fig = train.model.plot_components(train.forecast)
    ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
    xt.save(train_comp_fig, xt.name(odir, fn+"_components"))
    
    #MAPE
    train_cv_mape = train.cv_mape_fig()
    ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
    xt.save(train_cv_mape, xt.name(odir, fn+"_cv_mape"))

    
    plt.tight_layout()
    plt.show()

    
#
confirmed_logistic = True
confirmed_linear = False
deaths_logistic = False
deaths_linear = False
mortality_linear = True

odir = 'images'

q0 = xq.Query("All Period", "Confirmed > 0 and Date < '2021-01-01'")
q1 = xq.Query("Subperiod", "Confirmed > 0 and Date > '2020-02-15' and Date < '2021-01-01'")

#
ld = xp.DataLoader(query = q0)

#datasets
ds_confirmed = ld.train_ds_confirmed
ds_mortality = ld.train_ds_mortality
ds_deaths = ld.train_ds_deaths
tb = ld.table
periods = 21

#prediction for confirmed - logistic
if confirmed_logistic:
    param = op.Param(growth = 'logistic',
                     floor = 0.,
                     cap =  900e3,
                     smode = "additive",
                     periods = 21,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Confirmed", param, ds_confirmed, tb)

    plotter(train, "Confirmed cases", "Logistic Model", "prophet_logistic_confirmed", False)

#prediction for confirmed - linear
if confirmed_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = 21,
                     cpps = 0.5,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Confirmed", param, ds_confirmed, tb)

    plotter(train, "Confirmed cases", "Linear Model", "prophet_linear_confirmed", False)

#prediction for confirmed - logistic
if deaths_logistic:
    param = op.Param(growth = 'logistic',
                     floor = 0,
                     cap =  50e3,
                     smode = "additive",
                     periods = 21,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Deaths", param, ds_deaths, tb)

    plotter(train, "Deaths", "Logistic Model", "prophet_logistic_deaths", False)


#prediction for confirmed - logistic
if deaths_linear:
    param = op.Param(growth = 'linear',
                     smode = "additive",
                     periods = 21,
                     cpps = 0.05,
                     iw = 0.95)

    train =  pt.ProphetTrainer("Deaths", param, ds_deaths, tb)

    plotter(train, "Deaths", "Linear Model", "prophet_linear_deaths", False)


if mortality_linear:
    pass
    # Mortality rate model
m_prophet = Prophet ()
m_prophet.fit(ds_mortality)
m_future = m_prophet.make_future_dataframe(periods=31)
m_forecast = m_prophet.predict(m_future)



#illustrate
#fig, ax = plt.subplots(figsize=(15,7))

# plot logistic

#free
c_lin_fig = c_lin_prophet.plot(c_lin_forecast, xlabel = "Date", ylabel = "Confirmed cases")
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
xt.save(c_lin_fig, xt.name(odir, "prophet_linear_confirmed"), "RMSE=%.1f"%(c_lin_rmse) )

#linear
c_lin_fig = c_lin_prophet.plot(c_lin_forecast, xlabel = "Date", ylabel = "Confirmed cases")
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
xt.save(c_lin_fig, xt.name(odir, "prophet_linear_confirmed"), "RMSE=%.1f"%(c_lin_rmse) )

c_lin_comp_fig = c_lin_prophet.plot_components(c_lin_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
xt.save(c_lin_comp_fig, xt.name(odir, "prophet_linear_confirmed_components"))

m_fig = m_prophet.plot(m_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
xt.save(m_fig, xt.name(odir, "prophet_mortality"))

d_fig = d_prophet.plot(d_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
xt.save(d_fig, xt.name(odir, "prophet_deaths"))


