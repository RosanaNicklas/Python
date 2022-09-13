# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""
from calendar import c


def max(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return "Son iguales"
    else:
        return num2
       
print(max(56,52))

# EJERCICIO 2

"""
    Definir una función max_de_tres(),
    que tome tres números como argumentos y
    devuelva el mayor de ellos.
"""
def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        print("Son iguales o hay algun error")  

print(max_de_tres(12, 36, 58))

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista
    o una cadena dada.
    (Es cierto que python tiene la función len() incorporada,
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
cadena = "Mi perra se llama Ema"
def longitud(lista):
    contador = 0
    listo = lista.strip()
    print(listo)
    for i in listo:
        contador +=1
    return f"Esta lista o cadena contiene una longitud de {contador}"    
print(longitud(cadena))
# EJERCICIO 4


"""
    Escribir una función que tome un carácter y devuelva True si es una vocal,
    de lo contrario devuelve False.
"""
caracter = input("Introduce un caracter: ")
vocales = ["a", "e", "i", "o", "u"]
def es_vocal(caracter):
    caracter = caracter.lower()
    if caracter in vocales:
        return True
    else:
        return False
print(es_vocal(caracter))

# EJERCICIO 5

"""
    Escribir una función suma() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: suma([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def suma(lista):
    sum = 0
    for num in lista:
        sum = sum + num
    return sum

def multi(lista):
    mult = 1
    for num in lista:
        mult = mult * num
    return mult

print(sum([1,2,3,4]))
print(multi([1,2,3,4]))

print("Enhorabuena acabaste los ejercicios")