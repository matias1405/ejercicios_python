# El objetivo de esta actividad es hacer un programa en Python que responda la
# pregunta: ¿Cuántas figuritas hay que comprar para completar el álbum del
# Mundial?
# DATOS:
#   Álbum con 670 figuritas.
#   Cada figurita se imprime en cantidades iguales y se distribuye 
#   aleatoriamente.
#   Cada paquete trae cinco figuritas.

import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def crear_album(figus_total):
    """devuelve un álbum (vector) vacío con figus_total espacios para pegar 
    figuritas."""
    album = np.zeros(figus_total, dtype = np.int64)
    return album

def album_incompleto(A):
    """recibe un vector y devuelve True si el álbum A no está completo y 
    False si está completo."""
    estado = not(np.all(A))
    return estado

def comprar_figu(figus_total):
    """recibe el número total de figuritas que tiene el álbum (dado por el 
    parámetro figus_total) y devuelva un número entero aleatorio que 
    representa la figurita que nos tocó."""
    figu = random.randint(0, figus_total-1)
    return figu

def cuantas_figus(figus_total):
    """genere un álbum nuevo, simule su llenado y devuelva la cantidad de 
    figuritas que se debieron comprar para completarlo."""
    album = crear_album(figus_total)
    cant_fig = 0
    while album_incompleto(album):
        cant_fig += 1
        album[comprar_figu(figus_total)] += 1
    return cant_fig
        
def experimento_figus(n_repeticiones, figus_total):
    """simule el llenado de n_repeticiones álbums de figus_total figuritas y 
    devuelva el número estimado de figuritas que hay que comprar, en promedio, 
    para completar el álbum."""
    l = np.array([cuantas_figus(figus_total) for i in tqdm(range(n_repeticiones))])
    return l.mean()
        
def comprar_paquete(figus_total, figus_paquete):
    """funcion que, dado el tamaño del álbum (figus_total) y la cantidad de 
    figuritas por paquete (figus_paquete), genere un paquete (lista) de 
    figuritas al azar."""
    paquete = [comprar_figu(figus_total) for i in range(figus_paquete)]
    return paquete
    
def cuantos_paquetes(figus_total, figus_paquete):
    """funcion que, dado el tamaño del álbum y la cantidad de figus por 
    paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos 
    paquetes se debieron comprar para completarlo."""
    album = crear_album(figus_total)
    cant_paq = 0
    while album_incompleto(album):
        cant_paq += 1
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figurita in paquete:
            album[figurita] += 1
    return cant_paq
    
def experimento_paquete(n_repeticiones, figus_total, figus_paquete):
    """simula el llenado de n_repeticiones álbums de figus_total figuritas y 
    devuelva el número estimado de paquetes de figus_paquete por paquete que 
    hay que comprar, en promedio, para completar el álbum."""
    l = np.array([cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)])
    return l.mean()

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def mostrar_grafico():
    figus_total = 670
    figus_paquete = 5

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()

    
if __name__ == "__main__":
    print(experimento_figus(1000, 670))
    #print(experimento_paquete(1000, 670, 5))
    #mostrar_grafico()
