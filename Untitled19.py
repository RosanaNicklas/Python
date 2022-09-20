# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""
def inversa(cadena):
    return cadena[::-1]

print(inversa("Hola mundo"))

# Otra opción..

def inversa2(cadena):
  inver = ""
  i = -1
  cont = len(cadena)
  while cont >=1:
    inver = inver + cadena[i] 
    i= i + (-1)
    cont -=1
  return inver
print(inversa2("estoy probando"))

# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""


cadena = input("introduce una cadena por favor: ")
def palindromo(cadena):
    if cadena == cadena[::-1]:
        return True
    else:
        return False    

print(palindromo(cadena))

# otra opción...
def es_palindromo(cadena):
    palabra_invertida = inversa(cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            break
    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print("Es palindromo") # es porque recorrió todo el ciclo for y todas las
                                            # letras son iguales

es_palindromo("radar")

# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""
def superposicion(lista1, lista2):
    contador = 0
    for i in lista1:
        for j in lista2:
            if i == j:
                contador+= 1
    if contador >= 1:
        return True
    else:
        return False    

def superposicion2(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i in lista2:
                return True
            else:
                return False  


lista1 = [1, 2, 3]
lista2 = [1, 4, 8]

print("Resultado superposicion 1: ", superposicion(lista1, lista2))
print("Resultado superposicion 2: ", superposicion2(lista1, lista2))
lista1 = [0, 2, 3]
lista2 = [1, 4, 8]

print("Resultado superposicion 1: ", superposicion(lista1, lista2))
print("Resultado superposicion 2: ", superposicion2(lista1, lista2))