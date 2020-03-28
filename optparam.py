
class Param(object):
    def __init__(self, **kwargs):
        self.__growth = kwargs.get('growth', 'linear')
        self.__floor = kwargs.get('floor', None)
        self.__cap = kwargs.get('cap', None)
        self.__smode = kwargs.get('smode', 'additive')
        self.__periods = kwargs.get('periods', 10)
        self.__cpps = kwargs.get('cpps', 0.05) #changepoint_prior_scale
        self.__iw = kwargs.get('iw', 0.95) #interval_width
        self.___rmse = kwargs.get('rmse', 0.)
        
    def __post_init__(self):
       pass
   
    def __str__(self):
        buff = "floor = %i, cap = %i, smode = %s, periods = %i, cpps = %f, iw = %f, RMSE = %f"
        return buff%(self.__floor,
                     self.__cap,
                     self.__smode,
                     self.__periods,
                     self.__cpps,
                     self.__iw,
                     self.__rmse)
    @property
    def rmse(self): return self.__rmse

    @rmse.setter
    def rmse(self, rmse): self.__rmse = rmse
 
    @property
    def cap(self): return self.__cap

    @property
    def smode(self): return self.__smode

    @property
    def periods(self): return self.__periods

    @property
    def floor(self): return self.__floor

    @property
    def cpps(self):
        return self.__cpps

    @property
    def iw(self):
        return self.__iw

    @property
    def growth(self):
        return self.__growth
