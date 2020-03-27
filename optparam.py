"""
    def __init__(self,
                 rmse : float,
                 floor : int,
                 cap : int,
                 smode : str,
                 periods : int,
                 changepoint_prior_scale : float) :
        self.__rmse = rmse
        self.__floor = floor
        self.__cap = cap
        self.__smode = smode
        self.__periods = periods
        self.__changepoint_prior_scale = changepoint_prior_scale
"""

class Param(object):
    def __init__(self, **kwargs):
        self.___rmse = kwargs.get('rmse', 0.)
        self.__floor = kwargs.get('floor', 0.)
        self.__cap = kwargs.get('cap', 0.)
        self.__smode = kwargs.get('smode', 0.)
        self.__periods = kwargs.get('periods', 0.)
        self.__cpps = kwargs.get('cpps', 0.) #changepoint_prior_scale

    def __post_init__(self):
       pass
   
    def __str__(self):
        buff = "floor = %i, cap = %i, smode = %s, periods = %i, cpps = %f, RMSE = %f"
        return buff%(self.__floor,
                     self.__cap,
                     self.__smode,
                     self.__periods,
                     self.__cpps,
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
