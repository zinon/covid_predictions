from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import proc as xp
import tools as xt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def stationary_test_stat(df, a = 0.05):
    """
     Need differencing only if the series is non-stationary. 
    Else, no differencing is needed, that is, d-term=0.

    The null hypothesis of the ADF test is that the time series is non-stationary. 
    So, if the p-value of the test is less than the significance level (0.05) then you 
    reject the null hypothesis and infer that the time series is indeed stationary.
    """
    result = adfuller(df.dropna())
    print('ADF Statistic: %f' % result[0])
    p = result[1]
    print('p-value: %f' % p)
    if p < a:
        print("P-value is greater than the significance level")
        print("difference the series and see how the autocorrelation plot")

    else:
        print("P-value is less than the significance level")
        print("time series is indeed stationary")

def auto_corellation_plots(df):
    # Original Series
    fig, axes = plt.subplots(nrows = 3, ncols =2, figsize=(15,10), sharex=True)
    axes[0, 0].plot(df)
    axes[0, 0].set_title('Original Series')
    plot_acf(df, ax=axes[0, 1])

    # 1st Differencing
    axes[1, 0].plot(df.diff())
    axes[1, 0].set_title('1st Order Differencing')
    plot_acf(df.diff().dropna(), ax=axes[1, 1])

    # 2nd Differencing
    axes[2, 0].plot(df.diff().diff())
    axes[2, 0].set_title('2nd Order Differencing')
    plot_acf(df.diff().diff().dropna(), ax=axes[2, 1])
    return fig, axes


odir = 'images/predictions'
ld = xp.DataLoader(arima=True)

data = ld.train_ds_confirmed
print("arima data:\n", data)

## test statistic
stationary_test_stat(data['Confirmed'])

## data
data_train = data.iloc[ : int(data.shape[0]*0.90) ]
data_valid = data.iloc[ int(data.shape[0]*0.90) : ]
print('Training %d, Validation %d' % (len(data_train), len(data_valid)))

data_train_log = np.log(data_train["Confirmed"])
data_pred = data_valid.copy()



#data_train_arima = data['Confirmed'].values
#data_train_arima = data_train['Confirmed'].values

## prediction
data_train_arima = data_train_log

#buidl model
# p, d, q
model = ARIMA(data_train_arima,
              order=(10, 2, 1))

model_fit = model.fit(trend='c',
                      full_output=True,
                      disp=True)
model_fit.summary()

#forecast
forecast_steps = len(data_valid)
forecast, se, conf  = model_fit.forecast(steps = forecast_steps, alpha = 0.05) #95% CL

data_pred["prediction"]=list(np.exp(forecast))
data_pred["prediction_low"]=list(np.exp(conf[:, 0]))
data_pred["prediction_high"]=list(np.exp(conf[:, 1]))


model_msre = np.sqrt(mean_squared_error( list(data_valid["Confirmed"]),
                                         np.exp(forecast) ) )


print("Root Mean Square Error for ARIMA Model: ", model_msre)


# Make as pandas series
#forecast_series = pd.Series(forecast, index=data_valid.index)
#lower_series = pd.Series(conf[:, 0], index=data_valid.index)
#upper_series = pd.Series(conf[:, 1], index=data_valid.index)

forecast_series = data_pred["prediction"]
lower_series = data_pred["prediction_low"]
upper_series = data_pred["prediction_high"]

#visulaize auto-cor
#auto corellation plots
fig, axes = auto_corellation_plots(data['Confirmed'])
xt.save(fig, xt.name(odir, "arima_auto_correlation_plots" ))

# visualize series
fig = plt.figure(figsize=(12,7), dpi=100)
plt.plot(data_train['Confirmed'], label='Training')
plt.plot(data_valid['Confirmed'], label='Validation')
plt.plot(forecast_series, label='Forecast')
plt.fill_between(lower_series.index,
                 lower_series,
                 upper_series, 
                 color='k',
                 alpha=.15)
plt.title('Forecast vs Actuals')
plt.legend(loc='upper left', fontsize=8)
plt.grid(axis='x', linestyle='--')
plt.grid(axis='y', linestyle='--')

c_txt = "RMSE=%.2f"%(model_msre)
xt.save(fig, xt.name(odir, "arima_train_valid_confidence_series" ), c_txt)

# visualize residual errors
residuals = pd.DataFrame(model_fit.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])

xt.save(fig, xt.name(odir, "arima_residuals" ))

#visualize fit
fig, ax = plt.subplots(figsize=(15,10))
fig = model_fit.plot_predict(dynamic=False, ax = ax)
xt.save(fig, xt.name(odir, "arima_prediction" ))

## visualize prediction
fig, ax = plt.subplots(figsize=(15,10))
plt.plot(data_train.index,
         data_train["Confirmed"],
         label="Train Set",
         marker='o')
plt.plot(data_valid.index,
         data_valid["Confirmed"],
         label="Validation Set",
         marker='*')
plt.plot(data_pred["prediction"],
         label="ARIMA Model Prediction Set",
         marker='^')
plt.legend()
plt.xlabel("Date Time")
plt.ylabel('Confirmed Cases')
plt.title("Confirmed Cases ARIMA Model Forecasting")
plt.xticks(rotation=0)
plt.grid(axis='x', linestyle='--')
plt.grid(axis='y', linestyle='--')
plt.text(0.9, 0.1,
         "RMSE=%.1f"%(model_msre),
         fontsize=12,
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes)

xt.save(fig, xt.name(odir, "arima_train_valid_pred" ), c_txt)

#visualize auto-corellation
fig = plt.figure(figsize=(10, 5))
autocorrelation_plot(data['Confirmed'])
xt.save(fig, xt.name(odir, "arima_auto_correlation" ), c_txt)

#visualize components
fig, (ax1,ax2,ax3) = plt.subplots(3, 1,figsize=(11,7))
results = sm.tsa.seasonal_decompose(x = data_train["Confirmed"],
                                    model="additive",
                                    filt=None,
                                    period=7)

ax1.plot(results.trend)
ax1.text(0.1,
         0.9, "trend",
         size=12,
         ha="center", 
         transform=ax1.transAxes)

ax2.plot(results.seasonal)
ax2.text(0.1,
         0.9, "seasonal",
         size=12,
         ha="center", 
         transform=ax2.transAxes)

ax3.plot(results.resid)
ax3.text(0.1,
         0.9, "trend",
         size=12,
         ha="center", 
         transform=ax3.transAxes)

xt.save(fig, xt.name(odir, "arima_components" ), c_txt)

plt.show()
