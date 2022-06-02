
def mayor(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
def menor(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2

i=int(input("Ingrese un numero: "))
max=-i
min=i

while i >= 0:
    max=mayor(i, max)
    min=menor(i, min)
    i=int(input("Ingrese un numero: "))

print (f"El numero mas alto es: {max}")
print (f"El numero mas bajo es: {min}")