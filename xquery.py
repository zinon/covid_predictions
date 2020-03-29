"""
Class to handle queries for logical expressions
"""
class Query:
    def __init__(self,
                 name = 'unnamed',
                 query = ''):
        self.__name = name
        #
        self.__query = self.__format(query)

    def __repr__(self):
        return self.__name

    def __str__(self):
        return "Query '%s' : %s"%(self.__name,
                                  self.__query)

    def __add__(self, other): 
        return Query(self.__name + "+" + other.__name,
                     self.__combine(other.__query) )
    
    @property
    def name(self):
        return self.__name

    @property
    def query(self):
        return self.__query

    def __format(self, _string = ''):
        if not _string:
            return _string
        return "(%s)"%(_string)

    def __join(self, _string = ''):
        if not _string:
            print("Query: empty query - nothing to join")
            return False
        
        self.__query += "&" + self.__format(_string)
        return True

    def __combine(self, string : str):
        return self.__format(self.__query) + '&' + self.__format(string)
    
    def add(self, condition = ''):
        return self.__join(condition)


    
