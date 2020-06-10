print("Hacer llamada desde mi casa")
opcion = input("Contestan llamada? [S/N] ")
if opcion.upper() == "S":
    opcion = input("Preguntar ¿Quisiera compartid una merienda conmigo? [S/N] ")
    if opcion.upper() == "S":
        print("Cenar juntos")
        print("Empezar una amistad")
    elif opcion.upper() == "N":
        opcion = input("Preguntar ¿Disfrutarias de una bebida caliente? [S/N] ")
        if opcion.upper() == "S":
            print("Seleccionar el tipo de bebida que tomaran")
            bebida = input("Te, cafe o cocoa: ")
            if opcion.lower() == "te":
                print("Tomar té")
                print("Iniciar una amistad")
            elif opcion.lower() == "cocoa":
                print("Tomar té")
                print("Iniciar una amistad")
            elif opcion.lower() == "cafe":
                print("Tomar cafe")
                print("Iniciar una amistad")
        elif opcion.upper() == "N":
            print("Rebatir")
            opcion = input("Alguna actividad recreacional? (dile uno de tus intereses) [S/N] ")
            if opcion.upper() == "S":
                print("Comparto un mismo interes")
                print("Preguntar ¿Porque no compartir eso juntos?")
            elif opcion.upper() == "N":
                print("Rebatir")
                print("Volver a preguntar por una acccion menos objetable")
elif opcion.upper() == "N":
    print("Dejar un mensaje")
    print("Esperar que devuelva a llamar")

