import sys
import numpy as np
import time

def mult_mat_rec(i, j, d):
    if i == j:
        return 0
    else:
        mult = np.inf
        for k in range(i, j):
            t = mult_mat_rec(i, k, d) + mult_mat_rec(k+1, j, d) + d[i-1] * d[k] * d[j]
            if t < mult:
                mult = t
        return mult
        
def mat_mult(A):
    init = time.perf_counter_ns()
    n = len(A)
    
    cost = mult_mat_rec(1, n-1, A)
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

