def millasKilometros () :
    millas = input("Introduzca la cantidad de millas que desea convertir")    
    millas = float(millas)
    km = millas * 1.609344
    print("La cantidad de millas que ingresaste equivalen a:" + str(km) + "kilometros" )


def kilometrosMillas () :
    kilometros = input("Introduzca la cantidad de kilometros que desea convertir")    
    kilometros = float(kilometros)
    millas = kilometros * 0.6214
    print("La cantidad de kilometros que ingresaste equivalen a:" + str(millas) + "kilometros" )


def run(): 
    menu = """
            Bienvenido a tu conversor de millas a kilometros
             y kilomentros a millas.
            ¿Qué deseas convertir?
             1. Millas a kilometros
             2. Kilometros a millas
            """
    print(menu)
    opcion = input("Introduce el número de la opción del menu:")
    opcion = int(opcion)

    if(opcion == 1) :
        millasKilometros()
    elif(opcion == 2) :
        kilometrosMillas()
    else:
        print("Ingrese una opción valida")

if __name__ == '__main__':
    run();