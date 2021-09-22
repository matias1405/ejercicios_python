#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:08:38 2021

@author: alfaro
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
plt.figure()
dic_distancias = {}

#Graficamos los 12 caminos aleatorios
plt.subplot(2,1,1)
for caminata in range(12):
    camino = randomwalk(N)
    dic_distancias[np.max(abs(camino))] = camino
    plt.plot(camino)
#plt.xlabel("Tiempo")
#plt.ylabel("Distancia al origen")
distancia_max = max(dic_distancias.keys())
distancia_min = min(dic_distancias.keys())
plt.ylim(-distancia_max * 1.1, distancia_max * 1.1)    

# Graficamos la caminata que mas se aleja
plt.subplot(2,2,3)
camino_mas = dic_distancias[distancia_max]
plt.plot(camino_mas)
plt.ylim(-distancia_max * 1.1, distancia_max * 1.1)  

# Graficamos la caminata que menos se aleja
plt.subplot(2,2,4)
camino_menos = dic_distancias[distancia_min]
plt.plot(camino_menos)
plt.ylim(-distancia_max * 1.1, distancia_max * 1.1)  


plt.show()