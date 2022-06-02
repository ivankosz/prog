import random

print(":::::::::::::::::::::::::")
print("¡Piedra, Papel o Tijeras!")
print(":::::::::::::::::::::::::")

def intro():
    print("")                                       
    print("1.Piedra")
    print("2.Papel")
    print("3.Tijeras")               
    print("0.Salir")
    print("")

def cpu():
    return random.randint(1, 3)

def emp(n1,n2):
    if n1==n2:
        return True

def compare(n1,n2):
    if (n1==PIEDRA and n2==TIJERAS) or (n1==PAPEL and n2==PIEDRA) or (n1==TIJERAS and n2==PAPEL): 
        return True
    elif (n1==PIEDRA and n2==PAPEL) or (n1==PAPEL and n2==TIJERAS) or (n1==TIJERAS and n2==PIEDRA):
        return False

PIEDRA=1
PAPEL=2
TIJERAS=3
intro()
player1=int(input("Elije una opción: "))
contadorplayer1=0
contadorcpu=0

while player1!=0:
    pc=cpu()
    print(f"La Cpu eligio: {pc}")

    if player1 >3 or player1 <0:
        print("OPCION INCORRECTA")
    elif compare(player1, pc):
        print(f"Perdi con un {pc} y tiro otra vez")
        pc=cpu()
        if compare(player1, pc):
            print(f"Ahora saque {pc}")
            contadorplayer1+=1
            print("Ganaste")
        elif compare(player1, pc) ==False:
            print(f"Ahora saque {pc}")
            contadorcpu+=1
            print("Perdiste")
        else:
            print("Empate \n")
    elif compare(player1, pc) == False:
        contadorcpu+=1
        print("Perdiste")
    elif emp(player1, pc):
        print("Empate \n")  #hacer un def para delclarar el empate, antes que todo, pero que no quede en nada la funcion.
        
    intro()
    player1=int(input("Elije una opción: "))

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
    elif contadorplayer1 < contadorcpu:
        print(".................................")
        print("¡PERDISTE!La CPU ganó la partida.")
        print(".................................")