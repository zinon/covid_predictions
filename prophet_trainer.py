from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation, performance_metrics
from fbprophet.plot import plot_cross_validation_metric
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

import optparam as op
import proc as xp
import cvmetrics as cv

class ProphetTrainer():
    def __init__(self,
                 variable : str,
                 param    : op.Param(),
                 dloader  : xp.DataLoader()
    ):
        self.__variable   = variable
        self.__param      = param
        self.__dloader    = dloader
        #set these
        self.__data       = self.fetch_data()
        self.__table      = self.__dloader.table
        #
        self.__model      = None
        self.__forecast   = None
        self.__cv_metrics = cv.CVMetrics()
        self.__trained    = self.trainer()
        self.__validated  = self.validator()

    @property
    def variable(self): return self.__variable

    @property
    def param(self): return self.__param

    @property
    def model(self): return self.__model

    @property
    def forecast(self): return self.__forecast

    @property
    def cv_metrics(self):
        return self.__cv_metrics

    def fetch_data(self):
        if self.__variable == "Confirmed":
            return self.__dloader.train_ds_confirmed
        elif self.__variable == "Deaths":
            return self.__dloader.train_ds_deaths
        elif self.__variable == "Active":
            return self.__dloader.train_ds_active
        elif self.__variable == "Recovered":
            return self.__dloader.train_ds_recovered
        elif self.__variable == "Mortality":
            return self.__dloader.train_ds_mortality

        return None
        
    def mean_absolute_percentage_error(self, y_true, y_pred):
        '''Calculates MAPE'''
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(np.abs( (y_true - y_pred) / y_true) ) * 100
            
    def trainer(self):
        self.__model = Prophet(growth=self.__param.growth,
                               interval_width=self.__param.iw,
                               changepoint_prior_scale=self.__param.cpps,
                               changepoint_range=0.95,
                               yearly_seasonality=False,
                               weekly_seasonality=False,
                               daily_seasonality=True,
                               seasonality_mode=self.__param.smode)

        print("prophet_trainer: training %s model"%(self.__param.growth))

        #fit
        if self.__data.empty:
            print("prophet_trainer: data unavailable..."); exit(1)
         
        print("prophet_trainer: fitting data\n", self.__data.head(10))
        self.__model.fit(self.__data)

        #data frame
        future = self.__model.make_future_dataframe(periods=self.__param.periods,
                                                    freq = 'D')

        #logistic params
        if self.__param.floor is not None:
            print("setting floor to", self.__param.floor)
            future['floor'] = self.__param.floor
        if self.__param.cap is not None:
            print("setting cap to", self.__param.cap)
            future['cap'] = self.__param.cap

        #prediction
        if not future.empty:
            self.__forecast = self.__model.predict(future)
        else:
            print("prophet_trainer: empty future"); exit(1)

        #RMSE
        if self.__variable:
            if self.__param.is_rate:
                self.__param.rmse = np.sqrt(mean_squared_error(self.__data['y'],
                                                               self.__forecast['yhat'].head(self.__data.shape[0])))
            else:
                self.__param.rmse = np.sqrt(mean_squared_error(self.__table[self.__variable],
                                                               self.__forecast['yhat'].head(self.__table.shape[0])))


        print("forecast:\n", self.__forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']])
        print("confirmed future tail:\n", future.tail())
        print("cap:", self.__param.cap)
        print("RMSE:", self.__param.rmse)


        return True

    def validator(self):
        self.__cv_metrics.df_cv = cross_validation(self.__model,
                                                   initial = "1 days",
                                                   period = "120 days",
                                                   horizon = "15 days")

        self.__cv_metrics.df_perf = performance_metrics(self.__cv_metrics.df_cv)

        
        
        self.__cv_metrics.manual_mape = self.mean_absolute_percentage_error(self.__cv_metrics.df_cv.y,
                                                                             self.__cv_metrics.df_cv.yhat)

        

    def cv_mape_fig(self):
        '''
            'mse', 'rmse', 'mae', 'mape', 'coverage'
            rolling_window is the proportion of data included in the rolling window of aggregation.
            The default value of 0.1 means 10 aggregation for computing the metric.
        '''
        return  plot_cross_validation_metric(self.__cv_metrics.df_cv,
                                             metric='mape',
                                             rolling_window = 0.1)
        
