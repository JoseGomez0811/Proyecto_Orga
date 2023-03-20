def hash_function():
    return 

def load_matrix(id, model, title, price, status):
    return

def new_game():
    model = input("Ingrese el modelo del juego: ")
    digits = 0

    for char in model:
        if char.isdigit():
            digits += 1
        else:
            pass
    while len(model) != 8 or digits != 2:
        print("¡Ingreso invalido! Debe contener 6 letras y 2 números")
        model = input("Ingrese el modelo del juego: ")

        for char in model:
            if char.isdigit():
                digits += 1
            else:
                pass

    title = input("Ingrese el título del juego: ")

    while len(title) > 10:
        print("¡Ingreso invalido! Debe tener máximo 10 caracteres")
        title = input("Ingrese el título del juego: ")

    price = input("Ingrese el precio del juego: ")

    while not price.isnumeric():
        print("¡Ingreso invalido! Debe ingresar solo números")
        price = input("Ingrese el precio del juego: ")
    
    price = int(price)

    while price > 1000:
        print("¡Ingreso invalido! El precio debe ser menor a los 1000 Bs")
        price = input("Ingrese el precio del juego: ")


    status = "STOCK"
    # status = status.capitalize()

    # if status != "STOCK" or status != "ALQUILADO":
    #     print("¡Ingreso invalido! Debe indicar si el juego está en STOCK o ALQUILADO")
    #     status = input("Ingrese el estado del juego (STOCK / ALQUILADO): ")


    id = load_matrix()

    load_matrix(id, model, title, price, status)

    #Guardar los datos en un archivo txt
    # with open ("BaseDeDatos.txt", "a+") as data:
    #     data.write(f"{model} - {title} - {price} - {status}\n")

    return

def search_game_model():
    return

def search_game_by_title():
    return

def rent_game():

    status = "ALQUILADO"

    return

def return_game():
    return

def delete_game():

    status = "STOCK"

    return

def main():
    new_game()
main()