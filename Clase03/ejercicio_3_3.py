def tiene_uno(expresion):
    try:
        n = len(expresion)
        i = 0
        tiene = False
        while (i < n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        print("El argumento de la funcion debe ser de tipo cadena")


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
