

#TODOS los ejercicios se deben realizar en formato script con Visual Studio Code
#1)- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una
#función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio."""

def maximo(x,y):
    if x > y:
        return x
    else:
        return y  
print(maximo(10,5))


#2) - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c         

print(max_de_tres(5,8,3))

#3) - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada,
#pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud(valor):
    contador = 0
    while True:
        try:
            valor[contador]
            contador += 1
        except IndexError:
            breaks
    return contador
print(longitud("casa"))


#4) - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

caracter =input("Ingresa un caracter: ")
def vocal(caracter):
    caracter = caracter.lower()
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        return True
    else:
        return False
print(vocal(caracter))   


#5) - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por
#ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.


def suma(numeros):
    suman = 0
    for x in numeros:
        suman = suman + x
    return suman
print(suma([1,2,3,5,6,8]))
print(suma([1,2,3,4]))

def multi(numeros): 
    multin = 1  
    for x in numeros:
        multin = multin * x
    return multin

print(multi([1,2,3,5,6,8]))
print(multi([1,2,3,4]))