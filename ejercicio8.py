# EJERCICIO 1
from time import time
import pandas as pd
import numpy as np
# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1) Cadena de texto: hola como estas?

    # Nombre de la variable: "cadena"
cadena = "hola como estas?"

# Descomentar para ejecutar:
print(cadena)

# 2) Longitud de la cadena de texto

# Descomentar para ejecutar:
print(len(cadena))

# 3) Longitud de la cadena de texto calculada con un bucle
def longitud(cadena):
    contador = 0
    for caracter in cadena:
        contador+=1
    return contador


# Descomentar para ejecutar:
print(longitud(cadena))


# EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6

notas = {"Python": 10, "Big Data": 8, "NLP": 6}
print(notas)

values = [value for value in notas.values()]
# Descomentar para ejecutar:
print(values)

media = sum(values)/ len(values)
# Descomentar para ejecutar:
print(media)


# 1) Muestra el valor de las claves
def claves(diccio):
    return diccio.keys()
    

# Descomentar para ejecutar:
print(claves(notas))

# 2) Muestra el valor de los valores del diccionario
def valores(diccio):
    return diccio.values()



# Descomentar para ejecutar:
print(valores(notas))

# 3) Apendiza en el diccionario un nuevo elemento:
notas["Machine Learning"] = 9
    # Machine Learning --> 9
print(notas)
# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.
lista_nueva =[]
    # [["clave1", valor1], ["clave2", valor2]]

lista_nueva = []
for key, value in notas.items():
    listita = []
    listita.append(key)
    listita.append(value)
    print(listita)
    lista_nueva.append(listita)
   
print(lista_nueva)
# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta

# 6) ¿y la nota más baja?
curso = []
notis = []
for key, value in notas.items():
    curso.append(key)
    notis.append(value)
print(curso)
print(notis)   
diccionario = {"Asignatura": curso, "Notas": notas} 
# 7) Ordena el dataframe en orden descendente:
print(diccionario)
# EJERCICIO 3
df = pd.DataFrame(diccionario)
print(df)
mayor = max(df.Notas)
print(mayor)
menor = min(df.Notas)
print(menor)

%%time
def main():
     for i in range(10**8):
         pass

main()

x = time.time()

def main(): 
    for i in np.arange(10**8):
         pass

main()
y=time.time()
tiempo = y-x
print(tiempo)

%%time
def main():
     for i in np.arange(10**8):
         pass
main()
x=time.time()

def main(): 
    for i in np.arange(10**8):
         pass
main()
y=time.time()
tiempo = y-x
print(tiempo)
# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])
A = np.array([1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

print(A)
# se pide:
print(A.T)
# 1) Escribe ese código en Python
matriz_transpuesta = np.empty((3,3), int)
print(matriz_transpuesta)
for i in range(3):
    for j in range(3):
        matriz_transpuesta[i][j]==A[j][i]
print(matriz_transpuesta)        
# 2) Escribe la matriz transpuesta.




def transpuesta(matriz):
    list_main =[]
    for i in range(3):
        list_row = []
        for j in range(3):
            list_row.append(A[j][i]
        list_main.append(list_row)   
    trans = np.array(list_main) 
    return transpuesta
print(transpuesta())

    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.