class Lote():
    def __init__(self, _nombre, _cajones, _precio):
        self.nombre = _nombre
        self.cajones = _cajones
        self.precio = _precio

    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"

    def __str__(self):
        return f"Lote de {self.cajones} cajones de '{self.nombre}', pagados a ${self.precio} cada uno."
    
    def costo(self):
        return self.cajones * self.precio

    def vender(self, cajones_vend):
        self.cajones -= cajones_vend
        
        
