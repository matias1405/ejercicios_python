#geringoso.py
#Ejercicio de geringoso rustico

#Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe',
#'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = input("Ingrese una cadena de texto: ")
capadepenapa = ""   #cadena en geringoso rustico
vocales = "aeiou"
for c in cadena:
    capadepenapa += c
    if c in vocales:
        capadepenapa += "p" + c
print("La cadena en geringoso rustico es:", capadepenapa)
