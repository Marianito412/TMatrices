#Reto 1
def validarMatriz(pMatriz):
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

def diagonalSuperior(pMatriz):
    validacion = validarMatriz(pMatriz)
    if validacion != True:
        return validacion
    
    for i in range(len(pMatriz)):
        for j in range(len(pMatriz[i])):
            if (j<i) and pMatriz[i][j] != 0:
                return False
    return True

print(diagonalSuperior([[1,2,3],[0,12,6],[0,0,-3]]))
#Reto 3

#Reto 6
def soloBajoDiagonal(pMatriz):
    validacion = validarMatriz(pMatriz)
    if validacion != True:
        return validacion
    
    for i in range(len(pMatriz)):
        for j in range(len(pMatriz[i])):
            if ((j<i) and pMatriz[i][j] != 0) or (j>=i and pMatriz[i][j] == 0):
                return False
    return True

print(soloBajoDiagonal([[1,2,3],[1,12,1],[0,0,-3]]))
#Reto 7

#Reto 8
def sumaFila(pLista):
    resultado = 0
    for i in pLista:
        resultado+=i
    return resultado

def sumaColumna(pMatriz, pCol):
    resultado = 0
    for i in pMatriz:
        resultado += i[pCol]
    return resultado

def matrizMagica(pMatriz):
    validacion = validarMatriz(pMatriz)
    if validacion != True:
        return validacion

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
print(matrizMagica([[2,7,6], [9,5,1], [4,3,8]]))

#Reto 9
def validarNotas(pMatriz):
    if pMatriz == []:
        return "Matriz vacia"
    for notas in pMatriz:
        if len(notas) != 8:
            return "la matriz debe tener 8 columnas"
    return True
    
def promedio(pLista):
    resultado = 0
    for i in pLista:
        resultado+=i
    return resultado/len(pLista)

def analizarMatrizNotas(pMatriz):
    validacion = validarNotas(pMatriz)
    if not validacion==True:
        return validacion
    analisis = []
    for notas in pMatriz:
        analisis.append([promedio(notas), min(notas), max(notas), "Aprobado" if promedio(notas) >=70 else "Reprobado"])
    return analisis

print(analizarMatrizNotas([[90,12,90,89,89,89,89,89],[90,67,78,89,89,89,89,89],[0,0,0,0,0,0,0,0]]))