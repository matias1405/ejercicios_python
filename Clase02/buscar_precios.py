#Ejercicio 2.7: Buscar precios

def buscar_precios(fruta):
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            if(fruta == row[0]):
                return print("El precio de un cajon de", fruta, "es:", float(row[1]))
        return print(fruta + " no figura en la lista de precios")


buscar_precios("Frambuesa")
#salida: El precio de un cajon de Frambuesa es: 34.35
buscar_precios("Mango")
#salida: Mango no figura en la lista de precios
buscar_precios("Anana")
#salida: Anana no figura en la lista de precios
buscar_precios("Tomate")
#salida: El precio de un cajon de Tomate es: 66.67
