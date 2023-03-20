class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]
        
    def hash(self, clave):
        return hash(clave) % self.tamano
    
    def agregar(self, clave, valor):
        indice = self.hash(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                par[1] = valor
                return
        self.tabla[indice].append([clave, valor])
        
    def obtener(self, clave):
        indice = self.hash(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                return par[1]
        raise KeyError(clave)
