#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 19/04/2023 5:53pm
#Ultima version:  20/04/2023 7:03pm
#Version: 3.10.6

#Definición de funciones

#Validación
def validarMatriz(pMatriz):
    """
    Funcionalidad: Valida la matriz dada
    Entradas:
    -pMatriz(list): La matriz a validar
    Salidas:
    -return(bool): True si la matriz es válida, False si
    """
    largoMatriz = len(pMatriz)
    largoFila = len(pMatriz[0])

    if largoFila != largoMatriz:
        return "la matriz debe ser cuadrada"
    largo = len(pMatriz[0])
    for i in pMatriz:
        if len(i) != largo:
            return "Cada elemento de la matriz debe poseer la misma cantidad de columnas"
        if not isinstance(pMatriz[0], list):
            return "Cada elemento debe ser de tipo lista"
    return True

#Reto 3
def sumaRestaMatrices(pMatriz1,pMatriz2,pOperacion):
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
    return sumaRestaMatricesAux(pMatriz1,pMatriz2,pOperacion)

#Reto 6
def soloBajoDiagonal(pMatriz):
    """
    Funcionalidad: Verifca que sólo debajo de la diagonal está 100% llena de ceros y no hay ceros en ningún otro lugar
    Entradas:
    -pMatriz(list): La matriz a validar
    Salidas:
    -return(bool): True si sólo debajo de la diagonal está 100% llena de ceros y no hay ceros en ningún otro lugar si no False
    """
    for i in range(len(pMatriz)):
        for j in range(len(pMatriz[i])):
            if ((j<i) and pMatriz[i][j] != 0) or (j>=i and pMatriz[i][j] == 0):
                return False
    return True

def ESSoloBajoDiagonal(pMatriz):
    """
    Funcionalidad: Corre verificaciones y si pasan llama a soloBajoDiagonal
    Entradas:
    -pMatriz(list): La matriz a validar
    Salidas:
    -return(bool): True si sólo debajo de la diagonal está 100% llena de ceros y no hay ceros en ningún otro lugar si no False
    """
    validacion = validarMatriz(pMatriz)
    if validacion != True:
        return validacion
    return soloBajoDiagonal(pMatriz)

#Reto 7

def girarDerecha(pMatriz):
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
    return girarDerecha(girarDerecha(girarDerecha(pMatriz)))

def girarMatriz(pMatriz,pDireccion):
    if pDireccion=="d":
       return girarDerecha(pMatriz)
    else:
        return girarIzquierda(pMatriz)

def girarMatrizAUX(pMatriz1,pDireccion):
    pDireccion=pDireccion.lower()
    if not pDireccion=="d" and not pDireccion=="i":
        return "La operación debe ser “d” para derecha e “i” para izquierda."
    elif not all(len(i)==len(pMatriz1[0]) for i in pMatriz1):
        return "La matriz debe ser cuadrada."
    elif not all(all(isinstance(i, list) and isinstance(j, int) for j in i) for i in pMatriz1):
        return "Todos los elementos de la listas de la matriz deben de ser enteros."
    return girarMatriz(pMatriz1,pDireccion)

def ESGirarMatriz(pMatriz1,pDireccion):
    return girarMatrizAUX(pMatriz1,pDireccion)

#Reto 8
def sumaFila(pLista):
    """
    Funcionalidad: Suma todos los elementos de una lista
    Entradas:
    -pLista(list): La lista a sumar
    Salidas:
    -resultado(int): La suma de la lista dada
    """
    resultado = 0
    for i in pLista:
        resultado+=i
    return resultado

def sumaColumna(pMatriz, pCol):
    """
    Funcionalidad: Suma todos los elementos de una columna
    Entradas:
    -pLista(list): La matriz sobre la que operar
    -pColumna(int): La columna a sumar
    Salidas:
    -resultado(int): La suma de la columna dada
    """
    resultado = 0
    for i in pMatriz:
        resultado += i[pCol]
    return resultado

def matrizMagica(pMatriz):
    """
    Funcionalidad: Determina si una matriz es o no mágica
    Entradas:
    -pMatriz(list): La matriz a determinar
    Salidas:
    -resultado(int): La suma de una de las filas o un texto indicando que no es una matriz mágica
    """
    resultados = []
    diagonal = 0
    diagInversa = 0
    for i in range(len(pMatriz)):
        resultados.append(sumaFila(pMatriz[i]))
        for j in range(len(pMatriz[i])):
            resultados.append(sumaColumna(pMatriz, j))
            if i==j:
                diagonal += pMatriz[i][j]
            if i == len(pMatriz[i])-1-j:
                diagInversa += pMatriz[i][j]
    resultados += [diagonal, diagInversa]
    if all(x == resultados[0] for x in resultados):
        return resultados[0]
    else:
        return "No es una matriz mágica"

