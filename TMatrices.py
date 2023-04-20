#Reto 3

def sumaRestaMatrices(pMatriz1,pMatriz2,pOperacion):
    if not pOperacion=="+" and not pOperacion=="-":
        return "La operación debe ser “+” para suma y “-” para resta."
    elif not all(len(i)==len(pMatriz1[0]) for i in pMatriz1):
        return "Las matrices deben ser de la misma dimensión."
    elif not all(len(i)==len(pMatriz1[0]) for i in pMatriz2):
        return "Las matrices deben ser de la misma dimensión."
    elif not len(pMatriz1)==len(pMatriz2):
        return "Las matrices deben ser de la misma dimensión."
    elif not all(all(isinstance(i, list) and isinstance(j, int) for j in i) for i in pMatriz1):
        return "Todos los elementos de la listas de la matriz deben de ser enteros."
    elif not all(all(isinstance(i, list) and isinstance(j, int) for j in i) for i in pMatriz2):
        return "Todos los elementos de la listas de la matriz deben de ser enteros."
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

print(sumaRestaMatrices([[1,2],[3,6]],[[5,6],[7,8]],"-"))

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

    

print(girarMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],"I"))     
    
