import random

print("Welcome to 7 y medio: THE GAME")

mazo=[]
results=[]

players=int(input("Elija la cantidad de Jugadores (mínimo 2): "))

while players<2:
    print("Error en la matrix")
    players=int(input("Elija la cantidad de Jugadores (mínimo 2): "))
#modulo mazo
def deck():
    global mazo
    for a in range(1,13):
        for b in range (4):
            mazo.append(a)
    for c in range (4):
        mazo.remove(8), mazo.remove(9)
    random.shuffle(mazo)
    print(mazo)

#modulo valor
def valor(n1):
    if n1<=7:
        return n1
    else:
        return 0.5
#modulo puntaje
def puntaje(n2):
    return (n2>7.5)

def puntaje_ganador(n3):
    m=0
    if n3 > m:
        m=n3
        return m


deck()
for p in range(players):
    jugadores=[]
    cont=0
    carta=mazo.pop()
    print(f"Turno Jugador {p+1}")
    jugadores.append(p+1)
    print(f"Su carta este turno es: {carta}")
    cont+=valor(carta)
    print(f"En total lleva {cont}")
    desicion=input("¿Desea sacar otra carta? (s/n): ")   #hasta aca todo bien
    while desicion=="s" and not puntaje(cont):
        carta=mazo.pop()
        print(f"Su carta este turno es: {carta}")
        cont+=valor(carta)
        print(f"En total lleva {cont}")  #hasta aca parece que tambien ok
        if puntaje(cont):
            print("¡Perdiste!")
        else:
            desicion=input("¿Desea sacar otra carta? (s/n): ")
        
    print(f"El Jugador {p+1} terminó su partida con {cont}.")
    jugadores.append(cont)
    results.append(jugadores)
print(results)
max=0
pmax=0
for r, t in results:
    if t <= 7.5:
        print(f"El jugador {r} tiene {t} puntos")
        max=puntaje_ganador(t)
        if max>=t:
            pmax=r

         
print(f"El ganador es el jugador {pmax} con {max} puntos")
