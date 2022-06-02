def cantidad(c, s):
    if c in s:
        return s.count(c)
    else:
        return 0

string=input("Ingrese un string para procesar: ")
caracter=input("Ingrese un caracter para buscar: ")

print(f"El caracter {caracter} aparece {cantidad(caracter, string)} veces")