print("Bienvenido al Banco Provincia")
saldo= 1000
print("Su saldo actual es de: "+str(saldo))
extraccion= int(input("Ingrese monto a extraer: "))
saldonuevo=(saldo-extraccion)

if extraccion <= saldo:
    print("Ha extraido "+str(extraccion))
    print("Le queda en cuenta: "+str(saldonuevo))
    print("Gracias por operar con el Banco Provincia")

else:
    print("No hay suficiente saldo para completar la operacion")


