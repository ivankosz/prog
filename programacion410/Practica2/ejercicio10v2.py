import random

print(":::::::::::::::::::::::::")
print("¡Piedra, Papel o Tijeras!")
print(":::::::::::::::::::::::::")

print("")                                       #print("1.Piedra \n2.Papel \n3.Tijeras") alternativa de escritura
print("1.Piedra")
print("2.Papel")
print("3.Tijeras")               
print("")
print("0.Salir")
print("")

cpu= random.randint(1, 3)                    #la variable que determina la eleccion del cpu
player1=int(input("Elije una opción: "))
contadorplayer1=0
contadorcpu=0

while player1 <0 or player1 >3:
        print("OPCION INCORRECTA")
        player1=int(input("Elija una opción: "))
    
print(f"La Cpu eligio: {str(cpu)}")

while player1!=0:

    if player1==1 and cpu==1:                        #elplayer1 elije "piedra"
        print("Empate")
        print("")
    elif player1==1 and cpu==2:
        print("Papel envuelve a Piedra. Perdiste.")
        print("")
        contadorcpu +=1
    elif player1==1 and cpu==3:
        print("Piedra rompe Tijeras. ¡Ganaste!")
        print("")
        contadorplayer1 +=1


    if player1==2 and cpu==1:                           #el player1 elije "papel"
        print("Papel envuelve a Piedra. ¡Ganaste!.")
        print("")
        contadorplayer1 +=1
    elif player1==2 and cpu==2:
        print("Empate")
        print("")
    elif player1==2 and cpu==3:
        print("Tijeras cortan Papel. Perdiste.")
        print("")
        contadorcpu +=1


    if player1==3 and cpu==1:                          #el player1 elije "tijeras"
        print("Piedra rompe Tijeras. Perdiste.")
        print("")
        contadorcpu +=1
    elif player1==3 and cpu==2:
        print("Tijeras cortan Papel. ¡Ganaste!")
        print("")
        contadorplayer1 +=1
    elif player1==3 and cpu==3:
        print("Empate")
        print("")

    print("1.Piedra")
    print("2.Papel")
    print("3.Tijeras")
    print("")
    print("0.Salir")
    print("")
    cpu= random.randint(1, 3)
    player1=int(input("Elije una opción: "))

    while player1 <0 or player1 >3:
        print("OPCION INCORRECTA")
        player1=int(input("Elija una opción: "))

    print(f"La Cpu eligio: {str(cpu)}")

if player1==0:
    print("")
    print("Fin de partida")
    print("")
    print("::::PUNTAJE::::")
    print(f"Player: {str(contadorplayer1)}")
    print(f"Cpu: {str(contadorcpu)}")
    print(":::::::::::::::")
    print("")
    if contadorplayer1 > contadorcpu:
        print("::::::::::::::::::::")
        print("¡GANASTE LA PARTIDA!")
        print("::::::::::::::::::::")
    if contadorplayer1 < contadorcpu:
        print(".................................")
        print("¡PERDISTE!La CPU ganó la partida.")
        print(".................................")