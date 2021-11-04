#Ejercicio 7.4: costo_camion.py

import informe_final

def costo_camion(nombre_archivo):
    costo_total = 0
    registros = informe_final.leer_camion(nombre_archivo)
    for registro in registros:
        ncajones = int(registro.cajones)
        precio = float(registro.precio)
        costo_total += ncajones * precio
    return costo_total

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo camion')
    costo = costo_camion(parametros[1])
    print("El costo total es:", costo)


if __name__ == "__main__":
    import sys
    f_principal(sys.argv)

