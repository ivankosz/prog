numero=input("Ingrese un numero: ")
contador=0
PUNTO="."
while numero!=PUNTO:
    contador+=int(numero)
    numero=input("Ingrese un numero: ")
    if numero==PUNTO:
        print("La suma es "+ str(contador))