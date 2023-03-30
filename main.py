import sys
from HashTable import TablaHash

global hash
hash = TablaHash()

def validateNumber(number):
    if number.isnumeric():
        if int(number) > 0 and int(number) < 1000:
            return True
        else:
            return False
    else:
        return False

def new_game():
    model = input("\nIngrese el modelo del juego: ")
    model = model.upper()
    digits = 0

    for char in model:
        if char.isdigit():
            digits += 1
        else:
            pass
    while len(model) != 8 or digits != 2:
        print("¡Ingreso invalido! Debe contener 6 letras y 2 números")
        model = input("Ingrese el modelo del juego: ")
        model = model.upper()
        digits = 0

        for char in model:
            if char.isdigit():
                digits += 1
            else:
                pass


    result = hash.search_by_model(model)

    while result != None:
        print("\n¡Modelo invalido! El modelo que ingresó ya se encuentra registrado.")
        model = input("\nIngrese el modelo del juego: ")
        model = model.upper()
        result = hash.search_by_model(model)
    

    title = input("Ingrese el título del juego: ")
    title = title.upper()

    while len(title) > 10 or len(title) == 0:
        print("¡Ingreso invalido! Debe tener máximo 10 caracteres")
        title = input("Ingrese el título del juego: ")
        title = title.upper()

    result = hash.search_by_title(title)

    while result != None:
        print("\n¡Título invalido! El título que ingresó ya se encuentra registrado.")
        title = input("\nIngrese el título del juego: ")
        title = title.upper()
        result = hash.search_by_title(title)

    price = input("Ingrese el precio del juego: ")

    validado = validateNumber(price)

    while not validado:
        print("¡Ingreso invalido! Debe ingresar solo números y menores a los 1000 Bs")
        price = input("Ingrese el precio del juego: ")
        validado = validateNumber(price)

    # if price.isnumeric():
    #     price = int(price)
    #     while price > 1000:
    #         print("¡Ingreso invalido! El precio debe ser menor a los 1000 Bs")
    #         price = input("Ingrese el precio del juego: ")
    #         if price.isnumeric():
    #             price = int(price)
    #         else:
    #             while not price.isnumeric():
    #                 print("¡Ingreso invalido! Debe ingresar solo números")
    #                 price = input("Ingrese el precio del juego: ")
    #                 if price.isnumeric():
    #                     price = int(price)
    #                     break
    # else:
    #     while not price.isnumeric():
    #         print("¡Ingreso invalido! Debe ingresar solo números")
    #         price = input("Ingrese el precio del juego: ")
    #         if price.isnumeric():
    #             price = int(price)
    #             break
            

    price = int(price)

    status = "STOCK"

    hash.insert(model, title, model, title, price, status)

    return

def search_game_by_model():
    model = input("\nIngrese el modelo del juego que desea buscar: ")
    model = model.upper()
    result = hash.search_by_model(model)

    while result == None:
        print("\n¡Modelo invalido! Por favor ingrese un modelo válido.")
        model = input("\nIngrese el modelo del juego que desea buscar: ")
        model = model.upper()
        result = hash.search_by_model(model)

    print("\n",result)
    return

def search_game_by_title():
    title = input("Ingrese el título del juego que desea buscar: ")
    title = title.upper()
    result = hash.search_by_title(title)

    while result == None:
        print("\n¡Título invalido! Por favor ingrese un título válido.")
        title = input("\nIngrese el título del juego que desea buscar: ")
        title = title.upper()
        result = hash.search_by_title(title)

    print("\n",result)
    return

def validar_numero_opcion(opcion):
    if opcion.isnumeric():
        if int(opcion) > 0 and int(opcion) < 3:
            return True
        else:
            return False
    else:
        return False

def rent_game():

    result = []

    print("\n¿Desea buscar por modelo o por título?")
    print("1. Modelo\n2. Título")
    option = input("-> ")

    validacion = validar_numero_opcion(option)
    while not validacion:
        print("¡Ingreso invalido! Por favor ingrese una opción de la lista.")
        option = input("-> ")
        validacion = validar_numero_opcion(option)

    # while not option.isnumeric():
    #     print("¡Ingreso invalido! Por favor ingrese una opción de la lista.")
    #     option = input("-> ")

    option = int(option)

    if option == 1:
        model = input("\nIngrese el modelo del juego que desea alquilar: ")
        model =  model.upper()
        aux = hash.search_by_model(model)

        while aux == None:
            print("\n¡Modelo invalido! Por favor ingrese un modelo válido.")
            model = input("\nIngrese el modelo del juego que desea alquilar: ")
            model =  model.upper()
            aux = hash.search_by_model(model)

        for x in hash.search_by_model(model):
            result.append(x)

        if result[-1] == "ALQUILADO":
            print("\nEl juego no se encuentra disponible en estos momentos")
        else:
            result[-1] = "ALQUILADO"
            print("\nSe ha alquilado exitosamente el juego")

        hash.modify_by_model(model, result[0], result[1], result[2], result[3])

    elif option == 2:

        title = input("\nIngrese el título del juego que desea alquilar: ")
        title = title.upper()
        aux = hash.search_by_title(title)

        while aux == None:
            print("\n¡Título invalido! Por favor ingrese un título válido.")
            title = input("\nIngrese el título del juego que desea alquilar: ")
            title = title.upper()
            aux = hash.search_by_title(title)

        for x in hash.search_by_title(title):
            result.append(x)

        if result[-1] == "ALQUILADO":
            print("\nEl juego no se encuentra disponible en estos momentos")
        else:
            result[-1] = "ALQUILADO"
            print("\nSe ha alquilado exitosamente el juego")

        hash.modify_by_title(title, result[0], result[1], result[2], result[3])

    return

