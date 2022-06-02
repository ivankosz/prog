from pickle import TRUE
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
mundo=[]
destino=[]
id=[]
surv=[]
nohab=system.copy()
cant=int(input("Cantidad de Jugafores: "))

for a in range (cant):
    p=[]
    n=input("Ingrese su ID:")
    m=input("Ingrese el nombre de su mundo: ")
    p.append(n)
    mundo.append(m)
    v=input("¿desea realizar un viaje? (s/n): ")
    if v=="s":
        print(system)
        mv=input("Elija un mundo al cual viajar: ")
        p.append(mv)
    elif v=="n":
        p.append(m)
    id.append(p)
for e in mundo:
    for f in nohab:
        if e == f:
            nohab.remove(f)

#asteroide
def asteroid():
    r=choice(system)
    system.remove(r)
    return print (r)

#planetas deshabitados
def planetas_deshabitados(n1):
    for g in nohab:
        if g==n1:
            return True

#planetas habitados
def planetas_habitados(n2):
    for h in mundo:
        if h==n2:
            return True
rokita=asteroid()

for nombre, destino in id:
    print(f"{nombre} está en {destino}")
    if destino!=rokita and not planetas_deshabitados(destino):        #funciona bien
        surv.append(nombre)
for j in surv:
    print(f"{j} sobrevivió.")
print(system)
print(id) #jugadores y sus mundos actuales
print(mundo) #habitados (mundos de origen y vueltos habitables)
print(nohab) #deshabitados
print(surv) #sobrevivientes, pasan a la siguiente ronda.
