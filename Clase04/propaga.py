def propagar(lista):
    long = len(lista)
    for i in range(long):
        if lista[i] == 1 and i < long-1:
            if lista[i+1] == 0:
                lista[i+1] = 1
    for i in range(long-1, 0, -1):
        if lista[i] == 1 and i > 0:
            if lista[i-1] == 0:
                lista[i-1] = 1
    return lista


if __name__ == "__main__":
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    #[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
    print(propagar([ 0, 0, 0, 1, 0, 0]))
    #[1, 1, 1, 1, 1, 1]
    print(propagar([ 0, 0, -1, 0, 0, 1]))
    #[0, 0, -1, 1, 1, 1]