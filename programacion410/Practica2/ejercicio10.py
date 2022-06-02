import random

print(":::::::::::::::::::::::::")
print("¡Piedra, Papel o Tijeras!")
print(":::::::::::::::::::::::::")

print("")
print("1.Piedra")
print("2.Papel")
print("3.Tijeras")
print("")

cpu=random.randint(1, 3)
player1=int(input("Elija una opción: "))

if player1 <1 or player1 >3:
    print("OPCION INCORRECTA")
print(f"La Cpu eligio: {str(cpu)}")

if player1==1 and cpu==1:                        #elplayer1 elije "piedra"
    print("Empate")
    print("")
elif player1==1 and cpu==2:
    print("Papel envuelve a Piedra. Perdiste.")
    print("")
    
elif player1==1 and cpu==3:
    print("Piedra rompe Tijeras. ¡Ganaste!")
    print("")
    


if player1==2 and cpu==1:                           #el player1 elije "papel"
    print("Papel envuelve a Piedra. ¡Ganaste!.")
    print("")
    
elif player1==2 and cpu==2:
    print("Empate")
    print("")
elif player1==2 and cpu==3:
    print("Tijeras cortan Papel. Perdiste.")
    print("")
    


if player1==3 and cpu==1:                          #el player1 elije "tijeras"
    print("Piedra rompe Tijeras. Perdiste.")
    print("")
    
elif player1==3 and cpu==2:
    print("Tijeras cortan Papel. ¡Ganaste!")
    print("")
    
elif player1==3 and cpu==3:
    print("Empate")
    print("")
