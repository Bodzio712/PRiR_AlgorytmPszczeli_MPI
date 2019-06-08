from SwarmPackagePy import aba as bees


class MultiSwarms():



    def __init__(self,n_bees,p_threads,f_function,lb, ub, dimension, iteration):
        n = n_bees//p_threads
        n_rest = n_bees%p_threads
        for i in range(n_rest):
            bees(n+1,f_function,lb, ub, dimension, iteration)
        for i in range(p_threads-n_rest):
            bees(n+1,f_function,lb, ub, dimension, iteration)
        pass
