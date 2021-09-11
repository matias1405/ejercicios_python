# Escribí una función plotear_temperaturas() en un archivo
# plotear_temperaturas.py que lea el archivo de datos temperaturas.npy
# (debería tener las 999 mediciones simuladas que creaste recién) y haga un
# histograma de las temperaturas simuladas. 


import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load("../Data/temperaturas.npy") #cargamos el archivo con las temperaturas
plt.hist(temperaturas,bins=200) #creamos el grafico
plt.show() #mostramos el grafico