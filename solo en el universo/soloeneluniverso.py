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
id=[]
surv=[]
hab=[]
nohab=system.copy()
cant=int(input("Cantidad de Jugafores: "))

for a in range (cant):
    p=[]
    n=input("Ingrese su ID:")
    m=input("Ingrese su planeta de origen: ")
    p.append(n)
    hab.append(m)
    v=input("¿desea realizar un viaje? (s/n): ")
    if v=="s":
        print(system)
        mv=input("Elija un mundo al cual viajar: ")
        p.append(mv)
        destino.append(mv)
    elif v=="n":
        p.append(m)
    id.append(p)

def planeta_rehab():
    for m in destino:
        if destino.count(m) >=2:
            hab.append(m)
def planeta_nohab():
    for e in hab:
        for f in nohab:
            if e == f:
                nohab.remove(f)
"""           
for m in destino:
    if destino.count(m) >=2:           #Si dos o mas jugadores elijen el mismo destino, ese planeta se vuelve habitado.
        hab.append(m)

for e in hab:
    for f in nohab:
        if e == f:
            nohab.remove(f)
"""

#asteroide
def asteroid():
    r=choice(system)
    system.remove(r)
    if r in hab:
        hab.remove(r)
    elif r in nohab:
        nohab.remove(r)
    return r

#planetas deshabitados
def planetas_deshabitados(n1):
    for g in nohab:
        if g==n1:
            return True

#planetas habitados
def planetas_habitados(n2):
    for h in hab:
        if h==n2:
            return True

planeta_rehab()
planeta_nohab()
rokita=asteroid()
print(f"El asteroide impacto en {rokita}")
for nom, des in id:
    print(f"{nom} está en {des}")
    if des!=rokita and not planetas_deshabitados(des):        #funciona bien
        surv.append(nom)
        origen.append(des)
for j in surv:
    print(f"{j} sobrevivió.")


destino.clear()
id.clear()

print(system) #los planetas existentes en el sistema
print(id) #jugadores y sus mundos actuales
print(hab) #habitados (mundos de  y vueltos habitables)
print(nohab) #deshabitados
print(surv) #sobrevivientes, pasan a la siguiente ronda.
print(origen) #los planetas desde donde parten en la ronda 2

for k in surv:
    p=[]
    p.append(k)   
    v=input(f"¿{k} desea realizar un viaje? (s/n): ")
    if v=="s":
        print(system)
        mv=input("Elija un mundo al cual viajar: ")
        p.append(mv)
        destino.append(mv)
    elif v=="n":
        p.append(origen)
    id.append(p)

surv.clear()

print(system) #los planetas existentes en el sistema
print(id) #jugadores y sus mundos actuales
print(hab) #habitados (mundos de  y vueltos habitables)
print(nohab) #deshabitados
print(surv) #sobrevivientes, pasan a la siguiente ronda.
print(origen) #los planetas desde donde parten en la ronda 2
