

# Ejercicio 1

#**1)** Definir una función inversa() que calcule la inversión de una cadena.
 #Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    return cadena[::-1]
print(inversa("estoy probando"))  

#**2)** Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    if palabra == inversa(palabra):
        return True
    else:
        return False
print(es_palindromo("cosa"))    

#**3)** Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
 #Escribir la función usando el bucle for anidado.

def superposicion(lista1,lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
               return True
            else:
                return False  

  
print(superposicion([1,2,3,5,4],[11,12,13,14,15]))               



