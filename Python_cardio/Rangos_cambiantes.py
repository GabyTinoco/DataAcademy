def data():
    limite_inferior = print("Ingresa el limite inferior: ")
    limite_superior = print("Ingresa el limite superior: ")
    limite_comparacion = print("Ingresa el limite de comparacion:  ")
    
    if(limite_inferior >= limite_comparacion and limite_superior <= limite_comparacion) :
        return True
    else:
        return False 


def run():
    resultado = data()

    if(resultado == False) :
        data()
        

if __name__ == '__main__':
 run();