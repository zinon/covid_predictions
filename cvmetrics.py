class CVMetrics(object):
    def __init__(self):
        self.__auto_mape = None
        self.__manual_mape = None
        self.__df_cv = None
        self.__df_perf = None
        #self.__fig_mape = None

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

    #@property
    #def fig_mape(self):
    #    return self.__fig_mape

    #@fig_mape.setter
    #def fig_mape(self, x):
    #    self.__fig_mape = x
    
