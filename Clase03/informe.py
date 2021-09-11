import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                lote = dict(zip(headers, row))
                camion.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            try:
                precios[row[0]]=float(row[1])
            except:
                print('Faltan datos en la línea', i, 'del archivo.')
    return precios

#Costo del camion

camion = leer_camion('../Data/fecha_camion.csv')
total_c = 0
for x in camion:
    total_c += int(x['cajones'])*float(x['precio'])
print("El costo del camion es:", total_c)

#Recaudacion de la venta

precios = leer_precios('../Data/precios.csv')
total_v = 0
for x in camion:
    total_v += int(x['cajones'])*precios[x['nombre']]
print("El costo del camion es:", total_v)

#Balance:

print("\nLa Ganancia fue de:", round(total_v-total_c,2))
