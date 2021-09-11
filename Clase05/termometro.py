# Supongamos que una persona se compra un termómetro que mide la temperatura
# con un error aleatorio de distribución normal con media 0 y desvío estándar
# de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de
# 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n
# valores medidos por el termómetro. Escribí una función llamada medir_temp(n)
# que simule n mediciones y las devuelva en una lista.

# Escribí una función llamada resumen_temp(n) que realice una simulación de n
# temperaturas (usando la función medir_temp(n)) y devuelva una tupla con el
# valor máximo, el mínimo, el promedio y la mediana (en ese orden) de estas n
# mediciones. 

# Ampliá el código de la función medir_temp(n) para que además de devolver las
# temperaturas simuladas, guarde el vector con estas temperaturas en el
# directorio Data de tu carpeta de ejercicios, en un archivo llamado
# temperaturas.npy. Hacé que corra n = 999 veces.

import random
import numpy as np

def medir_temp(n):
    """genera una lista de tempertaturas con una distribucion normal y las
    almacena en un archivo .npy, luego retorna una lista con dichas 
    temperaturas"""
    variaciones = [random.normalvariate(0, 0.2) for x in range(n)] #genero numeros aleatorios con distribucion normal
    medidas = [x + 37.5 for x in variaciones] #cambio el punto central de la distribucion normal a 37.5
    temp_array = np.array(medidas) #lo convierto a a un array de np
    np.save("../Data/temperaturas", temp_array) #guardo el vector como un archivo .npy
    return medidas
    
def resumen_temp(n):
    medidas = medir_temp(n) #obtengo un lista con las medidas de temperatura
    medidas.sort() #ordeno la lista
    maximo = round(max(medidas), 2) #obtengo el maximo y lo redondeo con dos decimales
    minimo = round(min(medidas), 2) #obtengo la temperatura minima
    prom = round(sum(medidas)/n, 2) #obtengo el promedio o media
    indice_central = len(medidas)//2 #obtengo la posicion del elemento central
    if len(medidas) % 2 == 0: #si es par obtengo la mediana
        mediana = round((medidas[indice_central - 1] + medidas[indice_central]) / 2, 2)
    else: #si es impar obtengo la mediana
        mediana = round(medidas[indice_central], 2)
        
    return maximo, minimo, prom, mediana #retorno una tupla con el maximo, el minimo, el promedio y la mediana

if __name__ == "__main__":
    print(resumen_temp(999))