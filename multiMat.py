import sys
import numpy as np
import time
from Memoizado import mult_mat_mem
from RecursivoInocente import mult_mat_rec
from BottomUp import mat_mult_BU

pasosMultiMat = []
#función para el backTracking
def backTrackingMat(m,b,e,d):
    #caso base
    if(b == e):
        #esto es por estética, para agregar el * de la multiplicación 
        if(pasosMultiMat[len(pasosMultiMat)-1] == ")"):
            pasosMultiMat.append("*")
            pasosMultiMat.append(str(b))
        else:
            pasosMultiMat.append(str(b))
            pasosMultiMat.append("*")
        
    #se simula la k, para recorrer y ver en qué orden sale
    for k in range(b,e):
        if(m[b][k]+m[k+1][e]+(d[b-1]*d[k]*d[e]) == m[b][e]):
            #se agrega un * entre )( para que se vea más estético
            if(len(pasosMultiMat) > 0):
                if(pasosMultiMat[len(pasosMultiMat)-1] == ")"):
                    pasosMultiMat.append("*")
            pasosMultiMat.append("(")
            backTrackingMat(m,b,k,d)
            backTrackingMat(m,k+1,e,d)
            #if para corregir estética (que no quede un * y justo despues un cierre de paréntesis)
            if(pasosMultiMat[len(pasosMultiMat)-1] == "*"):
                pasosMultiMat.pop()
            pasosMultiMat.append(")")
    return

#función que se encarga de llamar todo lo del Bottom up
def llamar_mat_mult_BU(A):
    init = time.perf_counter_ns()
    n = len(A)
    m = []
    #llenamos con ceros
    for i in range(0,n):
        aux = []
        for j in range(0,n):
            aux.append(float('inf'))
        m.append(aux)
    cost = mat_mult_BU(A,0,n,m)
    end = time.perf_counter_ns()
    print(f'Tiempo total (ms): {(end - init)}')
    backTrackingMat(m,1,n-1, A)
    return cost

#función inicial que se encarga de llamar todo lo del memoizado
def llamar_mat_mult_mem(A):
    init = time.perf_counter_ns()
    n = len(A)
    m = []
    #llenamos con ceros
    for i in range(0,n):
        aux = []
        for j in range(0,n):
            aux.append(float('inf'))
        m.append(aux)
    cost = mult_mat_mem(1, n -1, A, m)
    end = time.perf_counter_ns()
    print(f'Tiempo total (ms): {(end - init)}')
    backTrackingMat(m,1,n-1, A)
    return cost

## -------------------------------------------------------------------------
if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "input_file")
    sys.exit(1)
# end if

Af = open(sys.argv[1], 'r').readlines()
A = [int(a) for a in Af][0:]

#Se viene el memoizado:
print('\nDiagonales de matrices leídas del archivo: \n',A,'\n')
print("\n=====================================================================================\n")
print("A continuación se muestran los resultados de la ejecución del algoritmo memoizado")
print("\n=====================================================================================\n")
print('el costo mínimo es: ',llamar_mat_mult_mem(A))
print("Multiplicando matrices en el siguiente orden: ")
#quedan un paréntesis inicial y final como de relleno, entonces por estética me los bajo
del pasosMultiMat[0]
pasosMultiMat.pop()
for simbolo in pasosMultiMat:
    print(simbolo, end="")

#reseteamos pasosMultiMat
pasosMultiMat = []

print("\n=====================================================================================\n")
print("A continuación se muestran los resultados de la ejecución del algoritmo Bottom up")
print("\n=====================================================================================\n")
print('el costo mínimo es: ',llamar_mat_mult_BU(A))
print("Multiplicando matrices en el siguiente orden: ")
#quedan un paréntesis inicial y final como de relleno, entonces por estética me los bajo
del pasosMultiMat[0]
pasosMultiMat.pop()
for simbolo in pasosMultiMat:
    print(simbolo, end="")