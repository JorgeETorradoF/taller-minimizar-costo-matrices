import numpy as np

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