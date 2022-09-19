import pandas as pd
import numpy as np

# EJERCICIO 1

"""
    1) Haz un programa que calcule los múltiplos de 3
    Para ello primero debe preguntarse al usuario cuántos múltiplos desea añadir.
Nota: Puedes usar un bucle while si lo deseas"""
numero_de_multiplos = int(input("Cuantos multiplos quiere añadir?  "))
for numero in range(1, numero_de_multiplos + 1):
    print(numero * 3)
        


numero_de_multiplos = int(input("Cuantos multiplos quiere añadir?  "))
def multiplo(numero_de_multiplos):
    multi = np.arange(1, numero_de_multiplos + 1)
    for numero in multi:
        print(numero * 3)

multiplo(numero_de_multiplos )        
""""
# 2) Haz lo mismo con np.arange
numero_de_multiplos = int(input("Cuantos multiplos quiere añadir?  "))
def calculo(numero_de_multiplos):
    multi = []
    for numero in range(3, (3*numero_de_multiplos) + 1, 3):
        multi.append(numero)
    return multi
calculo(numero_de_multiplos)
# EJERCICIO 2
numero_de_multiplos = int(input("Cuantos multiplos quiere añadir?  "))
def calculo1(numero_de_multiplos):
    return np.arange(3, (3*numero_de_multiplos) + 1, 3).tolist()
calculo1(numero_de_multiplos)     
    
numero_de_multiplos = int(input("Cuantos multiplos quiere añadir?  "))
def calculo1(numero_de_multiplos):
    return [*range(3, (3*multi) + 1, 3).tolist()]
calculo1(numero_de_multiplos)     

"""
"""
    Dado el listado del apartado 2

    Dada esta lista de variable "listado" y "valores": 10, 10, 20, 20, 20, 30, 40

    Se pide:"""


# 1) Crea un DataFrame con esa información e imprímelo
listado = [10, 10, 20, 20, 20, 30, 40]
print(listado)

# 2) Usa value_counts() para determinar cuántas repeticiones hay de cada número en esa columna
df = pd.DataFrame({"Listado" : listado})
print(df)
# 3) Haz un ".shape" a esa información del value_counts()
print(df.Listado.value_counts())

print(df.Listado.shape)
print(df.Listado.value_counts().shape)
    # NOTA: Escribe: .shape justo al final


# 4) A esa misma instrucción con value_counts() escribe al final ".values"
repeticiones = df.Listado.value_counts().values.tolist()
print(repeticiones)
    # Y veras la información..

    # pasa esa información a lista si puedes

    # y guarda ese listado como "repeticiones"
valores = [df.Listado.value_counts().index]
print(valores)

# 5) A esa información de value_counts() añade al final ".index"

    # Y pasa posteriormente a lista esa información

    # y guarda ese listado con el nombre: "valores"


# 6) Crea un DataFrame con 2 columnas,
df_value_counts = pd.DataFrame({"Valores": valores, "Repeticiones": repeticiones})
printt(df_value_counts)
    # 1 para "valores"

    # 1 para "repeticiones"

    # llámalo: "df_value_counts" (por ejemplo)

    # Y observa..


# 7) Haz lo siguiente: "df.value_counts()"
print(df.value_counts())
# 8) Observa si hay diferencias entre: "df" y "df_value_counts"
print(df)


# EJERCICIO 3
"""
    Comparación de matrices

    Haz el código que testee si esas 2 matrices son iguales

    1)

    Dadas:"""

matriz1 = np.array([[1,2],[3,4]])

matriz2 = np.array([[1,2],[3,8]])


#    -1- RECORRER MATRIZ1 Y MATRIZ2 CON LA PARAMETRIZACIÓN de i y j
#( matriz1 [ i ][ j ] == matriz2 [ i ][ j ] )

"""
    -2- crear una variable contador (inicializada en 0)
    y, cuando detecte, un número de una matriz en una posición concreta,

    y sea diferente del número que tiene LA OTRA MATRIZ..entonces..

    -3- incremento 1 unidad en dicho contador:
    SI los números son DISTINTOS

    --> entonces, que se incremente en 1 unidad..

    de tal manera que si ese contador=0 (al final)--> son todos iguales --> matriz1 = matriz2

    y si es distinto de 0 -> es que POR LO MENOS 1 vez encontró un número diferente

    matriz1 != matriz2

    -4- puedes usar np.arange( ) si lo deseas para las filas y para las columnas

    -5- recuerda el ejercicio del cronómetro para tener una referencia
"""

def test(contador):    
    if contador == 0:
        return "Las matrices son iguales"
    else:
        return f"hay {contador} elementos diferentes" 



def comparacion(matriz1, matriz2):
    contador = 0
    for i in range(2):
        for j in range(2):
            if matriz1[i][j] == matriz2[i][j]:
                contador+= 1
    print("comparacion valor contador: ", contador) 
    test(contador)
comparacion(matriz1, matriz2)  
def comparacion_matrices(matriz1, matriz2):
    return(matriz1 == matriz2).all()
    print(comparacion_matrices(matriz1,matriz2))