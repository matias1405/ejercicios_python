from fileparse import parse_csv

def leer_camion(nombre_archivo):
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion


def leer_precios(nombre_archivo):
    lista_precios = parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    precios = dict(lista_precios)
    return precios


def hacer_informe(camion, precios):
    informe = []
    for fila in camion:
        cambio = precios[fila['nombre']]-float(fila['precio'])
        tupla = (fila['nombre'], int(fila['cajones']),
                 float(fila['precio']), cambio)
        informe.append(tupla)
    return informe

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio:.2f}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

if __name__ == "__main__":
    informe_camion('../Data/camion.csv', '../Data/precios.csv')