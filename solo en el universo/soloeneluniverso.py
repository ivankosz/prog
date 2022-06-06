from random import choice

#creacion de planetas rehabilitados 
def planeta_rehab():
    lista=[]
    for jugadores, datos in players.items():
        lista.append(datos['Planeta actual'])
    for a in lista:
        if lista.count(a) >=2:
            if a not in hab:
                hab.append(a)

#creacion de planetas deshabitados
def planeta_nohab():
    for e in hab:
        for f in nohab:
            if e == f:
                nohab.remove(f)

#asteroide
def asteroid():
    r=choice(system)
    system.remove(r)
    if r in hab:
        hab.remove(r)
    elif r in nohab:
        nohab.remove(r)
    return r

#planetas deshabitados, comprobacion
def planetas_deshabitados(n1):
    for g in nohab:
        if g==n1:
            return True

#planetas habitados, comprobacion
def planetas_habitados(n2):
    for h in hab:
        if h==n2:
            return True

print("              Solo en el Universo")
print("................................................................")
print("Space X es una antigua empresa de viajes interestelares, fundada por el ya difunto Elon Musk a comienzos del SXXI. En principio realizaron viajes a Marte que solo podian ser costeados por pocos. Hoy, habiendo varios planetas en nuestro sistema colonizados y habitados, Space X es lo que antes se cononocian como aerolineas")
print("................................................................")
print("              Welcome to Space X")
print("                            *****")
print("            Have a great Xperience")
system=['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
players=dict()
hab=[]
nohab=system.copy()
cant=int(input("Cantidad de Jugafores: "))
while cant<1:
    print("Cantidad de jugadores mínima: 1")
    cant=int(input("Cantidad de Jugafores: "))

#primera ronda

for a in range (cant):
    print(f"Turno jugador {a+1}")
    id=dict()
    n=input("Ingrese su ID: ").capitalize()
    print(f"Hola {n}. Bienvenido a SpaceX.")
    print(system)
    m=input("Ingrese su planeta de origen: ").capitalize()
    while m not in system:
        print("Origen inexistente")
        m=input("Ingrese su planeta de origen: ").capitalize()
    id['Nombre']=n
    id['Planeta de origen']=m
    if m not in hab:
        hab.append(m)
    v=input("¿desea realizar un viaje? (s/n): ").lower()
    while v !="s" and v!="n":
        print("Ingreso inválido")
        v=input("¿desea realizar un viaje? (s/n): ").lower()
    if v=="s":
        print(system)
        mv=input("Elija un mundo al cual viajar: ").capitalize()
        while mv not in system:
            print("Destino inexistente")     
            mv=input("Elija un mundo al cual viajar: ").capitalize()
        while mv==m:
            print("Ya se encuentra en ese planeta.")
            mv=input("Elija un mundo al cual viajar: ").capitalize()
        print("Buen viaje.")
        id['Planeta actual']=mv
        id['cont']=0
    elif v=="n":
        id['Planeta actual']=m
        id['cont']=1
    id['ronda']=1
    players[a+1]=id


planeta_rehab()
planeta_nohab()
rokita=asteroid()
print(f"El asteroide impacto en {rokita}")

game_over=[]
for jugador, datos in players.items():
    print(f"{datos['Nombre']} está en {datos['Planeta actual']}")
    if datos['Planeta actual']==rokita or planetas_deshabitados(datos['Planeta actual']):
        game_over.append(jugador)     #no itera sobre un dict si cambia de tamaño asi que use una lista como puente.      
for a in game_over:
    players.pop(a)

lista=list(players.keys())

#siguientes rondas: el juego termina cuando queda uno solo vivo, o no quede nadie. En ese caso ganara el asteroide.

while len(lista)>1:
    print("Sobrevivientes:")
    for jugador, datos in players.items():
        print(f"{datos['Nombre']}")

    for jugador, datos in players.items():
        print(f"Turno de {datos['Nombre']}")
        if datos['cont']==0:
            v=input(f"¿{datos['Nombre']} desea realizar un viaje? (s/n): ").lower()
            while v !='s' and v!='n':
                print('Ingreso inválido')
                v=input(f"¿{datos['Nombre']} desea realizar un viaje? (s/n): ").lower()
            if v=="s":
                print(system)
                mv=input("Elija un mundo al cual viajar: ").capitalize()
                while m not in system:
                    print("Destino inválido")
                    mv=input("Elija un mundo al cual viajar: ").capitalize()
                while mv==datos['Planeta actual']:
                    print("Ya se encuentra en ese planeta.")
                    mv=input("Elija un mundo al cual viajar: ").capitalize()
                datos['Planeta actual']=mv
                datos['cont']=0
            elif v=="n":
                datos['cont']+=1
        else:
            print(system)
            mv=input(f"{datos['Nombre']}, elije un mundo al cual viajar: ").capitalize()
            while mv not in system:
                print("Destino inexistente")
                mv=input("Elija un mundo al cual viajar: ").capitalize()
            while mv==datos['Planeta actual']:
                print("Ya se encuentra en ese planeta.")
                mv=input("Elija un mundo al cual viajar: ").capitalize()
            datos['Planeta actual']=mv
            datos['cont']=0
        datos['ronda']+=1

    planeta_rehab()
    planeta_nohab()
    rokita=asteroid()
    print(f"El asteroide impacto en {rokita}")

    game_over=[]
    for jugador, datos in players.items():
        print(f"{datos['Nombre']} está en {datos['Planeta actual']}")
        if datos['Planeta actual']==rokita or planetas_deshabitados(datos['Planeta actual']):
            game_over.append(jugador)     #no itera sobre un dict si cambia de tamaño asi que use una lista como puente.      
    for a in game_over:
        players.pop(a)

    lista=list(players.keys())

if len(lista)==1:
    for jugador, datos in players.items():
        print(f"{datos['Nombre']} quedó solo en el universo")
        print("Fin")
        print("")
        if datos['Planeta de actual']==datos['Planeta de origen']:
            print(f"{datos['Nombre']} terminó sus días en {datos['Planeta actual']}, su planeta de origen")
        else:
            print(f"{datos['Nombre']} termino sus días en {datos['Planeta actual']}. Su planeta de origen, {datos['Planeta de origen']} fue destruido")
            print(f"Sobrevivió {datos['ronda']} contra {cant-1} jugadores.")
else:
    print("Fin del juego. No quedan sobrevivientes")

print(system) #los planetas existentes en el sistema
print(players) #jugadores, sus mundos de origen y sus mundos actuales
print(hab) #habitados (mundos de origen y rehabilitados)
print(nohab) #deshabitados

#Eureka. funciona.

#agregar easter egg, terminar frases finales, agregar contador de planetas visitados, agregar razas??, ideas...