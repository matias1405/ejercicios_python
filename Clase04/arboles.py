#Ejercicio 4.18: Diccionario con medidas

import csv

def leer_parque(nombre_archivo):
    arboleada = []
    with open(nombre_archivo, 'rt') as f:
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                d={name: func(val) for name, func, val in zip(headers, types, row)}
                arboleada.append(d)
            except ValueError:
                print('Faltan datos en el archivo.')
    return arboleada

def medidas_de_especies(lista_espec, lista_arboles):
    return {especie: [(x["altura_tot"], x["diametro"]) for x in lista_arboles if x["nombre_com"] == especie] for especie in lista_espec}


if __name__ == "__main__":
    arboleada = leer_parque("../Data/arbolado-en-espacios-verdes.csv")
    #print(arboleada)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    lista_alt_and_diam = medidas_de_especies(especies, arboleada)
    print(lista_alt_and_diam)