numero=input("Ingrese un numero: ")
contador=0
contador2=0
punto="."
while numero!=punto:
    contador+=int(numero)
    contador2+=1
    numero=input("Ingrese un numero: ")
    if numero==punto:
        print("La suma es "+ str(contador))
        promedio=contador/contador2
        print("El promedio es: "+ str(promedio))