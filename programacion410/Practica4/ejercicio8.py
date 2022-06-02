lista=[]
nolista=["hola", "chau", "nose", "si"]
cant=int(input("Ingrese el número de palabras que desea procesar: "))

for a in range(cant):
    i=input(f"Ingrese palabra {a+1}: ")
    while i in nolista:
        print(f"La palabra {i} está en la lista de palabras prohibidas, elija otra.")
        i=input(f"Ingrese palabra {a+1}: ")
    lista.append(i)
print(lista)
buscar=input("Ingrese la palabra que desea buscar: ")
if buscar in lista:
    l=lista.count(buscar)
    print(f"La palabra {buscar} aparece {l} {'vez' if l==1 else 'veces'}\n")
else:
    print("\nLa palabra no está listada\n")