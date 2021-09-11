# Ejercicio 3.17 : Tablas de Multiplicar

# Escribí un programa tablamult.py que imprima de forma prolija las tablas de
# multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la
# multiplicación, usando sólo sumas alcanza.


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in lista:
    if x == 0:
        print(f'{lista[x]:>9d}', end='')
    else:
        print(f'{lista[x]:>4d}', end='')
print('')
print('----------------------------------------------')
for y in lista:
    n = 0
    for x in lista:
        if x == 0:
            print(f'{y:>3}: {n:>4}', end='')
        else:
            print(f'{n:>4}', end='')
        n += y
    print('')
