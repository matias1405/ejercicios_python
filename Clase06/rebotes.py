#rebotes.py
#Ejercicio La pelota que rebota

altura = 100    #altura inicial en metros
num_rebote = 0

while num_rebote < 10:
    num_rebote += 1
    altura *= 0.6   #la pelota rebota hasta un 3/5 de la altura desde que cayó
    print("Numero de rebotes:", num_rebote," altura maxima alcanzada:",
    round(altura, 4), "m")
