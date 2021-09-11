import csv
from collections import Counter
from pprint import pprint


def leer_parque(nombre_archivo, parque):
    arbol = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            if row[10] != parque:
                continue
            try:
                lote = dict(zip(headers, row))
                arbol.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return arbol


def especies(lista_arboles):
    especies = []
    for x in parque:
        especies.append(x['nombre_com'])
    return especies


def contar_ejemplares(lista_arboles):
    tenencias = Counter()
    for s in lista_arboles:
        tenencias[s['nombre_com']] += 1
    print(tenencias.most_common(5))


parque = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
lista_especie = especies(parque)
#print(set(lista_especie), "\n")

#PARQUE LOS ANDES
# {'Ligustro', 'Árbol del cielo (Ailanto o Árbol de los dioses)', 'Ciprés',
# 'Sófora japónica', 'Pino de las canarias', 'Pata de vaca  (Pezuña de vaca)',
# 'Álamo plateado', 'Ginkgo', 'Morera blanca', 'Fresno americano', 'Acacia',
#'Encina', 'Acacia blanca', 'Laurel', 'Corona de cristo', 'Arce negundo',
# 'Liquidambar', 'Tilo', 'Tipa blanca', 'Pino', 'Aguaribay', 'Jacarandá',
# 'Casuarina', 'Trachycarpus', 'Ciprés calvo', 'Gomero', 'Cedro del Himalaya',
# 'Olmo europeo', 'Kauri de corteza lisa', 'Ficus', 'Eucalipto',
# 'Almez (Almecino o Almecina)', 'Palo borracho rosado',
#'Fresno (Fresno común)', 'Plátano', 'Morus', 'Pindó', 'Libocedro (Calocedro)',
#'Cedro', 'Paraíso', 'Pino del Paraná (Pino de Misiones o Pino de Brasil)',
#'Lapacho', 'Acacia frisia'}

#contar_ejemplares(parque)

#[('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21),
#('Palo borracho rosado', 18), ('Lapacho', 12)]


def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []
    for x in lista_arboles:
        if x["nombre_com"] == especie:
            inclinacion.append(x['inclinacio'])
    return inclinacion


def especimen_mas_inclinado(lista_arboles):
    lista = []
    for x in set(especies(lista_arboles)):
        lista_inclinacion = obtener_inclinaciones(lista_arboles, x)
        for y in lista_inclinacion:
            tupla = (float(y), x)
            lista.append(tupla)
    return lista
#lista_inclinacion = obtener_inclinaciones(parque, "Tipa blanca")
#pprint(lista_inclinacion)


lista = especimen_mas_inclinado(parque)
pprint(max(lista))
