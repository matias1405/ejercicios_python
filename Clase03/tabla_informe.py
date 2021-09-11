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
                precios[row[0]] = float(row[1])
            except:
                print('Faltan datos en la línea', i, 'del archivo.')
    return precios


def hacer_informe(camion, precios):
    informe = []
    for fila in camion:
        cambio = precios[fila['nombre']]-float(fila['precio'])
        tupla = (fila['nombre'], int(fila['cajones']),
                 float(fila['precio']), cambio)
        informe.append(tupla)
    return informe


camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
