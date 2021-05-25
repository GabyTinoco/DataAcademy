def area(base, altura):
    area = (base * altura)/2;
    return area

def run():
    base = int(input('Ingresa la base del triangulo '))
    altura = int(input('Ingresa la altura del triangulo:'))
    lado_a = int(input('Ingresa el lado a del triangulo:'))
    lado_c = int(input('Ingresa el lado c del triangulo:'))
      
    area_triangulo = area(base, altura)

    if(lado_a == lado_c  and lado_a == base):
        print("El triangulo es un equilatero")
    elif(base == lado_a and base != lado_c):
        print("El triangulo es un isósceles")
    elif(base != lado_a and base != lado_c):
        print("El triangulo es un escaleno")
    
    print('El area del triangulo que ingresaste es:  ' +  str(area_triangulo))
      
      
if __name__ == '__main__':
 run();