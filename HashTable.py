class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]
        
    def clave_primaria(self, clave):
        return hash(clave) % self.tamano
    
    def agregar(self, clave, model, title, price, status):
        list = [model, title, price, status]
        indice = self.clave_primaria(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                par[1] = model
                par[2] = title
                par[3] = price
                par[4] = status
                return
        self.tabla[indice].append([clave, model, title, price, status])
        
    def obtener(self, clave):
        try:
            indice = self.clave_primaria(clave)
            for par in self.tabla[indice]:
                if par[0] == clave:
                    list = [par[1], par[2], par[3], par[4]]
                    return list
        except KeyError:
            raise KeyError(clave)
    


    def clave_secundaria(self, clave):
        return hash(clave) % self.tamano
    
    def agregar2(self, clave, model, title, price, status):
        list = [model, title, price, status]
        indice = self.clave_secundaria(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                par[1] = model
                par[2] = title
                par[3] = price
                par[4] = status
                return
        self.tabla[indice].append([clave, model, title, price, status])
        
    def obtener2(self, clave):
        try:
            indice = self.clave_secundaria(clave)
            for par in self.tabla[indice]:
                if par[0] == clave:
                    list = [par[1], par[2], par[3], par[4]]
                    return list
        except KeyError:
            raise KeyError(clave)
