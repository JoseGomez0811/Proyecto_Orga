class TablaHash:
    def __init__(self):
        self.key_list = []

        self.primary_table = [[], [], []]
        self.overflow_table = [[], [], [], [], [], []]
    
    def hash_function(self, key):
        return hash(key) % 3
    
    def insert(self, key1, key2, model, title, price, status):
        try:
            index = self.hash_function(key1)
            if len(self.primary_table[index]) < 3:
                self.primary_table[index].append([key1, key2, [model, title, price, status]])
                self.key_list.append(key1)
                # print("Primario")
            else:
                overflow_index = index % 6
                if len(self.overflow_table[overflow_index]) < 3:
                    self.overflow_table[overflow_index].append([key1, key2, [model, title, price, status]])
                    self.key_list.append(key1)
                    # print("Overflow")
                # else:
                #     raise ValueError("No hay espacio en la tabla de hash")
        except ValueError:
            print("No hay espacio en la tabla de hash")

    def search_by_model(self, key):
        index = self.hash_function(key)
        for item in self.primary_table[index]:
            if item[0] == key:
                value = item[2]
                return value
        
        overflow_index = index % 6
        for item in self.overflow_table[overflow_index]:
            if item[0] == key:
                value = item[2]
                return value
                        
        return None
    
    def search_by_title(self, key):
        for items in self.primary_table:
            for item in items:
                if item[1] == key:
                    value = item[2]
                    return value
        
        for items in self.overflow_table:
            for item in items:
                if item[1] == key:
                    value = item[2]
                    return value
            
        return None
    
    def modify_by_model(self, key, model, title, price, status):
        index = self.hash_function(key)
        for item in self.primary_table[index]:
            if item[0] == key:
                item[2] = [model, title, price, status]
        
        overflow_index = index % 6
        for item in self.overflow_table[overflow_index]:
            if item[0] == key:
                item[2] = [model, title, price, status]
            
        return None
    
    def modify_by_title(self, key, model, title, price, status):
        for items in self.primary_table:
            for item in items:
                if item[1] == key:
                    item[2] = [model, title, price, status]
        
        for items in self.overflow_table:
            for item in items:
                if item[1] == key:
                    item[2] = [model, title, price, status]
            
        return None

    def delete_by_model(self, key):
        index = self.hash_function(key)
        for item in self.primary_table[index]:
            if item[0] == key:
                item[0] = None
                item[1] = None
                item[2] = None
        
        overflow_index = index % 6
        for item in self.overflow_table[overflow_index]:
            if item[0] == key:
                item[0] = None
                item[1] = None
                item[2] = None
            
        return None
    
    def delete_by_title(self, key):
        for items in self.primary_table:
            for item in items:
                if item[1] == key:
                    item[0] = None
                    item[1] = None
                    item[2] = None

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
            for item in self.primary_table[index]:
                if item[0] == key:
                    with open ("DataBase.txt", "a") as data:
                        data.write(f"{item[0]}, {item[1]}, {item[2]}\n")
            
            overflow_index = index % 6
            for item in self.overflow_table[overflow_index]:
                if item[0] == key:
                    with open ("DataBase.txt", "a") as data:
                        data.write(f"{item[0]},{item[1]},{item[2]}\n")
            
        return None
    
    def write_table(self):

        with open ("DataBase.txt", "r") as data:
            for line in data:
                info = line.strip().split(",")
                key1 = info[0].strip()
                key2 = info[1].strip()
                model = info[2].strip("[' '")
                title = info[3].strip("' '")
                price = info[4].strip("' '")
                status = info[5].strip("' ']")

                self.insert(key1, key2, model, title, price, status)

            data.close()

        return None

    def empty_txt(self):
        with open("DataBase.txt", "w+") as data:
            datos = data.readlines()
            data.writelines(datos)
            data.close()
        return
  