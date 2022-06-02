
numero=int(input("Ingrese un numero: "))
contador=0
for x in range(numero):
    contador+=x+1
print("La suma es: "+str(contador))


numero=int(input("Ingrese un numero: "))
print(f"La suma es: {str(numero*(numero+1)//2)}")


numero=int(input("Ingrese un numero: "))
contador=numero
while contador!=0:
    numero+=contador-1
    contador=contador-1
print("La suma es: "+str(numero))


