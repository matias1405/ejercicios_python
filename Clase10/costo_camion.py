#Ejercicio 7.4: costo_camion.py

import informe_final

def costo_camion(nombre_archivo):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo camion')
    costo = costo_camion(parametros[1])
    print("El costo total es:", costo)


if __name__ == "__main__":
    import sys
    f_principal(sys.argv)

