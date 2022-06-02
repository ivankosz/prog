nombre=input("Ingrese un nombre: ")
contador=0
while nombre!="Juan" and nombre!="juan" and nombre!="JUAN":
    contador+=1
    nombre=input("Ingrese un nombre: ")
if nombre=="Juan" or nombre=="juan" or nombre=="JUAN":
    contador+=1
print("Llegaron "+str(contador)+"personas")