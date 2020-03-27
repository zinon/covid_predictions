from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation, performance_metrics
from fbprophet.plot import plot_cross_validation_metric
import optparam as op
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

class CVMetrics(object):
    def __init__(self):
        self.__auto_mape = None
        self.__manual_mape = None
        self.__df_cv = None
        self.__df_perf = None
        self.__fig_mape = None

    @property
    def auto_mape(self):
        return self.__auto_mape

    @auto_mape.setter
    def auto_mape(self, x):
        self.__auto_mape = x

    @property
    def manual_mape(self):
        return self.__manual_mape

    @manual_mape.setter
    def manual_mape(self, x):
        self.__manual_mape = x

    @property
    def df_cv(self):
        return self.__df_cv

    @df_cv.setter
    def df_cv(self, x):
        self.__df_cv = x

    @property
    def df_perf(self):
        return self.__df_perf

    @df_perf.setter
    def df_perf(self, x):
        self.__df_perf = x

    @property
    def fig_mape(self):
        return self.__fig_mape

    @fig_mape.setter
    def fig_mape(self, x):
        self.__fig_mape = x
    
class ProphetTrainer():
    def __init__(self,
                 param : op.Param(),#:None, None, None, None, None, None, None),
                 data : pd.DataFrame(),
                 table : pd.DataFrame(),
    ):
        self.__param = param
        self.__data = data
        self.__table = table
        #
        self.__model = None
        self.__forecast = None
        self.__cv_metrics = CVMetrics()
        self.__trained = self.trainer()
        self.__validated = self.validator()

    @property
    def param(self): return self.__param

    @property
    def model(self): return self.__model

    @property
    def forecast(self): return self.__forecast

    @property
    def cv_metrics(self):
        return self.__cv_metrics

    def mean_absolute_percentage_error(y_true, y_pred):
        '''Calculates MAPE'''
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(np.abs( (y_true - y_pred) / y_true) ) * 100
            
    def trainer(self):
        self.__model = Prophet(growth="logistic",
                               interval_width=0.95,
                               changepoint_prior_scale=self.__param.cpps,
                               changepoint_range=0.9,
                               yearly_seasonality=False,
                               weekly_seasonality=False,
                               daily_seasonality=True,
                               seasonality_mode=self.__param.smode)

        self.__model.fit(self.__data)
        future = self.__model.make_future_dataframe(periods=self.__param.periods, freq = 'D')
        future['floor'] = self.__param.floor
        future['cap'] = self.__param.cap
        self.__forecast = self.__model.predict(future)
        rmse = np.sqrt(mean_squared_error(self.__table["Confirmed"],
                                          self.__forecast['yhat'].head(self.__table.shape[0])))

        print(self.__forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']])
        print("confirmed future tail - logistic", future.tail())
        print("logistic scan cap", self.__param.cap)
        print("logistic scan RMSE", rmse)

        self.__param.rmse = rmse

        return True

    def validator(self):
        self.__cv_metrics.df_cv = cross_validation(self.__model,
                                                   initial = "30 days",
                                                   period = "60 days",
                                                   horizon = "30 days")

        self.__cv_metrics.df_perf = performance_metrics(self.__cv_metrics.df_cv)

        self.__cv_metrics.fig_mape = plot_cross_validation_metric(self.__cv_metrics.df_cv, metric='mape')

        self.__cv_metrics.manual_mappe = self.mean_absolute_percentage_error(self.__cv_metrics.df_cv.y,
                                                                             self.__cv_metrics.df_cv.yhat)
        
