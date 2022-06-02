cad=input("Ingrese un string para procesar: ")

def caracter(x):
    cont=0
    for a in x:
        cont+=1
        print(f"La letra {cont} es {a}")

caracter(cad)