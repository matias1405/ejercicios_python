# ticker.py

from vigilante import vigilar
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 2]] for  row in rows)
    rows = ([func(val) for func, val in zip([str, float, int], row)] for row in rows)
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    return rows

def dict_to_list(lines):
    for line in lines:
        yield [line['nombre'], str(line['precio']), str(line['volumen'])]

def ticker(camion_file, log_file, fmt):
    from formato_tabla import crear_formateador
    import informe_final
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = (row for row in rows if row['nombre'] in camion)
    rows = ([row['nombre'], str(row['precio']), str(row['volumen'])] for row in rows)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        formateador.fila(row)

if __name__ == '__main__':
    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    rows = filtrar_datos(rows, camion)
    for row in rows:
        print(row)
