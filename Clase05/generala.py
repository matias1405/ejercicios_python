import random
from collections import Counter

def tirar():
    """Funcion que genera una lista con 5 numeros aleatorios representando las
    5 tiradas de dados"""
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada


def es_generala(l):
    """Funcion que comprueba si todos los dados obtuvieron el mismo numero, lo
    que significa hacer generala.
    Si es generala devuelve 'True', sino 'False' """
    if l[0] == l[1] == l[2] == l[3] == l[4]:
        es_gen = True
    else:
        es_gen = False
    return es_gen
    
    
def prob_generala(N):
    """Funcion que devuelve la probabilidad de obtener generala.
    Toma como argumento N el cual es el numero de intentos(cada uno con un
    maximo de 3 tiradas) que tendra el experimento para obtener la
    probabilidad."""
    resultados = [] #iniciamos la lista resultados donde se almacenaran los booleanos para saber si es o no generala.
    for x in range(N): #for para realizar el experimento N veces
        tirada = tirar() #realiza la primera tirada, tirada es una lista
        generala = es_generala(tirada) #evalua si es generala
        for y in range(2): #for para realizar hasta 2 tiradas mas (ademas de la primera)
            if generala == False: #si no es generala
                num_sacados = Counter() #inicializa un contador
                for s in tirada: #en el diccionario-contador se almacena como clave el numero obtenido y como valor la cantidad de veces que salio
                    num_sacados[s] += 1 
                m = num_sacados.most_common(1)  #obtenemos el numero obtenido mas comun en la tirada
                                                #obtenemos como retorno una lista de tuplas con el par (clave, valor)
                #if m[0][1] == 1:
                #   tirada = tirar()
                #else:
                for e, i in enumerate(tirada): 
                # si el elemento i de la tirada es distinto a la clave(numero 
                # mas obtenido) asigna un nuevo valor aleatorio(vuelve a tirar 
                # ese dado)
                    if i != m[0][0]:
                        tirada[e] = random.randint(1,6)
                        generala = es_generala(tirada) #evalua si es generala
            else: #si es generala salir del for
                break
        resultados.append(generala) #agrega un True si se obtuvo generala o un False en caso contrario
    G = sum(resultados) #suma los valores de la lista resultados
    prob = G/N #obtiene la probabilidad
    return prob
    
    
    
if __name__ == "__main__":
    N = 1000000
    prob = prob_generala(N)
    #rint(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')