def ESMatrizMagica(pMatriz):
    """
    Funcionalidad: Corre verificaciones y si pasan llama a matrizMagica
    Entradas:
    -pMatriz(list): La matriz a validar
    Salidas:
    -return(bool): True si sólo debajo de la diagonal está 100% llena de ceros y no hay ceros en ningún otro lugar si no False
    """
    validacion = validarMatriz(pMatriz)
    if validacion != True:
        return validacion
    return matrizMagica(pMatriz)

#Reto 9
def validarNotas(pMatriz):
    """
    Funcionalidad: valida que todas las notas en una matriz tenga un mínimo de 8 notas cada uno
    Entradas:
    -pMatriz: La matriz a validar
    Salidas:
    return(bool): True si la matriz es válida, de lo contrario un mensaje explicando el problema
    """
    if pMatriz == []:
        return "Matriz vacia"
    for notas in pMatriz:
        if len(notas) != 8:
            return "la matriz debe tener 8 columnas"
    return True
    
def promedio(pLista):
    """
    Funcionalidad: Retorna el promedio de una lista de números
    Entradas:
    -pLista: La lista de números a promediar
    Salidas:
    return(float): El promedio de la lista
    """
    resultado = 0
    for i in pLista:
        resultado+=i
    return resultado/len(pLista)

def analizarMatrizNotas(pMatriz):
    """
    Funcionalidad: Analiza las notas dadas consiguiendo la menor, mayor, el promedio y el estado del estudiante
    Entradas:
    -pMatriz(list): La matriz de notas
    Salidas:
    -analisis(list): La matriz de analisis con la información obtenida
    """
    analisis = []
    for notas in pMatriz:
        analisis.append([promedio(notas), min(notas), max(notas), "Aprobado" if promedio(notas) >=70 else "Reprobado"])
    return analisis

def ESAnalizarMatrizNotas(pMatriz):
    """
    Funcionalidad: Corre verificaciones y si pasan llama a analizarMatrizNotas
    Entradas:
    -pMatriz(list): La matriz a validar
    Salidas:
    -return(list): La matriz de analisis con la información obtenida
    """
    validacion = validarNotas(pMatriz)
    if not validacion==True:
        return validacion
    return analizarMatrizNotas(pMatriz)

#Programa principal
print("Reto 3")
print("Entrada: [[1,2],[3,4]],[[5,6],[7,8]],'+'")
print("Salida: ")
print(ESSumaRestaMatrices([[1,2],[3,4]],[[5,6],[7,8]],"+"))

print("Entrada: [[1,3,2],[1,0,0],[1,2,2]],[[1,0,5],[7,5,0],[2,1,1]],'+'")
print("Salida: ")
print(ESSumaRestaMatrices([[1,3,2],[1,0,0],[1,2,2]],[[1,0,5],[7,5,0],[2,1,1]],"+"))

print("Entrada: [[1,3,2],[1,0,0],[1,2,2]],[[1,0],[7,5],[2,1]],'+'")
print("Salida: ")
print(ESSumaRestaMatrices([[1,3,2],[1,0,0],[1,2,2]],[[1,0],[7,5],[2,1]],"+"))

print("Entrada: [[1,2],[3,4]],[[5,6],[7,8]],'/'")
print("Salida: ")
print(ESSumaRestaMatrices([[1,2],[3,4]],[[5,6],[7,8]],"/"))
print()

print("Reto 6")
print("Entrada: [[1,2,3],[1,12,1],[0,0,-3]]")
print("Salida: ")
print(ESSoloBajoDiagonal([[1,2,3],[1,12,1],[0,0,-3]]))
print()

print("Reto 7")
print("Entrada: [[1,2,3,4],[5,6,7,8],[9,10,11,12]],'i'")
print("Salida: ")
print(ESGirarMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],"i"))
print("Entrada: [[1,2,3,4],[5,6,7,8],[9,10,11,12]],'d'")
print("Salida: ")
print(ESGirarMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],"d"))
print()

print("Reto 8")
print("Entrada: [[2,7,6], [9,5,1], [4,3,8]]")
print("Salida: ")
print(ESMatrizMagica([[2,7,6], [9,5,1], [4,3,8]]))
print()

print("Reto 9")
print("Entrada: [[90,12,90,89,89,89,89,89],[90,67,78,89,89,89,89,89],[0,0,0,0,0,0,0,0]]")
print("Salida: ")
print(analizarMatrizNotas([[90,12,90,89,89,89,89,89],[90,67,78,89,89,89,89,89],[0,0,0,0,0,0,0,0]]))



