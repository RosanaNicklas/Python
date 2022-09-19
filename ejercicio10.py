# EJERCICIO 1
import numpy as np
# Crea una matriz con ayuda numpy:
matriz = np.zeros((4,4))
print(matriz)
# 1) Cuya matriz contenga 4 filas por 4 columnas de ceros

for x in range(len(matriz)):
    for y in range(len(matriz)):
        if x == y:
            matriz[x][y] = 1

            
print(matriz)        
# 2) Apartir de la matriz de ceros crea la matriz identidad


# EJERCICIO 2

# Crea una matriz con ayuda numpy:
matriz1 = np.array([[3, 6, 8],
                    [20, 5, 7],
                    [10, 14, 1]])
print(matriz1)             
# Primera fila contenga: 3, 6, 8
# Segunda fila contenga: 20, 5, 7
# Tercera fila contenga: 10, 14, 1
print(matriz1.T)

# 1) Crea la transpuesta de esta matriz
trans = []
for x in len(matriz1):
    trans.append([])
    for y in len(matriz1[x]):
        trans[x][y]== matriz1[y][x]
print(trans)        
# 2) Muestra el tamaño de la matriz

# 3) Muestra las dimensiones
print(matriz1.size)
print(matriz1.shape)
# 4) ¿La matriz tiene valores menores de 0?


np.all(matriz1 < 0)      
np.any(matriz1 > 10)  
7 in matriz1       
# 5) ¿La matriz tiene algún valor mayor de 10?
 
# 6) Coge una muestra de 5 valores de esa matriz usando linespace
muestra = np.linspace(matriz1.min(), matriz1.max(), 5)
print(muestra)
# 7) La matriz contiene el valor 7

# 8) Crea una copia de esa matriz en una única dimensión
matriz1.flatten()
# 9) Crea una copia de esa matriz en una única dimensión, en este caso usando un bucle y una lista vacia
lista = []
for x in range(len(matriz1)):
    for y in range(len(matriz1[x])):
        lista.append(matriz1[x][y])
print(lista)
matriz2 = np.array(lista)
# 10) Realiza a esta última matriz creada con flatten la potencia de 3
pow(matriz2, 3)
import pandas as pd
df = pd.DataFrame(muestra)
df