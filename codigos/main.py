import recepcion_datos

def menu():
    print("======================================================")
    print("\t\tAcceso de usuario")
    print("======================================================")
    print("\t1.- Registrarse.")
    print("\t2.- Validar usuario.")
    print("\t3.- Salir.")

def repetir_menu():
    while True:
        menu()
        opcion = input("Ingrese opcion: ")
        if opcion == "1":
            recepcion_datos.guardando_datos()
        elif opcion == "2":
            recepcion_datos.validando_datos()
        elif opcion == "3":
            print("Gracias por usar el sistema de login.")
            break
        else:
            print("Pulsa una opcion correcta.")

def main():
    repetir_menu()


if __name__ == "__main__":
    main()
