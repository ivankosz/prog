def palabra(cad):
    lista=cad.split(sep=None, maxsplit=-1)
    cont=0
    for a in lista:
        cont+=1
    return print(f"La cadena tiene {cont} palabras")

cadena=input("Ingrese una cadena de strings: ")
palabra(cadena)