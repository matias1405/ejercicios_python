def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posición de ese elemento en la lista (si se encuentra en la 
    lista)
    Devuelve la posición donde se podrá insertar el elemento para que la 
    lista permanezca ordenada (si no está en la lista)
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:       
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos == -1:
        if lista[medio] < x:
            pos = medio + 1
        else:
            pos = medio
    return pos


def insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posición de ese elemento en la lista (si se encuentra en la 
    lista)
    Inserta el elemento y devuelve la posición donde se insertó el elemento 
    para que la lista permanezca ordenada (si no está en la lista)
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:       
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos == -1:
        if lista[medio] < x:
            pos = medio + 1
        else:
            pos = medio
        lista.insert(pos, x)
    return pos

def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    lista = [0]*n
    secuencias = [lista.copy()]
    for l in range(2**n-1):
        lista = incrementar(lista)
        secuencias.append(lista.copy())
    return secuencias
        
        
if __name__ == "__main__":
    secuencias = listar_secuencias(21)