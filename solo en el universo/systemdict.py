system={'Mercurio':'nohab', 'Venus':'nohab', 'Tierra':'nohab', 'Marte':'nohab', 'Jupiter':'nohab', 'Saturno':'nohab', 'Urano':'nohab', 'Neptuno':'nohab'}

players=dict()
cant=int(input("Cantidad de Jugafores: "))

for a in range (cant):
    id=dict()
    n=input("Ingrese su ID:")
    m=input("Ingrese su planeta de origen: ")
    id["Nombre"]=n
    id["Planeta de origen"]=m
    v=input("¿desea realizar un viaje? (s/n): ")
    if v=="s":
        print(system)
        mv=input("Elija un mundo al cual viajar: ")
        id["Planeta actual"]=mv
    elif v=="n":
        id["Planeta actual"]=m
    players[a+1]=id

print(players)