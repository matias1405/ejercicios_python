#Ejercicio 4.18: Diccionario con medidas

import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo):
    """funcion que lee el archivo indicado y devuelva una lista de 
    diccionarios con la información de todos los árboles en el archivo. La 
    función debe devolver una lista conteniendo un diccionario por cada árbol 
    con todos los datos."""
    arboleda = []   #crea una lista vacia para contener diccionarios
    with open(nombre_archivo, 'rt') as f:   #abro el archivo y lo apodo f
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]   #crea una lista con el tipo de datos que necesitamos
        rows = csv.reader(f)    #leo el archivo y lo almaceno en rows
        headers = next(rows)    #la primera linea es una lista que contiene los titulos de cada campo
        for row in rows:    #para las siguientes lineas las voy leyendo con un for una a la vez
            try:    #try-except por si al archivo le faltan datos
                #creo un diccionario para cada linea donde las claves esta dada por los headers y los valores por lo que se lee en la linea convertido al tipo dados por la lista types   
                d={name: func(val) for name, func, val in zip(headers, types, row)} 
                arboleda.append(d)  #agrego este diccionario a la lista arboleda
            except ValueError:
                print('Faltan datos en el archivo.')
    return arboleda     #retorna la lista de diccionarios


def medidas_de_especies(lista_espec, lista_arboles):
    """funcion que recibe de una lista de arboles y una lista de especies y 
    genera un diccionario donde las claves son el nombre de una especie y los
    valores son una lista de tuplas con los valores de altura y diametro de
    cada arbol de dicha especie"""
    return {especie: [(x["altura_tot"], x["diametro"]) for x in lista_arboles if x["nombre_com"] == especie] for especie in lista_espec}


def lista_h_y_d(nombre_archivo):
    """funcion que devuelve una lista de tuplas con la altura y los diametros 
    de los Jacarandás"""
    arboleda = leer_arboles(nombre_archivo)  
    return [(x["altura_tot"], x["diametro"]) for x in arboleda if x["nombre_com"] == "Jacarandá"]
    

def histograma_altura(nombre_archivo):
    """funcion que generá un histograma con las alturas de los Jacarandás en 
    el dataset."""
    arboleda = leer_arboles(nombre_archivo)     #genera una lista de diccionarios
    altos = [arbol["altura_tot"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"] #genera una lista con las alturas de una determinada especie de arboles
    plt.hist(altos,bins=100)    #genera un histograma con las alturas
    plt.ylabel("Cantidad de arboles")   #nombre del eje y
    plt.xlabel("Altura en m.")  #nombre del eje x
    plt.title("Alturas de arboles Jacarandás")  #nombre del titulo del grafico


def scatter_hd(lista_de_pares, color="red", especie = "Jacarandá"):
    """función que a partir de una lista de pares de alturas y diametros 
    genera un scatterplot para visualizar la relación entre altura y diámetro 
    de los Jacarandás del dataset."""
    plt.figure()
    h_y_d = np.array(lista_de_pares)    #genera un array a partir de la lista de pares recibida
    h = h_y_d[:, 0]     #genera un vector que solo contenga las alturas
    d = h_y_d[:, 1]     #genera un vector que solo contenga los diametros
    plt.scatter(d,h, s=5.0, c=color, alpha=0.35)       #genera un scatterplot
    plt.xlabel("diametro (cm)")     #nombre del eje x
    plt.ylabel("alto (m)")  #nombre del eje y
    title = "Relación diámetro-alto para " + especie
    plt.title(title)     #nombre del titulo del grafico
    
    
def scatter_especies(nombre_archivo):
    """funcion que a partir de un archivo, realiza un grafico de dispersión
    para una lista de especies de arboles, y normaliza los limites de los 
    gráficos para poder comparar"""
    arboleda = leer_arboles(nombre_archivo)     #lee el archivo
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']   #realiza una lista con las especies deseadas
    medidas = medidas_de_especies(especies, arboleda)   #creo una lista de diccionarios con la informacion de altura y diametro por especie
    colores = ["red", "green", "blue"]  #genera una lisa de colores para diferenciar los graficos
    for i, especie in enumerate(especies):
        scatter_hd(medidas[especie], colores[i], especie)   #realizo el grafico
        plt.xlim(0,300)     #fijo los limites de los graficos a una valor comun para mejorar la comparacion
        plt.ylim(0,50) 




if __name__ == "__main__":
   
   lista = lista_h_y_d("../Data/arbolado-en-espacios-verdes.csv")
   scatter_especies("../Data/arbolado-en-espacios-verdes.csv")