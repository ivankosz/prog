import random

player=str(input("Jugador/a: "))
ruleta=random.randint(0,99)
general=[]
ganadores=[]

while player!=".":
    jugadoryapuesta=[]
    jugadoryapuesta.append(player)
    bet=int(input("Apuesta: "))
    while bet <0 or bet >99:
        print("Apuesta Inválida")
        bet=int(input("Apuesta: "))
    jugadoryapuesta.append(bet)
    general.append(jugadoryapuesta)
    player=str(input("Jugador/a: "))  
print(general)
print(f"\nSalió sorteado el número {ruleta}\n")
for jugador, apuesta in general:
    if ruleta==apuesta:
        ganadores.append(jugador)
    

print("\nGanadores:")
for a in ganadores:
   print(a)
if len(ganadores)==0:
    print("No hubo ganadores")