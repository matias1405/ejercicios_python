from fileparse import parse_csv
import lote
import formato_tabla
from camion import Camion

def leer_camion(nombre_archivo):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo) as f:
        camion_dicts = parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:   
        lista_precios = parse_csv(f, types = [str, float], has_headers = False)
    precios = dict(lista_precios)
    return precios


def hacer_informe(camion, precios):
    informe = []
    for fila in camion:
        cambio = precios[fila.nombre]-float(fila.precio)
        tupla = (fila.nombre, int(fila.cajones),
                 float(fila.precio), cambio)
        informe.append(tupla)
    return informe


def imprimir_informe(informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    # Crear los datos para el informe
    informe = hacer_informe(camion, precios)
    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)

    
def f_principal(parametros):
    if len(parametros) == 3:
        informe_camion(parametros[1], parametros[2])
    elif len(parametros) == 4:
        informe_camion(parametros[1], parametros[2], parametros[3])
    else:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios formato de salida(opcional)')


if __name__ == "__main__":
    import sys
    f_principal(sys.argv)
