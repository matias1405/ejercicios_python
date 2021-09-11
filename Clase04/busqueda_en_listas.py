def buscar_u_elemento(lista, elemento):
    for i, e in enumerate(lista):
        if e == elemento:
            return i
    return -1

def buscar_n_elemento(lista, elemento):
    count = 0
    for e in lista:
        if e == elemento:
            count += 1
    return count
    
def maximo(lista):
    m = lista[0]
    for e in lista:
        if m < e:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    for e in lista:
        if m > e:
            m = e
    return m

if __name__ == "__main__":
    print(maximo([1,2,7,2,3,4]))
    #7
    print(maximo([1,2,3,4]))
    #4
    print(maximo([-5,4]))
    #4
    print(maximo([-5,-4]))
    #-4
    