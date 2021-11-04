 def pascal(n, k):
    if k > n:
        raise "la columna debe ser menor o igual a la fila"
    def _pascal(n, c = 0, l=[]):
        if n >= c:
            aux = [1] * (c+1)
            for i in range(1, c):
                aux[i] = l[i-1] + l[i]
            l = aux
            c += 1
            l = _pascal(n, c, l)
        return l
    res = _pascal(n)
    return res[k]

if __name__ == "__main__":
    print(pascal(5,2))