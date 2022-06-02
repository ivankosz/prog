import random
from random import choice

lista=[]
cant=int(input("Cantidad de alumnos: "))
docente="Cristian"

for a in range(cant):
    p=input(f"Participante {a+1}: ")
    lista.append(p)
if cant %2==1:
    lista.append(docente)
listanueva=lista.copy()
random.shuffle(lista)
print("")
for a in lista:
    amigo=choice(listanueva)
    while amigo==a:
        amigo=choice(listanueva)
    listanueva.remove(amigo)
    print(f"{a} es el amigo invisible de {amigo}")
print("")