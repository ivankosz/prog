def estaEn(a, b):
    if a in b:
        return True
    else:
        return False
cad1=input("Ingrese una cadena: ")
cad2=input("Ingrese otra cadena: ")
if estaEn(cad1, cad2):
    print("True")
else:
    print("False")