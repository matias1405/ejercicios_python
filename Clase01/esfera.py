#esfera.py
#Ejercicio de la esfera

#En tu directorio de trabajo de esta clase, escribí un programa llamado
#esfera.py que le pida al usuario que ingrese por teclado el radio r de una
#esfera y calcule e imprima el volumen de la misma. Sugerencia: recordar que el
#volúmen de una esfera es 4/3 πr^3.

import math as m

r = float(input("Ingrese por teclado el radio r de una esfera: "))
volumen = 4 / 3 * m.pi * r ** 3
print("El volumen de la esfera de radio", r, "es:", volumen)

#entrada: 6
#salida: El volumen de la esfera de radio 6.0 es: 904.7786842338603
