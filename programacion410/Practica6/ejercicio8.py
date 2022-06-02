cant=int(input('Ingrese un número: '))
def tupla(n):
    l=[]
    for a in range(n):
        l.append(a)
    t=tuple(l)
    return t
t=tupla(cant)
print(t)