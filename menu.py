def muestraMenu():
    __op = 0
    while True:
        print("----------Eliga una opcion----------\n")
        print("1. Dar alta a paciente\n")
        print("2. Ingrese un diagnostico para consultar los pacientes\n")
        print("3. Salir")
        __op = input("Ingrese su opcion: ")
        if __op in ("1", "2", "3"):
            return __op
        input("No se ha ingresado ninguna opcion correcta.\n""Pulsa ENTER para continuar\n")
