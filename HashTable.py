class TablaHash:
    def __init__(self):
        # self.model_primary_table = [[] for _ in range(3)]
        # self.model_overflow_table = [[] for _ in range (6)]
        # self.title_primary_table = [[] for _ in range(3)]
        # self.title_overflow_table = [[] for _ in range (6)]

        # self.model_primary_table = [[], [], []]
        # self.model_overflow_table = [[], [], [], [], [], []]
        # self.title_primary_table = [[], [], []]
        # self.title_overflow_table = [[], [], [], [], [], []]

        self.key_list = []
        # self.title_key_list = []

        self.primary_table = [[], [], []]
        self.overflow_table = [[], [], [], [], [], []]

        # self.primary_group = 3
        # self.primary_group_size = 3
        # self.overflow_group = 6
        # self.overflow_group_size = 3
        # self.table = [[] for _ in range(self.primary_group + self. overflow_group)]
    
    def hash_function(self, key):
        return hash(key) % 3
    
    def insert(self, key1, key2, model, title, price, status):
        try:
            index = self.hash_function(key1)
            # primary_list = self.primary_table[index]
            if len(self.primary_table[index]) < 3:
                self.primary_table[index].append([key1, key2, [model, title, price, status]])
                self.key_list.append(key1)
                # self.title_key_list.append(key2)
                print("Primario")
            else:
                overflow_index = index % 6
                # overflow_list = self.overflow_table[overflow_index]
                if len(self.overflow_table[overflow_index]) < 3:
                    self.overflow_table[overflow_index].append([key1, key2, [model, title, price, status]])
                    self.key_list.append(key1)
                    # self.title_key_list.append(key2)
                    print("Overflow")
                # else:
                #     raise ValueError("No hay espacio en la tabla de hash")
        except ValueError:
            print("No hay espacio en la tabla de hash")

    def search_by_model(self, key):
        index = self.hash_function(key)
        # primary_list = self.primary_table[index]
        for item in self.primary_table[index]:
            if item[0] == key:
                value = item[2]
                return value
        
        overflow_index = index % 6
        # overflow_list = self.overflow_table[overflow_index]
        for item in self.overflow_table[overflow_index]:
            if item[0] == key:
                value = item[2]
                return value
            
        return None
    
    def search_by_title(self, key):
        # index = self.hash_function(key)
        # primary_list = self.primary_table[index]
        for items in self.primary_table:
            for item in items:
                if item[1] == key:
                    value = item[2]
                    return value
        
        # overflow_index = index % 6
        # overflow_list = self.overflow_table[overflow_index]
        for items in self.overflow_table:
            for item in items:
                if item[1] == key:
                    value = item[2]
                    return value
            
        return None
    
    def modify_by_model(self, key, model, title, price, status):
        index = self.hash_function(key)
        # primary_list = self.primary_table[index]
        for item in self.primary_table[index]:
            if item[0] == key:
                item[2] = [model, title, price, status]
        
        overflow_index = index % 6
        # overflow_list = self.overflow_table[overflow_index]
        for item in self.overflow_table[overflow_index]:
            if item[0] == key:
                item[2] = [model, title, price, status]
            
        return None
    
    def modify_by_title(self, key, model, title, price, status):
        # index = self.hash_function(key)
        # primary_list = self.primary_table[index]
        for items in self.primary_table:
            for item in items:
                if item[1] == key:
                    item[2] = [model, title, price, status]
        
        # overflow_index = index % 6
        # overflow_list = self.overflow_table[overflow_index]
        for items in self.overflow_table:
            for item in items:
                if item[1] == key:
                    item[2] = [model, title, price, status]
            
        return None

    def delete_by_model(self, key):
        index = self.hash_function(key)
        # primary_list = self.primary_table[index]
        for item in self.primary_table[index]:
            if item[0] == key:
                item[0] = None
                item[1] = None
                item[2] = None
        
        overflow_index = index % 6
        # overflow_list = self.overflow_table[overflow_index]
        for item in self.overflow_table[overflow_index]:
            if item[0] == key:
                item[0] = None
                item[1] = None
                item[2] = None
            
        return None
    
    def delete_by_title(self, key):
        # index = self.hash_function(key)
        # primary_list = self.primary_table[index]
        for items in self.primary_table:
            for item in items:
                if item[1] == key:
                    item[0] = None
                    item[1] = None
                    item[2] = None
        
        # overflow_index = index % 6
        # overflow_list = self.overflow_table[overflow_index]
        for items in self.overflow_table:
            for item in items:
                if item[1] == key:
                    item[0] = None
                    item[1] = None
                    item[2] = None
            
        return None
    
    def write_txt(self):
        for key in self.key_list:
            index = self.hash_function(key)
            # primary_list = self.primary_table
            for item in self.primary_table[index]:
                if item[0] == key:
                    with open ("DataBase.txt", "a") as data:
                        data.write(f"{item[0]}, {item[1]}, {item[2]}\n")
            
            # data.close()
            
            overflow_index = index % 6
            # overflow_list = self.overflow_table[overflow_index]
            for item in self.overflow_table[overflow_index]:
                if item[0] == key:
                    with open ("DataBase.txt", "a") as data:
                        data.write(f"{item[0]},{item[1]},{item[2]}\n")
            
            # data.close()
            
        return None
    
    def write_table(self):

        with open ("DataBase.txt", "r") as data:
            for line in data:
                info = line.strip().split(",")
                key1 = info[0].strip()
                key2 = info[1].strip()
                # value = info[2:]
                model = info[2].strip("[' '")
                title = info[3].strip("' '")
                price = info[4].strip("' '")
                status = info[5].strip("' ']")
                
                # value_split = info[2:].strip().split(",")

                # print(key1)
                # print(key2)
                # print(value)
                
                # model = value_split[0].strip("[' '")
                # title = value_split[1].strip("' '")
                # price = value_split[2].strip("' '")
                # status = value_split[3].strip("' ']")

                # print(key1)
                # print(key2)
                # print(model)
                # print(title)
                # print(price)
                # print(status)

                self.insert(key1, key2, model, title, price, status)

            data.close()

        return None

    def empty_txt(self):
        with open("DataBase.txt", "w+") as data:
            datos = data.readlines()
            data.writelines(datos)
            data.close()
        return
        

    # def insert_by_model(self, key1, key2, model, title, price, status):
    #     try:
    #         index = self.primary_hash_function(key1)
    #         if len(self.model_primary_table) < 3:
    #             self.model_primary_table[index].append([key1, key2, [model, title, price, status]])         
                
    #         else:
    #             overflow_index = index % 6
    #             if len(self.model_overflow_table) < 3:
    #                 self.model_overflow_table[overflow_index].append([key1, key2, [model, title, price, status]])         

    #     except ValueError:
    #         return "No hay epacio"
    

    # def search_by_model(self, key):
    #     index = self.primary_hash_function(key) 
    #     for item in self.model_primary_table[index]:
    #         if item[0] == key:
    #             print(item[2])

    # def insert_by_model(self, model, title, price, status):
    #     try:
    #         primary_index = self.secundary_hash_function(model)
    #         secundary_index = self.primary_hash_function(title)
    #         primary_list = self.model_primary_table[primary_index]
    #         value_list = self.model_primary_table[secundary_index]
    #         if len(primary_list) < 3:
    #             value_list.append([model, title, price, status])
    #             primary_list.append([model, value_list[0:3]])
    #             # self.title_key_list.append(model)
    #             print("Primario")
    #         else:
    #             overflow_index = primary_index % 6
    #             secundary_overflow_index = secundary_index % 6
    #             overflow_list = self.model_overflow_table[overflow_index]
    #             overflow_value_list = self.model_overflow_table[secundary_overflow_index]
    #             if len(overflow_list) < 3:
    #                 overflow_value_list.append([model, title, price, status])
    #                 overflow_list.append(overflow_value_list)
    #                 # self.title_key_list.append(model)
    #                 print("Overflow")
    #     except ValueError:
    #         print("No hay espacio en la tabla de hash")

    # def insert_by_model(self, model, title, price, status):
    #     try:
    #         primary_index = self.primary_hash_function(model)
    #         secundary_index = self.primary_hash_function(title)
    #         primary_list = self.model_primary_table[primary_index]
    #         value_list = self.model_primary_table[secundary_index]
    #         if len(primary_list) < 3:
    #             primary_list.append([model, [model, title, price, status]])
    #             for item in primary_list:
    #                 if item[0] == model:
    #                     value_list.append(item[1])
    #                     item[1] = value_list
                
    #             self.model_key_list.append(model)
    #             print("Primario")
    #         else:
    #             overflow_index = primary_index % 6
    #             secundary_overflow_index = secundary_index % 6
    #             overflow_list = self.model_overflow_table[overflow_index]
    #             overflow_value_list = self.model_overflow_table[secundary_overflow_index]
    #             if len(overflow_list) < 3:
    #                 overflow_list.append([model, [model, title, price, status]])
    #                 for item in overflow_list:
    #                     if item[0] == model:
    #                         overflow_value_list.append(item[1])
    #                         item[1] = overflow_value_list
                    
    #                 self.model_key_list.append(model)
    #                 print("Overflow")
    #     except ValueError:
    #         print("No hay espacio en la tabla de hash")





    # def search_by_model(self, key):
    #     primary_index = self.primary_hash_function(key)
    #     primary_list = self.model_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[0] == key:
    #             return item[2]
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.model_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[0] == key:
    #             return item[2]
            
    #     return None








    
    # def search_by_title(self, key):
    #     primary_index = self.primary_hash_function(key)
    #     primary_list = self.model_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[1] == key:
    #             return item[2]
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.model_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[1] == key:
    #             return item[2]
            
    #     return None
    
    # def modify_by_model(self, model, status):

    #     list = []
    #     result = []

    #     primary_index = self.primary_hash_function(model)
    #     primary_list = self.model_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[0] == model:
    #             for x in item[1]:
    #                 list.append(x)
    #             for y in list[0]:
    #                 result.append(y)
    #             result[3] = status
    #             item[1] = [result[0], result[1], result[2], result[3]]
    #             secundary_index = self.primary_hash_function(result[1])
    #             value_list = self.model_primary_table[secundary_index]
    #             value_list.clear()
    #             value_list.append(item[1])
    #             item[1] = value_list
    #             print(item[1])
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.model_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[0] == model:
    #             for x in item[1]:
    #                 list.append(x)
    #             for y in list[0]:
    #                 result.append(y)
    #             result[3] = status
    #             item[1] = [result[0], result[1], result[2], result[3]]
    #             secundary_index = self.primary_hash_function(result[1])
    #             value_list = self.model_primary_table[secundary_index]
    #             value_list.clear()
    #             value_list.append(item[1])
    #             item[1] = value_list
    #             print(item[1])
            
    #     return None
    
    # def modify_by_title(self, title, status):

    #     list = []

    #     primary_index = self.primary_hash_function(title)
    #     primary_list = self.model_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[1] == title:
    #             for x in item[0:]:
    #                 list.append(x)
    #             list[3] = status
    #             item[1] = [list[0], list[1], list[2], list[3]]
    #             secundary_index = self.primary_hash_function(list[1])
    #             value_list = self.model_primary_table[secundary_index]
    #             value_list.clear()
    #             value_list.append(item[1])
    #             item[1] = value_list
    #             print(item[1])


    # def delete_by_model(self, key):
    #     primary_index = self.primary_hash_function(key)
    #     primary_list = self.model_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[0] == key:
    #             item[0] = ""
    #             item[1] = ""
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.model_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[0] == key:
    #             item[0] = ""
    #             item[1] = ""
            
    #     return None


    # def delete_by_title(self, key):
    #     primary_index = self.secundary_hash_function(key)
    #     primary_list = self.title_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[1] == key:
    #             item[1] = ""
    #             item[0:] = ""
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.title_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[1] == key:
    #             item[1] = ""
    #             item[0:] = ""
            
    #     return None



    
        
        # overflow_index = primary_index % 6
        # overflow_list = self.model_overflow_table[overflow_index]
        # for item in overflow_list:
        #     if item[0] == title:
        #         for x in item[1]:
        #             list.append(x)
        #         for y in list[0]:
        #             result.append(y)
        #         result[3] = status
        #         item[1] = [result[0], result[1], result[2], result[3]]
        #         secundary_index = self.primary_hash_function(result[1])
        #         value_list = self.model_primary_table[secundary_index]
        #         value_list.clear()
        #         value_list.append(item[1])
        #         item[1] = value_list
        #         print(item[1])
            
        # return None

            # primary_index = self.primary_hash_function(model)
            # secundary_index = self.primary_hash_function(title)
            # primary_list = self.model_primary_table[primary_index]
            # value_list = self.model_primary_table[secundary_index]
            # if len(primary_list) < 3:
            #     # value_list.append([title, [model, title, price, status]])
            #     primary_list.append([model, [model, title, price, status]])
            #     for item in primary_list:
            #         if item[0] == model:
            #             value_list.append(item[1])
            #             item[1] = value_list
                
            #     self.model_key_list.append(model)   
            #     print("Primario")
            # else:
            #     overflow_index = primary_index % 6
            #     overflow_list = self.model_overflow_table[overflow_index]
            #     if len(overflow_list) < 3:
            #         overflow_list.append([model, [model, title, price, status]])
            #         self.model_key_list.append(model)
            #         print("Overflow")








    

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
            
    # def search_by_title(self, key):
    #     primary_index = self.secundary_hash_function(key)
    #     primary_list = self.title_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[0] == key:
    #             return item[1]
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.title_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[0] == key:
    #             return item[1]
            
    #     return None
    
    # def modify_by_title(self, key, model, title, price, status):
    #     primary_index = self.secundary_hash_function(key)
    #     primary_list = self.title_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[0] == key:
    #             item[1] = [model, title, price, status]
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.title_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[0] == key:
    #             item[1] = [model, title, price, status]
            
    #     return None

    # def delete_by_title(self, key):
    #     primary_index = self.secundary_hash_function(key)
    #     primary_list = self.title_primary_table[primary_index]
    #     for item in primary_list:
    #         if item[0] == key:
    #             item[0] = None
    #             item[1] = None
        
    #     overflow_index = primary_index % 6
    #     overflow_list = self.title_overflow_table[overflow_index]
    #     for item in overflow_list:
    #         if item[0] == key:
    #             item[0] = None
    #             item[1] = None
            
    #     return None

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
