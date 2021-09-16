# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers:
            #si tiene encabezados la primera linea es el encabezado
            # Lee los encabezados del archivo
            encabezados = next(filas)
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
        else:
            #si no tiene encabezado ignora cualquier paramentro pasado en la lista select
            select = None
        if select:
            #si se especifica el campo select, busca los indices de la columna correspondiente
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
            
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            # si se especificaron los tipos de datos, transforma los datos al tipo correspondiente
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            
            if has_headers:
                # si tiene encabezados armar un diccionario
                registro = dict(zip(encabezados, fila))
            else:
                #si no tiene encabezados armar una tupla
                registro = tuple(fila)            
            registros.append(registro)

    return registros