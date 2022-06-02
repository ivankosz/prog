saldo= 1000
print(".............................")
print("Bienvenido al Banco Provincia")
print("")
print("Su saldo actual es de: $"+str(saldo))
print(".............................")
print("¿Que desea hacer?")
print("1.Extracción")
print("2.Depósito")
print("3.Consultar Saldo")
print("")
print("0.Salir")
print("")
choice= int(input("Elija una opción: "))

while choice!=0:
    if choice==1:
        extraccion= int(input("Ingrese monto a extraer: "))
        if extraccion <= saldo:
            saldo -= extraccion
            print("Ha extraido $"+str(extraccion))
            print("Su saldo actual es de: $"+str(saldo))
            print("")
        if extraccion>saldo:
            print("...................................................")
            print("No hay suficiente saldo para completar la operacion")
            print("...................................................")
            print(".........................................")
            print("Gracias por operar con el Banco Provincia")
            print(".........................................")


    elif choice==2:
        deposito= int(input("Ingrese monto a depositar: "))
        saldo += deposito
        print("Ha depositado $" +str(deposito))
        print("Su saldo actual es de: $" +str(saldo))
        print("")

    elif choice==3:
        print("")
        print(f"Su saldo actual es de : ${str(saldo)}")
        print("")

    elif choice < 0 or choice > 2:
        print("........................")
        print("Opción incorrecta")
        print("........................")
    
    
    print("¿Que desea hacer?")
    print("1.Extracción")
    print("2.Depósito")
    print("3.Consultar Saldo")
    print("")
    print("0.Salir")
    print("")
    choice= int(input("Elija una opción: "))
    print("")

if choice==0:
    print("::::::::::::::::::::::::::::::::::::")
    print("Gracias por usar nuestros serivicios")
    print("::::::::::::::::::::::::::::::::::::")
    print("")