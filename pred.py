import matplotlib.pyplot as plt
import numpy as np
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error,r2_score
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

import proc as xp


def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
                    if str(val).split(".")[1] == "0":
                        return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])
    return y

#
ld = xp.DataLoader()

#datasets
ds_confirmed = ld.train_ds_confirmed
ds_mortality = ld.train_ds_mortality
ds_deaths = ld.train_ds_deaths
tb = ld.table

#prediction for confirmed - logistic
c_log_prophet = Prophet(growth="logistic",
                    interval_width=0.98,
                    # changepoint_prior_scale=0.05,
                    #changepoint_range=0.9,
                    yearly_seasonality=False,
                    weekly_seasonality=False,
                    daily_seasonality=True,
                    seasonality_mode='additive')

c_log_prophet.fit(ds_confirmed)
c_log_future = c_log_prophet.make_future_dataframe(periods=20)
c_log_future['cap'] = ld.confirmed_population
c_log_future['floor'] = ld.confirmed_floor
print("confirmed future tail - linear", c_log_future.tail())
c_log_forecast = c_log_prophet.predict(c_log_future)
print(c_log_forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']])
print("RMSE for Linear Prophet Model - Confirmed:",
      np.sqrt(mean_squared_error(tb["Confirmed"],
                                 c_log_forecast['yhat'].head(tb.shape[0]))) )


#prediction for confirmed - linear
c_lin_prophet = Prophet(growth="linear",
                    interval_width=0.98,
                    # changepoint_prior_scale=0.05,
                    #changepoint_range=0.9,
                    yearly_seasonality=False,
                    weekly_seasonality=False,
                    daily_seasonality=True,
                    seasonality_mode='additive')

c_lin_prophet.fit(ds_confirmed)
c_lin_future = c_lin_prophet.make_future_dataframe(periods=20)
#c_lin_future['cap'] = ld.confirmed_population
#c_lin_future['floor'] = ld.confirmed_floor
print("confirmed future tail -linear", c_lin_future.tail())
c_lin_forecast = c_lin_prophet.predict(c_lin_future)
print(c_lin_forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']])
print("RMSE for Linear Prophet Model - Confirmed:",
      np.sqrt(mean_squared_error(tb["Confirmed"],
                                 c_lin_forecast['yhat'].head(tb.shape[0]))) )



# Mortality rate model
m_prophet = Prophet ()
m_prophet.fit(ds_mortality)
m_future = m_prophet.make_future_dataframe(periods=31)
m_forecast = m_prophet.predict(m_future)

# Deaths model
d_prophet = Prophet(growth="logistic",
                    interval_width=0.95)
d_prophet.fit(ds_deaths)

d_future = m_prophet.make_future_dataframe(periods=7)
d_future['cap'] = ld.deaths_population
d_future['floor'] = ld.deaths_floor
d_forecast = m_prophet.predict(d_future)


#illustrate
#fig, ax = plt.subplots(figsize=(15,7))


c_log_fig = c_log_prophet.plot(c_log_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

c_log_comp_fig = c_log_prophet.plot_components(c_log_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

c_lin_fig = c_lin_prophet.plot(c_lin_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

c_lin_comp_fig = c_lin_prophet.plot_components(c_lin_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

m_fig = m_prophet.plot(m_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

d_fig = d_prophet.plot(d_forecast)
ax = plt.gca(); ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))



plt.tight_layout()
plt.show()

