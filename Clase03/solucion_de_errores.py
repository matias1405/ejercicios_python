# solucion_de_errores.py
# Ejercicios de errores en el código

#%%

# Ejercicio 3.1. Función tiene_a()
# Comentario: El error era de sintaxis y estaba ubicado en la Linea 7 y 8.
#   Lo corregí quitando la linea 7 y pasar la linea 8 al final de la funcion
#   fuera del bloque while
#   La funcion no detecta las A (mayuscula) por lo que en el primer caso de
#   prueba devuelve false
#   A continuación va el código corregido


from pprint import pprint
import csv


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%

# Ejercicio 3.2. Función tiene_a(), nuevamente
# Comentario: El error era de tipo semantico y estaba ubicado en la linea 1, 4,
# 5 y 8
#   Puntualmente, en las lineas 1, 4 y 5 faltaban los dos puntos ":" y los
#   agregue
#   En el if la condición estaba mal escrita, tenia un = de asignación, y lo
#   reemplaze por un == de comparacion
#   En el último return de la función, estaba escrito "Falso" asi que lo corregí
#   A continuación va el código corregido


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%

# Ejercicio 3.3. Función tiene_uno()
# Comentario: El error era un error en tiempo de ejecución, de tipo TypeError
# El error ocurria en la linea dos cuando era llamado por tercera vez la funcion
#   Este error se soluciona agregando un bloque try - except que atrape errores
#   de tipo TypeError
#   A continuación va el código corregido


def tiene_uno(expresion):
    try:
        n = len(expresion)
        i = 0
        tiene = False
        while (i < n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        print("El argumento de la funcion debe ser de tipo cadena")


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%


# Ejercicio 3.4. Función suma(a, b)
# Comentario: El error era de tipo semántico
# El error ocurria porque la funcion no retornaba ningun valor despues de
# calcular la suma
#   Este error se soluciona agregando un return que devuelva el resultado de la
#   suma "c"
#   A continuación va el código corregido


def suma(a, b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")


#%%


# Ejercicio 3.5. Función leer_camion(nombre_archivo)
# Comentario: El error era de tipo semántico
# El error ocurria porque se creaba un diccionario registro al cual la lista
# camion hacia referencia en sus elementos. Con ciclo for nosotros
# actualizabamos el valor de las claves del diccionario registro, lo cual
# modificaba (o actualizaba mejor dicho) el valor de la lista camion al mismo
# tiempo.
#   Este error se soluciona sacando la linea de creacion de registro en la
#   linea 7 y colocarla al principio del ciclo for. Esto logra que en cada
#   iteracion del ciclo, el diccionario registro se elimine y cree uno vacio,
#   eliminando la actualizacion de la lista camion debido a referencias.
#   A continuación va el código corregido


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion


camion = leer_camion('../Data/camion.csv')
pprint(camion)
