a={'Dolar': {'simbolo' :'$', 'valor':119.4}, 'Euro': {'simbolo':'€', 'valor': 128.07}, 'Yen':{'simbolo':'¥', 'valor':1.06}, 'Peso argentino': {'simbolo':'$' , 'valor':1}}

m=(input("Ingrese el monto en pesos: "))

def conversion(n1,d1):
    conv=n1/a[d1].get('valor')
    return conv
while not m.isnumeric():
    print("Error en el valor ingresado")
    m=(input("Ingrese el monto en pesos: "))

d=input("Ingrese la divisa para convertir: ")
if d in a:  
    print(f"{m} pesos argentinos es equivalente a: {round(conversion(float(m),d), 2)} {a[d].get('simbolo')}")
    print(f"1 {a[d].get('simbolo')} es igual a {a[d].get('valor')} pesos argentinos")
else:
    print("La divisa no existe")