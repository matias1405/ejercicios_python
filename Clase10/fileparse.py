# fileparse.py
import csv

def parse_csv(file, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if has_headers == False and select != None:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    filas = csv.reader(file)
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
    for n, fila in enumerate(filas):
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]
        # si se especificaron los tipos de datos, transforma los datos al tipo correspondiente
        try:
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            
            if has_headers:
                # si tiene encabezados armar un diccionario
                registro = dict(zip(encabezados, fila))
            else:
                #si no tiene encabezados armar una tupla
                registro = tuple(fila)            
            registros.append(registro)
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {n}: No pude convertir {fila}')
                print(f'Fila {n}: Motivo: {e}')
            continue
    return registros

