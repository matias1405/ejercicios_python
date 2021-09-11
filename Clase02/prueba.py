import os

with open("Downloads/Ejercicios/ejercicios_python/Data/camion.csv", "rt") as f:
    next(f)
    for line in f:
        print(line, end='')
