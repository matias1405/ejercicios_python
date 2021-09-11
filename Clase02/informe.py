import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                lote = {headers[0]:row[0], headers[1]:int(row[1]), headers[2]:float(row[2])}
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

camion = leer_camion('../Data/camion.csv')
total_c = 0
for x in camion:
    total_c += x['cajones']*x['precio']
print("El costo del camion es:", total_c)

#Recaudacion de la venta

precios = leer_precios('../Data/precios.csv')
total_v = 0
for x in camion:
    total_v += x['cajones']*precios[x['nombre']]
print("El costo del camion es:", total_v)

#Balance:

print("\nLa Ganancia fue de:", round(total_v-total_c,2))
