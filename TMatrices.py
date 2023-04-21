#Reto 3

def sumaRestaMatrices(pMatriz1,pMatriz2,pOperacion):
    """
    Funcionalidad: Recibe dos matrices y el tipo de operación (“+” para sumar, “-“ para restar) y retorna otra matriz con el resultado
    Entradas:
    -pMatriz1(list): matriz a utilizar
    -pMatriz2(list): matriz a utilizar
    -pOperacion: operacion a realizar entre las matrices
    Salidas:
    -return(list): matriz con el resultado.
    """
    filas=0
    resultado=[]
    while filas <= len(pMatriz1)-1:
        columna=0
        acumulador=[]
        while columna <= len(pMatriz1[filas])-1:
            if pOperacion=="+":
                acumulador.append((pMatriz1[filas][columna])+(pMatriz2[filas][columna]))
            else:
                acumulador.append((pMatriz1[filas][columna])-(pMatriz2[filas][columna]))
            columna+=1
        resultado.append(acumulador)
        filas+=1
    return resultado

def sumaRestaMatricesAux(pMatriz1,pMatriz2,pOperacion):
    """
    Funcionalidad: Valida la entrada de sumaRestaMatrices
    Entradas:
    -pMatriz1(list): matriz a analizar, debe de ser cuadrada y de igual longitud a la segunda
    -pMatriz2(list): matriz a analizar, debe de ser cuadrada y de igual longitud a la primera
    -pOperacion: operacion a realizar entre las matrices, debe ser + o -
    Salidas:
    -return: Envia a la funcion de proceso si todos los valores son correctos.
    """
    if not pOperacion=="+" and not pOperacion=="-":
        return "La operación debe ser “+” para suma y “-” para resta."
    elif not all(len(i)==len(pMatriz1[0]) for i in pMatriz1):
        return "La matriz debe ser cuadrada."
    elif not all(len(i)==len(pMatriz1[0]) for i in pMatriz2):
        return "Las matrices deben ser de la misma dimensión."
    elif not len(pMatriz1)==len(pMatriz2):
        return "Las matrices deben ser de la misma dimensión."
    elif not all(all(isinstance(i, list) and isinstance(j, int) for j in i) for i in pMatriz1):
        return "Todos los elementos de la listas de la matriz deben de ser enteros."
    elif not all(all(isinstance(i, list) and isinstance(j, int) for j in i) for i in pMatriz2):
        return "Todos los elementos de la listas de la matriz deben de ser enteros."
    return sumaRestaMatrices(pMatriz1,pMatriz2,pOperacion)

def ESSumaRestaMatrices(pMatriz1,pMatriz2,pOperacion):
    """
    Funcionalidad: reciba los valores de entrada y trae el resultado de la funcion de validar para imprimir el resultado.
    Entradas:
    -pMatriz1(list): matriz a analizar
    -pMatriz2(list): matriz a analizar
    -pOperacion: operacion a realizar entre las matrices
    Salidas:
    -resultado: resultado de la funcion de proceso
    """
    return sumaRestaMatricesAux(pMatriz1,pMatriz2,pOperacion)
    
#Reto 7

def girarDerecha(pMatriz):
    """
    Funcionalidad: gira una matriz a la derecha
    Entradas:
    -pMatriz1(list): matriz a girar
    -pDireccion(str): derecha
    Salidas:
    -return(list): matriz girada
    """
    resultado=[]
    columna=0
    while columna <= len(pMatriz[1])-1:
        fila=0
        i=1
        acumulador=[]
        while fila <= len(pMatriz)-1:
            acumulador.append(pMatriz[len(pMatriz)-i][columna])
            i+=1
            fila+=1
        resultado.append(acumulador)
        columna+=1
    return resultado

def girarIzquierda(pMatriz):
    """
    Funcionalidad: gira una matriz a la izquierda
    Entradas:
    -pMatriz1(list): matriz a girar
    -pDireccion(str): izquierda
    Salidas:
    -return(list): matriz girada
    """
    return girarDerecha(girarDerecha(girarDerecha(pMatriz)))

def girarMatriz(pMatriz,pDireccion):
    """
    Funcionalidad: envia a la matriz a la funcion necesaria segun la direccion indicada
    -pMatriz1(list): matriz a girar
    -pDireccion(str): direccion a girar la matriz
    Salidas:
    -return: envia a la funcion segun el giro
    """
    if pDireccion=="d":
       return girarDerecha(pMatriz)
    else:
        return girarIzquierda(pMatriz)

def girarMatrizAUX(pMatriz1,pDireccion):
    """
    Funcionalidad: Valida la entrada de girarMatriz
    Entradas:
    -pMatriz1(list): matriz a validar, debe de ser cuadrada.
    -pDireccion(str): direccion a girar la matriz, solo debe ser d o i
    Salidas:
    -return: Envia a la funcion de proceso si todos los valores son correctos.
    """
    pDireccion=pDireccion.lower()
    if not pDireccion=="d" and not pDireccion=="i":
        return "La operación debe ser “d” para derecha e “i” para izquierda."
    elif not all(len(i)==len(pMatriz1[0]) for i in pMatriz1):
        return "La matriz debe ser cuadrada."
    elif not all(all(isinstance(i, list) and isinstance(j, int) for j in i) for i in pMatriz1):
        return "Todos los elementos de la listas de la matriz deben de ser enteros."
    return girarMatriz(pMatriz1,pDireccion)

def ESGirarMatriz(pMatriz1,pDireccion):
    """
    Funcionalidad: reciba los valores de entrada y trae el resultado de la funcion de validar para imprimir el resultado.
    Entradas:
    -pMatriz1(list): matriz a analizar
    -pDireccion(str): direccion a girar la matriz
    Salidas:
    -resultado: resultado de la funcion de proceso
    """
    return girarMatrizAUX(pMatriz1,pDireccion)

print(ESSumaRestaMatrices([[1,2],[3,4]],[[5,6],[7,8]],"+"))
print(ESSumaRestaMatrices([[1,3,2],[1,0,0],[1,2,2]],[[1,0,5],[7,5,0],[2,1,1]],"+"))
print(ESSumaRestaMatrices([[1,3,2],[1,0,0],[1,2,2]],[[1,0],[7,5],[2,1]],"+"))
print(ESSumaRestaMatrices([[1,2],[3,4]],[[5,6],[7,8]],"/"))
print(ESGirarMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],"i"))
print(ESGirarMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],"d"))
    