def return_game():

    result = []

    print("\n¿Desea buscar por modelo o por título?")
    print("1. Modelo\n2. Título")
    option = input("-> ")

    while not option.isnumeric():
        print("¡Ingreso invalido! Por favor ingrese una opción de la lista.")
        option = input("-> ")

    option = int(option)

    if option == 1:
        model = input("\nIngrese el modelo del juego que desea devolver: ")
        model =  model.upper()
        aux = hash.search_by_model(model)

        while aux == None:
            print("\n¡Modelo invalido! Por favor ingrese un modelo válido.")
            model = input("\nIngrese el modelo del juego que desea devolver: ")
            model =  model.upper()
            aux = hash.search_by_model(model)

        for x in hash.search_by_model(model):
            result.append(x)
        
        if result[-1] == "STOCK":
            print("\nEl juego ya ha sido devuelto anteriormente")
        else:
            result[-1] = "STOCK"
            print("\nSe ha devuelto exitosamente el juego")

        hash.modify_by_model(model, result[0], result[1], result[2], result[3])

    elif option == 2:

        title = input("\nIngrese el título del juego que desea devolver: ")
        title = title.upper()
        aux = hash.search_by_title(title)

        while aux == None:
            print("\n¡Título invalido! Por favor ingrese un título válido.")
            title = input("\nIngrese el título del juego que desea devolver: ")
            title = title.upper()
            aux = hash.search_by_title(title)

        for x in hash.search_by_title(title):
            result.append(x)

        if result[-1] == "STOCK":
            print("\nEl juego ya ha sido devuelto anteriormente")
        else:
            result[-1] = "STOCK"
            print("\nSe ha devuelto exitosamente el juego")

        hash.modify_by_title(title, result[0], result[1], result[2], result[3])

    return

def delete_game():
    model = ""
    title = ""

    result = []

    print("\n¿Desea buscar por modelo o por título?")
    print("1. Modelo\n2. Título")
    option = input("-> ")

    while not option.isnumeric():
        print("¡Ingreso invalido! Por favor ingrese una opción de la lista.")
        option = input("-> ")

    option = int(option)

    if option == 1:
        model = input("\nIngrese el modelo del juego que desea alquilar: ")
        model =  model.upper()
        aux = hash.search_by_model(model)

        while aux == None:
            print("\n¡Modelo invalido! Por favor ingrese un modelo válido.")
            model = input("\nIngrese el modelo del juego que desea alquilar: ")
            model =  model.upper()
            aux = hash.search_by_model(model)

        for x in hash.search_by_model(model):
            result.append(x)

        hash.delete_by_model(model)

    elif option == 2:

        title = input("\nIngrese el título del juego que desea alquilar: ")
        title = title.upper()
        aux = hash.search_by_title(title)

        while aux == None:
            print("\n¡Título invalido! Por favor ingrese un título válido.")
            title = input("\nIngrese el título del juego que desea alquilar: ")
            title = title.upper()
            aux = hash.search_by_title(title)

        for x in hash.search_by_title(title):
            result.append(x)
        
        hash.delete_by_title(title)

    print("\nSe ha eliminado exitosamente el juego")

    return

def main():
    hash.write_table()

    print("\nBIENVENIDO A RENT A GAME CARACAS\n")
    
    while True:
        print("\nEscoja una opción:\n")
        print("1. Ingresar un nuevo juego a la base de datos\n2. Buscar un juego por modelo\n3. Buscar un juego por título\n4. Alquilar un juego\n5. Devolver un juego\n6. Eliminar un juego de la base de datos\n7. Salir del programa")
        option = input("-> ")

        while not option.isnumeric():
            print("¡Ingreso invalido! Por favor ingrese una opción de la lista.")
            option = input("-> ")

        option = int(option)

        if option == 1:
            new_game()
        elif option == 2:
            search_game_by_model()
        elif option == 3:
            search_game_by_title()
        elif option == 4:
            rent_game()
        elif option == 5:
            return_game()
        elif option == 6:
            delete_game()
        elif option == 7:
            hash.empty_txt()
            hash.write_txt()
            sys.exit()
            False    
    
main()