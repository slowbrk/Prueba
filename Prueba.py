import json

with open ("biblioteca.json", "r") as archivo:
    dat = json.load(archivo)

    while True:
        print("*********************")
        print("*    MUNDO LIBRO    *")
        print("*********************")
        print()
        print()
        print("[1] - Mantenedor de libros")
        print("[2] - Reportes")
        print("[3] - Salir")
        print()
        opcion1 = int(input("Ingrese una opcion: ")) 
        if opcion1 == 1:
            print("****************************")
            print("*     MANTENEDOR LIBRO     *")
            print("****************************")
            print()
            print("[1] - Agregar libro")
            print("[2] - Editar libro")
            print("[3] - Eliminar libro")
            print("[4] - Buscar libro")
            print("[5] - Volver")
        elif opcion1 == 2:
            print()


        elif opcion1 == 3:
            print("Saliendo...")
            break    
            




    





    


