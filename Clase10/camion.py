class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, item):
        return self.lotes[item]

    def __repr__(self):
        lista = [l for l in self.lotes]
        return f'Camion({lista})'

    def __str__(self):
        cadena = ''
        for l in self.lotes:
            cadena += f'{str(l)} \n'
        return f'Camion con {self.__len__()} lotes: \n{cadena}'

    def precio_total(self):
        return sum((l.costo() for l in self.lotes))

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
