
# EJERCICIO 1

"""
    Escriba una función es_bisiesto() que determine si un año determinado es un año
    bisiesto. Un año bisiesto es divisible por 4, pero no por 100.
    También es divisible por 400.
"""

def es_bisiesto():
    print("Comprueba años bisiestos")
    a = int(input("Escriba un año y le dire si es bisiesto: "))
    if a % 4 == 0 and (not(a % 100 == 0)):
        print("El año", a, "es un año bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print("El año", a, "es un año bisiesto porque es multiplo de 400")
    else:
        print("El año", a, "no es bisiesto")

es_bisiesto()

# EJERCICIO 2

"""
    Haz un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
    Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos
    esos años si cada año se aplica la tasa de interés introducida.
    Recordar que un capital C dolares a un interés del x por cien durante n años
    se convierte en C * (1 + x/100)elevado a n (años). Probar el programa
    sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""

def calculo(dinero, inte, cant_anos):
    x = dinero * ((1 + inte/100) **cant_anos)
    return x

def main():
    dolares = int(input("Cuantos dolares: "))
    interes = input("Cuanto interes: ")
    interes = float(interes)
    anos = int(input("Cantidad de años: "))
    print("\n")

    resultado = calculo(dolares, interes, anos)
    print("Cuando pasen", anos, u"años, con un", interes, u"de interes, usted habrá generado", resultado, "dolares.")

main()

# EJERCICIO 3

"""
    Este programa muestra primero el listado de categorías de películas
    y pide al usuario que introduzca el código de la categoría de la película
    y posterior a ello pide que el usuario introduzca el número de días de atraso,
    y así se muestra al final el total a pagar.
"""

# CATEGORIA     PRECIO  CODIGO  RECARGO/DIA DE ATRASO
# FAVORITOS      2.50      1          0.50
# NUEVOS         3.00      2          0.75
# ESTRENOS       3.50      3          1.00
# SUPER ESTRENOS 4.00      4          1.50

while True:
    print("\n")
    print("**************** MENU *******************")
    print("*****************************************")
    print("***********  1. Favoritos ***************")
    print("***********  2. Nuevos    ***************")
    print("***********  3. Estrenos  ***************")
    print("***********  4. Super Estrenos  *********")
    print("***********  99. Salir (del menú)  ******")
    print("*****************************************")

    print("\n")
    
    opcion = int(input("Inserte su opción: "))

    if opcion == 1:
        n_dias = int(input("Inserte numero de días: "))
        total = float(2.50 + (0.50 * n_dias))
        print("EL TOTAL A PAGAR ES: $",total, "dolares")
    elif opcion == 2:
        n_dias = int(input("Inserte numero de días: "))
        total = float(3.00+ (0.75 * n_dias))
        print("EL TOTAL A PAGAR ES: $",total, "dolares")
    elif opcion == 3:
        n_dias = int(input("Inserte numero de días: "))
        total = float(3.50+ (1.0 * n_dias))
        print("EL TOTAL A PAGAR ES: $",total, "dolares")
    elif opcion == 4:
        n_dias = int(input("Inserte numero de días: "))
        total = float(4.0+ (1.50 * n_dias))
        print("EL TOTAL A PAGAR ES: $",total, "dolares")
    elif opcion == 99:
        break
    else:
        print("por favor, escriba una opción correcta. ")
        print("\n")


