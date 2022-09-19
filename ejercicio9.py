# EJERCICIO 1

"""
    Dado este listado de números:

    -3, 150, 0, 499, 500, 1200, -350, 0, 750, 25

    Haz un pequeño algoritmo que haga lo siguiente:

    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante

"""

# 1) Escribir en formato lista
L = [-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]
print(L)
# 2) Haz el propio ejercicio de programación planteado
for numero in L:
    if numero == -numero:
        print("Valor negativo")
    elif numero == 0:
        print(0)
    elif numero > 0 and numero <= 200:
        print(0,200)  
    elif numero >= 200 and numero <= 500:
        print(200,500)   
    elif numero == 500:
        continue
    elif numero > 500 and numero < 1000:
        break
    else:
        print("Valor demasiado grande, desde 1000, en adelante")   

# EJERCICIO 2

# Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40
Listado = [10, 20, 20, 30, 40, 40, 40]
print(Listado)
# 1) Crea la lista e imprimela

# 2) Haz un set de esa lista
print(list(set(Listado)))
# 3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)

# Pista: Puedes almacenar todo en una nueva lista
lista_nueva =[]
for numero in Listado:
    if numero not in lista_nueva:
        lista_nueva.append(numero)
print(lista_nueva)

# EJERCICIO 3

# Dados estos clientes:
bbdd=["Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"]
print(bbdd)
# Usando el continue/break
cliente = input("Introduce nombre de cliente: ")
for nombre in bbdd:
    if nombre == cliente:
        print("El nombre esta en la base de datos")
        break
    else:
        continue
print("El nombre no esta en la base de datos")
cliente = input("Introduce nombre de cliente: ")
# Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

# "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"
