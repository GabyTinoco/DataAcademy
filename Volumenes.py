def prisma_triangular() :
    base = input("Introduzca la base:")
    altura = input("Introduzca la altura:")
    lateral1  = input("Introduzca la longitud del lateral 1")
    lateral2 = input("Introduzaca la longitud del lateral 2")
    piso  = input("Introduzaca la longitud del piso")
    altura  = input("Introduzaca la altura del prisma")
    
    area_base = (float(base) * float(altura))/2
    area_lateral = float(lateral1) * float(lateral2)
    area_piso = area_lateral * float(piso)
    area_total = area_base + area_lateral + area_piso

    volumen = area_total * altura

    print("El volumen del prisma es:" + str(volumen))
   
def cubo() :
    longitud = input("Introduzca la longitud del cilindro")
    volumen = pow(float(longitud), 3)
    print("El volumen del cubo es:  " + str(volumen))
 
def cilindro() : 
    menu_cilindro = """
        ¿Cómo desea calcular el volumen del cilindro?
        1. Con la formula de πR2h
         2. Con la formula de Abh 
     """
    print(menu_cilindro)
    opcion_cilindro = input("Introduce el número de la opción del menu:")
    opcion_cilindro = int(opcion_cilindro)

    if(opcion_cilindro == 1) :
        volumen_cilindro_formula1()
    elif(opcion_cilindro == 2) :
        volumen_cilindro_formular2()
    else:
        print("Elija una opción valida")


def volumen_cilindro_formula1 () :
    altura = input("Introduzca la altura del cilindro")
    radio =  input("Introduzca el radio del cilindro")
    volumen = float(altura) * 3.1416 * pow(float(radio), 2)
    print("El volumen del cilindro es:  " + str(volumen) + " centimetros cúbicos" )

def volumen_cilindro_formular2 () :
    # s el área de la base B por la altura h .
    radio =  input("Introduzca el radio del cilindro")
    altura =  input("Introduzca la altura del cilindro")
    area_base =  3.1416 * pow(float(radio), 2)
    volumen = area_base * altura    
    print("El volumen del cilindro es : " + str(volumen) + " centimetros cúbicos")


def run(): 
    menu = """
            Bienvenido a tu conversor de volumen
            Elije la figura geométrica
             1. Cilindro
             2. Cubo
             3. Prisma triangular
            """
    print(menu)
    opcion = input("Introduce el número de la opción del menu:")
    opcion = int(opcion)

    if(opcion == 1) :
        cilindro()               
    elif(opcion == 2) :
        cubo()
    elif(opcion == 3) :
        prisma_triangular()
    else:
        print("Ingrese una opción valida")

if __name__ == '__main__':
    run();