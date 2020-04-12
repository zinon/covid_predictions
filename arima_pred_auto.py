from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as plticker
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
import numpy as np
import proc as xp
import pandas as pd
import tools as xt
import xquery as xq
odir = 'images/predictions'

#query
qAll = xq.Query("All Period", "Confirmed > 0 and Date < '2021-01-01'")
qGerm = xq.Query("Germany", "Confirmed > 0 and Country == 'Germany'")

#query = qAll; tag = ""
query = qGerm; tag = "Germany"

#data loader
dloader = xp.DataLoader(query = query, arima = True)

df = dloader.train_ds_confirmed['Confirmed']


model = pm.auto_arima(df.values,
                      start_p=1,
                      start_q=1,
                      test='adf',       # use adftest to find optimal 'd'
                      max_p=4,          # maximum p
                      max_q=4,          # maximum q
                      m=1,              # frequency of series
                      d=1,           # let model determine 'd'
                      seasonal=False,   # No Seasonality
                      start_P=1, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)

print(model.summary())

#review the residual plots using stepwise_fit.
#model.plot_diagnostics(variable = 0, lags = 10, figsize=(7,5))
#plt.show()

# Forecast
n_periods = 21
fc, confint = model.predict(n_periods=n_periods,
                            return_conf_int=True)
index_of_fc = np.arange(len(df.values),
                        len(df.values)+n_periods)

# make series for plotting purpose
fc_series = pd.Series(fc, index=index_of_fc)
lower_series = pd.Series(confint[:, 0], index=index_of_fc)
upper_series = pd.Series(confint[:, 1], index=index_of_fc)

# Plot
## visualize prediction
fig, ax = plt.subplots(figsize=(15,10))
plt.plot(df.index,
         df.values,
         label="Data",
         marker='o')

#ax = plt.gca()
ax.yaxis.set_major_formatter(FuncFormatter(xt.y_fmt))
ax.set(xlabel='Day', ylabel='Cases')

#Spacing between each line
intervals = 2
loc = plticker.MultipleLocator(base=intervals)
ax.xaxis.set_major_locator(loc)
ax.grid(which = 'minor')
xmin, xmax, ymin, ymax = plt.axis()
print("x axis", xmin, xmax)
xmaxnew = index_of_fc[-1]
ax.set_xlim(left = -0.5, right = xmaxnew)


plt.plot(df.values, label='Prediction')
plt.plot(fc_series, color='red')
plt.fill_between(lower_series.index, 
                 lower_series, 
                 upper_series, 
                 color='k',
                 alpha=.15,
                 label = "95% CL")

plt.grid(axis='x', linestyle='--')
plt.grid(axis='y', linestyle='--')
plt.xticks(rotation=30)
plt.title("Confirmed")
plt.legend(loc='upper left', fontsize=12)
xt.save(fig, xt.name(odir, ("auto_arima_forecast"+ ("_"+tag if tag else "") ) ))
plt.tight_layout()
plt.show()
