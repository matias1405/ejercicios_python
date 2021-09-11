#Ejercicio 4.5 : Invertir lista

def invertir_lista(lista):
    lista_inv = []
    for e in lista:
        lista_inv.insert(0, e)
    return lista_inv

if __name__ == "__main__":
    print(invertir_lista([1, 2, 3, 4, 5]))
    #[5, 4, 3, 2, 1]
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
    #['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']