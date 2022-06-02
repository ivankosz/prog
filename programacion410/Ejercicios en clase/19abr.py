from random import*
lista=[]
inscripcion=input("Ingrese un nombre: ")
lista.append(inscripcion)

while inscripcion != "":
    lista.append(inscripcion)
    inscripcion=input("Ingrese un nombre: ")

a=choice(lista)
print(f"El ganador es {a}")