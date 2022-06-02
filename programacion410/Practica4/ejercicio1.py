lista=[1,2,3,4,5,6,7]                                     #creo una lista con los elementos pedidos, y luego una lista vacia
listanueva=[]                                             

def cuadrado(n1):                                         #una funcion que multiplique a cada elemento en la primera lista por si mismo y me devuelva ese valor
    cuad=n1*n1
    return cuad

for a in lista:
    listanueva.append(cuadrado(a))                       #a la vez que lo agrego.a mi nueva lista(lo paso por la funcion(usando cada elemento "a" en la lista original))
print(listanueva)