lista=[]
cantidad=int(input("Ingrese el número de palabras que desea procesar: "))
for a in range (cantidad):
    i=input(f"Ingrese palabra {a+1}: ")
    lista.append(i)
print(lista)