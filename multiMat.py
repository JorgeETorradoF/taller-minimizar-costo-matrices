import sys
import numpy as np
import time

pasosMultiMat = []
#recuerda que b es 0
def mat_mult_BU(d, b, e, m):

    #La matriz se construye en cuanto a filas de abajo hacia arriba

    for i in range(e-1,b,-1):

        #en columnas desde i hasta n, pues el caso base es i = j lo que significa coste cero

        for j in range(i,e):

            #caso base diagonales (no me cuesta multiplicar una matriz con nada)

            if i == j:
                m[i][j] = 0

            else:

                #se viene la magia XD

                for k in range(i,j):

                    #se calcula el coste de multiplicar desde i hasta j con una partición intermedia k y se almacena en un temporal

                    aux = m[i][k]+m[k+1][j]+(d[i - 1] * d[k] * d[j])

                    #si el costo temporal es menor a lo que hay actualmente, se sobreescribe, pues estamos minimizando

                    if(aux < m[i][j]):
                        m[i][j] = aux

    # Retornar la matriz de costos calculada
    return m[1][e-1]

def backTrackingMat(m, l,d):
    for i in range(1,l-1):
        if(m[1][i]+m[i+1][l-1]+(d[0]*d[i]*d[l-1]) == m[1][l-1]):
            pasosMultiMat.append(1)
            pasosMultiMat.append(i)
            pasosMultiMat.append(i+1)
            pasosMultiMat.append(l-1)
    return

#función inicial que dio el profe, no la comento pq mucho texto
def mat_mult(A):
    init = time.perf_counter_ns()
    n = len(A)
    m = []
    #llenamos con ceros
    for i in range(0,n):
        aux = []
        for i in range(0,n):
            aux.append(float('inf'))
        m.append(aux)
    cost = mat_mult_BU(A,0,n,m)
    end = time.perf_counter_ns()
    print(f'Tiempo total: {(end - init)}')
    backTrackingMat(m,n, A)
    return cost
# end def

## -------------------------------------------------------------------------
if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "input_file")
    sys.exit(1)
# end if

Af = open(sys.argv[1], 'r').readlines()
A = [int(a) for a in Af][0:]

print('Diagonales de matrices leídas del archivo: \n',A,'\n')
print('el costo mínimo es: ',mat_mult(A))
print("pasando por las matrices: ")
for i in range(0, len(pasosMultiMat)-1,2):
    print(pasosMultiMat[i],' - ', pasosMultiMat[i+1])