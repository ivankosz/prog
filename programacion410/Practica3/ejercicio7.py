import random

def dado():
    return random.randint(1, 6)

def compare(n1,n2):
    if n1 == n2:
        return True
    else:
        return False

p1=int(input("Ingrese un numero del 1 al 6: "))

while compare(p1, dado())==False:   
    if p1 >6 or p1 <1:
        print("Numero inválido")
    else:
        print("Estuviste cerca, volve a intentar")
    p1=int(input("Ingrese un numero del 1 al 6: "))

print(f"Muy bien, el numero era {p1}")