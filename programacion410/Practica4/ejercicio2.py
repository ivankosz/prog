import random 

lista=[]                                                        #defino una lista vacia
def rant():
    return random.randint(-1000,1000)
cont=0  

for a in range (100):
    lista.append(rant())                                        #adiciono a mi lista un numero random a traves de la funcion rant que me devuelve un numero random.
print(lista)

for a in lista:
    cont+=a                                                     #aca simplemente sumo cada numero nuevo a mi contador. "a" en cada iteracion es un elemento nuevo en mi lista.
print(f"Suma: {cont}")
print(f"Promedio: {cont//100}")

"""
listarandom=[random.randint(-1000,1000) for a in range (100)]        #forma contraida del mismo ejercicio, modulo random+ iteracion todo en la misma variable
print(listarandom)
for a in listarandom:
    cont+=a
print(f"Suma: {cont}")
print(f"Promedio: {cont//100}")

"""


