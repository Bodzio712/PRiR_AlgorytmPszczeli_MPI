from mpi4py import MPI
import SwarmPackagePy
from SwarmPackagePy import aba
from SwarmPackagePy import testFunctions


#def cross_in_tray_function(x):
#    return round(-0.0001*(abs(sin(x[0])*sin(x[1])*exp(abs(100 -
#                            sqrt(sum([i**2 for i in x]))/pi))) + 1)**0.1, 7)

class MultiSwarms():
    def __init__(self,n_bees,p_threads,f_function,lb, ub, dimension, iteration):
        n = n_bees//p_threads
        n_rest = n_bees%p_threads

        for i in range(n_rest):
            pass
            #bees(n+1,f_function,lb, ub, dimension, iteration)
        for i in range(p_threads-n_rest):
            pass
            #bees(n+1,f_function,lb, ub, dimension, iteration)
        pass

class xd():

    def __init__(self,function):
        self.__function = function

    def fun(self,x):
        return self.__function(x)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p_threads = 4

sd = xd(testFunctions.cross_in_tray_function)
print(sd.fun([1.0,1.0]))

if rank == 0:
    data = {'n': 7,'function': testFunctions.cross_in_tray_function, 'type':'only_swarms','lb':-10,'ub':10,"dim":2, 'iterations':100}#'stricted_swarms' - other type
    for i in range(1,p_threads):
        print(i)
        comm.send(data, dest=i, tag=11)
elif rank > 0:
    data = comm.recv(source=0, tag=11)
    optimizer = aba.aba(data['n'],data['function'], data['lb'], data['ub'], data['dim'], data['iterations'])
    print(data['n'])


