import SwarmPackagePy
from SwarmPackagePy import aba as bees
from SwarmPackagePy import testFunctions


class xd():

    def __init__(self,function):
        self.__function = function

    def fun(self,x):
        return self.__function(x)


class MultiSwarms():



    def __init__(self,n_bees,p_threads,f_function,lb, ub, dimension, iteration):
        n = n_bees//p_threads
        n_rest = n_bees%p_threads
        for i in range(n_rest):
            bees(n+1,f_function,lb, ub, dimension, iteration)
        for i in range(p_threads-n_rest):
            bees(n+1,f_function,lb, ub, dimension, iteration)
        pass


sd = xd(testFunctions.cross_in_tray_function)
print(sd.fun([1.0,1.0]))

#print(fun(,[1.0,1.0]))

#swarms = MultiSwarms(100,4,testFunctions.easom_function,-10,10,2,100)