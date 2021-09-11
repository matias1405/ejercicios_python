#Ejercicio 2.14 : Diccionario Geringoso

def diccionario_geriongoso(lista):
    diccionario={}
    for palabra in lista:
        palabra_geringoso = ""
        for c in palabra:
            palabra_geringoso += c
            if c in 'aeiouAEIOU':
                palabra_geringoso += "p" + c
        diccionario[palabra] = palabra_geringoso
    return diccionario

d = diccionario_geriongoso(['banana', 'manzana', 'mandarina'])
print(d)

#salida:
#{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
