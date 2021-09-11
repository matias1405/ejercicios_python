def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
