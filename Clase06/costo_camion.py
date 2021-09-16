#Ejercicio 6.12: costo_camion.py

import informe_funciones

def costo_camion(nombre_archivo):
    costo_total = 0
    registros = informe_funciones.leer_camion(nombre_archivo)
    for registro in registros:
        ncajones = int(registro['cajones'])
        precio = float(registro['precio'])
        costo_total += ncajones * precio
    return costo_total


if __name__ == "__main__":
    costo = costo_camion("../Data/fecha_camion.csv")
    print("El costo total es:", costo)
