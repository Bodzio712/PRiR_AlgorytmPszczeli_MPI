from SwarmPackagePy import aba as bees
from mpi4py import MPI



def function(x):
    return (x*x)/(x^2-1)

class MultiSwarms():
    def __init__(self,n_bees,p_threads,f_function,lb, ub, dimension, iteration):
        n = n_bees//p_threads
        n_rest = n_bees%p_threads

        for i in range(n_rest):
            bees(n+1,f_function,lb, ub, dimension, iteration)
        for i in range(p_threads-n_rest):
            bees(n+1,f_function,lb, ub, dimension, iteration)
        pass

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    monitor = MultiSwarms(40,4,function(),5,5,1,100)

