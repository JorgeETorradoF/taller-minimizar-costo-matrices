import sys
import numpy as np
import time
        
def mult_mat_mem(i, j, d, M):
    if M[i][j] == np.inf:
        if i == j:
            M[i][j] = 0
        else:
            for k in range(i, j):
                t = mult_mat_mem(i, k, d, M) + mult_mat_mem(k+1, j, d, M) + d[i-1] * d[k] * d[j]
                if t < M[i][j]:
                    M[i][j] = t
    return M[i][j]

def mat_mult(A):
    init = time.perf_counter_ns()
    n = len(A)
    
    M = np.zeros((n,n))
    M.fill(np.inf)
    
    cost = mult_mat_mem(1, n -1, A, M)
    
    end = time.perf_counter_ns()
    print(f' Total time is: {(end - init)}')
    return cost
# end def

## -------------------------------------------------------------------------
if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "input_file")
    sys.exit(1)
# end if

Af = open(sys.argv[1], 'r').readlines()
A = [int(a) for a in Af][1:]

print(A)
print(mat_mult(A))

