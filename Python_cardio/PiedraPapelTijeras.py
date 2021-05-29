def run():
    menu = """
            Bienvenido a piedra, papel o tijera
            Tienen 3 intentos
            """
    print(menu)
    jugador1 = input("Ingrese el nombre del primero jugador:")
    jugador2 = input("Ingrese el nombre del segundo jugador:")


    contador1 = 0
    contador2 = 0
    menu_opciones = """ 
        Elija las siguientes opciones:
        1. Piedra
        2. Papel
        3. Tijera
                ** Solo coloque el número de la opción
        """     
    print(menu_opciones)

    i = 0
    while( i< 3):
        contador_jugadas = i + 1
        jugada1 = input("Intento No." + str(contador_jugadas) + " de" + jugador1)
        jugada1 = int(jugada1)
        jugada2 = input("Intento No." + str(contador_jugadas) + " de" + jugador2)
        jugada2 = int(jugada2)
       
        if(jugada1 == 1 and jugada2 == 3 or jugada1 == 3 and jugada2 == 1)  :  #Ganador piedra
                if(jugada1 < jugada2):
                        contador1 += 1
                elif (jugada2 >  jugada2):
                        contador2 += 1
        elif(jugada1 == 3 and jugada2 == 2 or jugada1 == 2 and jugada2 == 3) :  #Ganador tijera
                if(jugada1 > jugada2):
                        contador1 += 1
                elif (jugada2 < jugada2):
                        contador2 += 1
        elif(jugada1 == 2 and jugada2 == 1 or jugada1 == 1 and jugada2 == 2) :  #Ganador papel
                if(jugada1 > jugada2):
                        contador1 += 1
                elif (jugada2 < jugada2):
                        contador2 += 1

        i = i + 1
       
    print("Juego ha terminado:")


    if(contador1 > contador2) :
        print('Ganaste: ' +  str(jugador1))
    elif(contador2 > contador1) :
        print('Ganaste: ' +  str(jugador2))




if __name__ == '__main__':
 run();