#Ejercicio 2.10: camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                costo_total += int(row[1])*float(row[2])
            except ValueError:
                print("# WARNING: ")
        return costo_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
costo = costo_camion(nombre_archivo)
print("El costo total es:", costo)
