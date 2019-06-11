from mpi4py import MPI
from SwarmPackagePy import aba
from SwarmPackagePy import testFunctions
import sys
import os

def sort(table,function):
    change = 1
    while change > 0:
        change = 0
        for i in range(table.__len__()-1):
            if function(table[i])<function(table[i+1]):
                tmp = table[i]
                table[i] = table[i+1]
                table[i+1] = tmp

func = testFunctions.easom_function

if sys.argv.__len__()==4:
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    p_threads = size
    if rank == 0:
        time_start = MPI.Wtime()
        n_bees = int(sys.argv[2])
        iterations = int(sys.argv[3])
        data2 = {
            'n': (n_bees // (p_threads-1)) +1,
            'function': func,
            'lb': -10,
            'ub': 10,
            "dim": 2,
            'iterations': iterations
        }
        out = []
        for i in range(1, p_threads):
            comm.send(data2, dest=i, tag=11)
        for i in range(1, p_threads):
            out.append(comm.recv(source=i,tag=12))
        sort(out,func)
        print("Global best: " + out[0].__str__())
        print("execution time: " + (MPI.Wtime()-time_start).__str__())
    elif (rank > 0) & (rank<p_threads) :
        data = comm.recv(source=0, tag=11)
        optimizer = aba.aba(data['n'], data['function'], data['lb'], data['ub'], data['dim'], data['iterations'])
        comm.send(optimizer.get_Gbest(), dest=0, tag=12)
elif sys.argv.__len__()==3:
    start = os.times().user
    optimizer = aba.aba(int(sys.argv[1]),func,-10,10,2,int(sys.argv[2]))
    print(optimizer.get_Gbest())
    print("execution time: " + (os.times().user - start).__str__())
