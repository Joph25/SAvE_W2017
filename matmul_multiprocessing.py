import multiprocessing
import random
import time
import numpy

MATNR = 10
ns1 = 1000
nz1 = ns1


def mat_create_multi(nr):
    # Creates nr matrices with random numbers [-10000 ... 10000]
    m = []
    for j in range(nr):
        m.append([[float(x) / 10 for x in random.sample(range(-100000, 100000), ns1)] for s in range(nz1)])
    return m


# ---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    mat = []
    mat_out = []
    start_time = time.time()  # initialising timer
    mat = mat_create_multi(MATNR)
    print("Creation took ", time.time() - start_time, " seconds")

    start_time = time.time()  # resetting timer
    for i in range(MATNR):  # multiplying matrices one by one using numpy.dot
        mat_out.append(numpy.dot(mat[i], mat[(i + 1) % (len(mat))]))
        # print(mat_out[i])
        # print("------------------------------__")
    print("Simple Multiplikation took ", time.time() - start_time, " seconds")
    start_time = time.time()  # resetting timer

    mat_offset = []
    for i in range(MATNR):  # creating a list of matrices offset by one
        mat_offset.append(mat[(i + 1) % len(mat)])

    p2 = multiprocessing.Pool(processes=4)  # creating a pool for multiprocessing
    M = p2.starmap(numpy.dot, zip(mat, mat_offset))  # multiplying matrices using multiprocessing
    print("Multiprocessing took", time.time() - start_time, " seconds")

    """
    for i in range (MATNR):     #comparing results of multiplication
        if (numpy.all(M[i] == mat_out[i])):
            print ("gleich")
    """
# ---------------------------------------------------------------------------------------------------------
