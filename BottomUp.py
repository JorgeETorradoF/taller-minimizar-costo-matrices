#posdata personal: Recuerda que b es 0
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