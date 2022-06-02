numero=int(input("Ingrese un numero: "))


def iteracion(n1):
    contador=0
    for x in range(n1):
        contador+=x+1
    return print(f"La suma es {contador}")

def formula(n1):
    n2=n1*(n1+1)//2
    return print(f"La suma es {n2}")


iteracion(numero)
formula(numero)

