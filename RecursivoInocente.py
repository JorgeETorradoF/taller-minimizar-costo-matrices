
def mult_mat_rec(i, j, d):
    if i == j:
        return 0
    else:
        mult = float('inf')
        for k in range(i, j):
            t = mult_mat_rec(i, k, d) + mult_mat_rec(k+1, j, d) + d[i-1] * d[k] * d[j]
            if t < mult:
                mult = t
        return mult