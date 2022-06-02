stock={'Mayonesa':140.50, 'Cerveza': 130, 'Agua mineral': 110.15, 'Servilleta': 65.20}

def compra(n1,n2):
    return n1*n2
cont=0
prod=input("Ingrese producto: ")

while prod != "fin":
    if prod =="parcial":
        print(f"Parcial compra: ${cont}")
    elif prod in stock:
        cant=int(input("Ingrese cantidad: "))
        precio=round(compra(stock.get(prod), float(cant)),2)
        print(f"El precio es: ${precio}")
        cont+=precio
    else:
        print("El producto no existe")
    prod=input("Ingrese producto: ")
    
print(f"El total de su compra es: ${cont}")