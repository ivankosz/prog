import random
from random import choice

print("              Solo en el Universo")
print("................................................................")
print("Space X es una antigua empresa de viajes interestelares, fundada por el ya difunto Elon Musk a comienzos del SXXI. En principio realizaron viajes a Marte que solo podian ser costeados por pocos. Hoy, habiendo varios planetas en nuestro sistema colonizados y habitados, Space X es lo que antes se cononocian como aerolineas")
print("................................................................")
print("              Welcome to Space X")
print("                            *****")
print("            Have a great Xperience")
system=['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
origen=[]
destino=[]
players=dict()
surv=[]
hab=[]
nohab=system.copy()
cant=int(input("Cantidad de Jugafores: "))

for a in range (cant):
    id=dict()
    n=input("Ingrese su ID:")
    m=input("Ingrese su planeta de origen: ")
    id["Nombre"]=n
    id["Planeta de origen"]=m
    hab.append(m)
    v=input("¿desea realizar un viaje? (s/n): ")
    if v=="s":
        print(system)
        mv=input("Elija un mundo al cual viajar: ")
        id["Planeta actual"]=mv
        destino.append(mv)
    elif v=="n":
        id["Planeta actual"]=m
    players[a+1]=id

print(players, id)
