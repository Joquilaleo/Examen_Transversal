import funciones as fnc 
def main():
    productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
    }

    stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
    }

    while True:
        fnc.leer_opcion()
        opcion = fnc.elegir_opcion()
        if opcion == 1: #buscar categoria
            buscar = input("Ingrese la categoria que busca:")
            categorias = fnc.unidades_categoria(buscar,productos,stock)
        elif opcion == 2: #buscar productos por precio
            try:
                precio_minimo = int(input("Ingrese el precio minimo de busqueda"))
                precio_maximo = int(input("Ingrese el precio maximo de busqueda"))
            except ValueError:
                print("Error al ingresar datos")
            
        elif opcion == 3: #Actualizar precios de productos
            print("")

        elif opcion == 4: # agregar producto
            print("=====Agregar Producto=====")
            fnc.agregar_producto(productos,stock)
        elif opcion == 5: # eliminar producto
            print("")
        
        elif opcion == 6: # salir
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()

