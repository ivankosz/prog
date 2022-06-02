a={'Dolar':'$', 'Euro':'€', 'Yen':'¥', 'Peso argentino':'$'}
div=input("Ingrese una divisa para saber el símbolo: ")

if div in a:
    print(f"El símbolo es: {a.get(div)}")
else:
    print("La divisa no existe")