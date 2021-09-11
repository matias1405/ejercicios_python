#Ejercicio 2.9: costo_camion.py

import csv
def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            costo_total += int(row[1])*float(row[2])
        return costo_total
costo = costo_camion("../Data/camion.csv")
print("El costo total es:", costo)
