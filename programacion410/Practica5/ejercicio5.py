
nom=input("Ingrese un nombre: ")
lista=[]
lista.append(nom)
while nom != ".":
    nom=input("Ingrese un nombre: ")
    lista.append(nom)
print("Las personas son:")
for a in lista:
    print(a.capitalize())