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
    backTrackingMat(m,1,n-1, A)
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
print("Multiplicando matrices en el siguiente orden: ")
#quedan un paréntesis inicial y final como de relleno, entonces por estética me los bajo
del pasosMultiMat[0]
pasosMultiMat.pop()
for simbolo in pasosMultiMat:
    print(simbolo, end="")