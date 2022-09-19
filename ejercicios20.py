"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    return  caracter * n
print(generar_n_caracteres(5, "x"))
# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""
def procedimiento(lista):
    for i in lista:
        print("*" * i)

print(procedimiento([5, 6, 8]))
# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""
def mas_larga(lista):
    larga = ""
    for i in lista:
        if len(i) > len(larga):
            larga = i
    return larga    
print(mas_larga(["osa", "casa", "piramide"]))       

# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""


def filtrar_palabras(lista, n):
    lista_mas = []
    for i in lista:
        if len(i) > n:
            lista_mas.append(i)
    return lista_mas
print(filtrar_palabras(["osa", "casa", "popeye","camarero"], 4))        
# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""
cadena = input("Ingrese una cadena de texto :")
def mayusculas(cadena):
    cont = 0
    for caracter in cadena:
        if caracter == caracter.upper():
            print(caracter)
            cont +=1
    return cont
print(mayusculas(cadena))

# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

edades = (20, 30, 50, 40, 85, 75, 69, 45)
print(edades)
def mayores_de_20(tupla):
    mayor20 = []
    cont = 0
    for edad in edades:
        if edad > 20:
            mayor20.append(edad)
            cont +=1
    return mayor20, cont
print(mayores_de_20(edades))
# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""
nombres = ["Ana", "Agustin", "Antonio", "Isabel", "Rosa", "Alberto"]
print(nombres)
letra = "a"
def empiezan_A( lista):
    cont = 0
    for nombre in lista:
        nombre = nombre.lower()
        if nombre[0] == "a":
            cont +=1
    return cont
print(empiezan_A(nombres))           


# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def vocales(palabra):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letra in palabra:
        letra = letra.lower()
        if letra == "a":
            a+=1
        elif letra == "e":
            e+=1
        elif letra == "i":
            i+=1
        elif letra =="o":
            o+=1
        elif letra == "u":
            u+=1
    print(f" a = {a}, e = {e}, i = {i}, o = {o}, u = {u}")
print(vocales("constelacion"))