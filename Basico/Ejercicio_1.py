#Ejercicio 1

#DESCRIBE UNA VARIABLE CON NOMBRE "Notas" QUE TENGA EL VALOR -3.
from decimal import BasicContext


notas = -3
print(notas)

""" Ejercicio 2
Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida: El valor de "s" es "valor de s" y el valor de y es
"valor de y """

s = 25
y = 10
print(f'el valor de s es {s} y el valor de y es {y}')
print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
print('el valor de s es ', s, ' y el valor de y es ', y)
print(f'el valor de s es %s y el valor de y es %s' %(s, y))

# EJERCICIO 3
#Declarar una variable con nombre "name", que tenga el valor de Juan "El profesor"
name = "Juan 'El profesor'"
print(name)


#EJERCICIO 4
import pandas as pd
L = [10, None, 8, 5, None, 20]
df = pd.DataFrame(L)
df