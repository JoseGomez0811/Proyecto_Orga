class TablaHash:
    def __init__(self):
        # self.model_primary_table = [[] for _ in range(3)]
        # self.model_overflow_table = [[] for _ in range (6)]
        # self.title_primary_table = [[] for _ in range(3)]
        # self.title_overflow_table = [[] for _ in range (6)]

        self.model_primary_table = [[], [], []]
        self.model_overflow_table = [[], [], [], [], [], []]
        self.title_primary_table = [[], [], []]
        self.title_overflow_table = [[], [], [], [], [], []]

        self.model_key_list = []
        self.title_key_list = []
    
    def primary_hash_function(self, key):
        return hash(key) % 3

    def insert_by_model(self, key, model, title, price, status):
        try:
            primary_index = self.primary_hash_function(key)
            primary_list = self.model_primary_table[primary_index]
            if len(primary_list) < 3:
                primary_list.append([key, [model, title, price, status]])
                self.model_key_list.append(key)
                print("Primario")
            else:
                overflow_index = primary_index % 6
                overflow_list = self.model_overflow_table[overflow_index]
                if len(overflow_list) < 3:
                    overflow_list.append([key, [model, title, price, status]])
                    self.model_key_list.append(key)
                    print("Overflow")
                # else:
                    # raise ValueError("No hay espacio en la tabla de hash")
        except ValueError:
            print("No hay espacio en la tabla de hash")

    def search_by_model(self, key):
        primary_index = self.primary_hash_function(key)
        primary_list = self.model_primary_table[primary_index]
        for item in primary_list:
            if item[0] == key:
                return item[1]
        
        overflow_index = primary_index % 6
        overflow_list = self.model_overflow_table[overflow_index]
        for item in overflow_list:
            if item[0] == key:
                return item[1]
            
        return None
    
    def modify_by_model(self, key, model, title, price, status):
        primary_index = self.primary_hash_function(key)
        primary_list = self.model_primary_table[primary_index]
        for item in primary_list:
            if item[0] == key:
                item[1] = [model, title, price, status]
        
        overflow_index = primary_index % 6
        overflow_list = self.model_overflow_table[overflow_index]
        for item in overflow_list:
            if item[0] == key:
                item[1] = [model, title, price, status]
            
        return None

    def delete_by_model(self, key):
        primary_index = self.primary_hash_function(key)
        primary_list = self.model_primary_table[primary_index]
        for item in primary_list:
            if item[0] == key:
                item[0] = None
                item[1] = None
        
        overflow_index = primary_index % 6
        overflow_list = self.model_overflow_table[overflow_index]
        for item in overflow_list:
            if item[0] == key:
                item[0] = None
                item[1] = None
            
        return None

    def write_txt_by_model(self):
        for key in self.model_key_list:
            primary_index = self.primary_hash_function(key)
            primary_list = self.model_primary_table[primary_index]
            for item in primary_list:
                if item[0] == key:
                    with open ("ModelKeyDB.txt", "a") as data:
                        data.write(f"{item[0]}: {item[1]}\n")
            
            # data.close()
            
            overflow_index = primary_index % 6
            overflow_list = self.model_overflow_table[overflow_index]
            for item in overflow_list:
                if item[0] == key:
                    with open ("ModelKeyDB.txt", "a") as data:
                        data.write(f"{item[0]}: {item[1]}\n")
            
            # data.close()
            
        return None
    
    def write_table_by_model(self):

        with open ("ModelKeyDB.txt", "r") as data:
            for line in data:
                info = line.strip().split(":")
                key = info[0]
                value = info[1]
                
                value_split = value.strip().split(",")
                
                model = value_split[0].strip("[' '")
                title = value_split[1].strip("' '")
                price = value_split[2].strip("' '")
                status = value_split[3].strip("' ']")

                self.insert_by_model(key, model, title, price, status)

            data.close()

        return None

    def empty_txt_by_model(self):
        with open("ModelKeyDB.txt", "w+") as data:
            datos = data.readlines()
            data.writelines(datos)
            data.close()
        return







    def secundary_hash_function(self, key):
        return hash(key) % 3

    def insert_by_title(self, key, model, title, price, status):
        try:
            primary_index = self.secundary_hash_function(key)
            primary_list = self.title_primary_table[primary_index]
            if len(primary_list) < 3:
                primary_list.append([key, [model, title, price, status]])
                self.title_key_list.append(key)
                print("Primario")
            else:
                overflow_index = primary_index % 6
                overflow_list = self.title_overflow_table[overflow_index]
                if len(overflow_list) < 3:
                    overflow_list.append([key, [model, title, price, status]])
                    self.title_key_list.append(key)
                    print("Overflow")
                # else:
                #     raise ValueError("No hay espacio en la tabla de hash")
        except ValueError:
            print("No hay espacio en la tabla de hash")
            
    def search_by_title(self, key):
        primary_index = self.secundary_hash_function(key)
        primary_list = self.title_primary_table[primary_index]
        for item in primary_list:
            if item[0] == key:
                return item[1]
        
        overflow_index = primary_index % 6
        overflow_list = self.title_overflow_table[overflow_index]
        for item in overflow_list:
            if item[0] == key:
                return item[1]
            
        return None
    
    def modify_by_title(self, key, model, title, price, status):
        primary_index = self.secundary_hash_function(key)
        primary_list = self.title_primary_table[primary_index]
        for item in primary_list:
            if item[0] == key:
                item[1] = [model, title, price, status]
        
        overflow_index = primary_index % 6
        overflow_list = self.title_overflow_table[overflow_index]
        for item in overflow_list:
            if item[0] == key:
                item[1] = [model, title, price, status]
            
        return None

    def delete_by_title(self, key):
        primary_index = self.secundary_hash_function(key)
        primary_list = self.title_primary_table[primary_index]
        for item in primary_list:
            if item[0] == key:
                item[0] = None
                item[1] = None
        
        overflow_index = primary_index % 6
        overflow_list = self.title_overflow_table[overflow_index]
        for item in overflow_list:
            if item[0] == key:
                item[0] = None
                item[1] = None
            
        return None

    def write_txt_by_title(self):
        for key in self.title_key_list:
            primary_index = self.primary_hash_function(key)
            primary_list = self.title_primary_table[primary_index]
            for item in primary_list:
                if item[0] == key:
                    with open ("TitleKeyDB.txt", "a") as data:
                        data.write(f"{item[0]}: {item[1]}\n")
            
            overflow_index = primary_index % 6
            overflow_list = self.title_overflow_table[overflow_index]
            for item in overflow_list:
                if item[0] == key:
                    with open ("TitleKeyDB.txt", "a") as data:
                        data.write(f"{item[0]}: {item[1]}\n")
            
        return None
    
    def write_table_by_title(self):

        with open ("TitleKeyDB.txt", "r") as data:
            for line in data:
                info = line.strip().split(":")
                key = info[0]
                value = info[1]
                
                value_split = info[1].strip().split(",")
                
                model = value_split[0].strip("[' '")
                title = value_split[1].strip("' '")
                price = value_split[2].strip("' '")
                status = value_split[3].strip("' ']")

                self.insert_by_title(key, model, title, price, status)
        return None

    def empty_txt_by_title(self):
        with open("TitleKeyDB.txt", "w+") as data:
            datos = data.readlines()
            data.writelines(datos)
            data.close()
        return











    # def __init__(self):
    #     self.primary_table = [[],[],[]]
    #     self.overflow_table = [[],[],[],[],[],[]]

    # def hash_function(self, key):
    #     return hash(key) % 3
    
    # def insert(self, key, model, title, price, status):
    #     index = self.hash_function(key)
    #     if len(self.primary_table[index]) < 3:
    #         self.primary_table[index].append([model, title, price, status])
    #     else:
    #         index = (index + 1) % 6
    #         while len(self.overflow_table[index]) >= 3:
    #             index = (index + 1) % 6
    #             self.overflow_table[index].append([model, title, price, status])

    # def search(self, key):
    #     try:
    #         index = self.hash_function(key)
    #         # if self.primary_table[index] is None:
    #         #     if self.overflow_table[index] is None:
    #         #         print("No hay elementos con ese valor")
    #         #     else:
    #         #         # for item in self.overflow_table[index]:
    #         #         #     if item[0] == key:
    #         #         #         list = [item[1], item[2], item[3], item[4]]
    #         #         #         return list
    #         #         result = self.overflow_table[index]
    #         #         return result
    #         # else:
    #         #     # for item in self.primary_table[index]:
    #         #     #         if item[0] == key:
    #         #     #             list = [item[1], item[2], item[3], item[4]]
    #         #     #             return list
    #         #     result = self.overflow_table[index]
    #         #     return result
    #         return self.overflow_table[index]

    #     except KeyError:
    #         raise KeyError(key)
    












    
    # def __init__(self, tamano):
    #     self.tamano = tamano
    #     self.tabla = [[] for _ in range(3)]
        
    # def clave_primaria(self, clave):
    #     return hash(clave) % self.tamano
    
    # def agregar(self, clave, model, title, price, status):
    #     list = [model, title, price, status]
    #     indice = self.clave_primaria(clave)
    #     for par in self.tabla[indice]:
    #         if par[0] == clave:
    #             par[1] = model
    #             par[2] = title
    #             par[3] = price
    #             par[4] = status
    #             return
    #     self.tabla[indice].append([clave, model, title, price, status])
        
    # def obtener(self, clave):
    #     try:
    #         indice = self.clave_primaria(clave)
    #         if self.tabla[indice] is None:
    #             print("No hay elementos con ese valor")
    #         else:
    #             for par in self.tabla[indice]:
    #                 if par[0] == clave:
    #                     list = [par[1], par[2], par[3], par[4]]
    #                     return list
    #     except KeyError:
    #         raise KeyError(clave)
        
    # def eliminar(self, clave):
    #     indice = self.clave_primaria(clave)
    #     if self.tabla[indice] is None:
    #         print("No hay elementos con ese valor")
    #     else:
    #         print("Elemento con valor", clave, "eliminado")
    #         self.tabla[indice] = None



    


    # def clave_secundaria(self, clave):
    #     return hash(clave) % self.tamano
    
    # def agregar2(self, clave, model, title, price, status):
    #     list = [model, title, price, status]
    #     indice = self.clave_secundaria(clave)
    #     for par in self.tabla[indice]:
    #         if par[0] == clave:
    #             par[1] = model
    #             par[2] = title
    #             par[3] = price
    #             par[4] = status
    #             return
    #     self.tabla[indice].append([clave, model, title, price, status])
        
    # def obtener2(self, clave):
    #     try:
    #         indice = self.clave_secundaria(clave)
    #         if self.tabla[indice] is None:
    #             print("No hay elementos con ese valor")
    #         else:
    #             for par in self.tabla[indice]:
    #                 if par[0] == clave:
    #                     list = [par[1], par[2], par[3], par[4]]
    #                     return list
    #     except KeyError:
    #         raise KeyError(clave)
    
    # def eliminar2(self, clave):
    #     indice = self.clave_secundaria(clave)
    #     if self.tabla[indice] is None:
    #         print("No hay elementos con ese valor")
    #     else:
    #         print("Elemento con valor", clave, "eliminado")
    #         self.tabla[indice] = None
    
    



    # def recorrer(self):
    #     for clave in self.tabla:
    #         with open ("BaseDeDatos.txt", "a+") as data:
    #             data.write(f"{clave}\n")
