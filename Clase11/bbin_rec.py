def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        res = lista[medio] == e
        if not res:
            if e > lista[medio]:
                res = bbinaria_rec(lista[medio+1:], e)
            else:
                res = bbinaria_rec(lista[:medio], e)
    return res


if __name__ == '__main__':
    for e in range(10):
        print(bbinaria_rec([0, 1, 3, 4, 5, 7, 8, 9], e))