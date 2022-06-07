from random import choice

inscritos=dict()

#menu
print("1-nueva inscripción \n2-ver inscritos \n3-salir")
print("")
print("0-realizar sorteo")
print("")

e=int(input("Elija una opción: "))

while e !=3:
    if e==1:
        dni=int(input("DNI: "))
        if dni not in inscritos:
            i=dict()
            apellido=input("Apellido: ").capitalize()
            nombre=input("Nombre: ").capitalize()
            doc=input("Documentación (s/n): ")
            observaciones=input("Observaciones: ")
            i["Apellido"]=apellido
            i["Apellido"]=apellido
            i["Nombre"]=nombre
            i["Documentacion"]=doc
            inscritos[dni]=i
            print("")
        else:
            print("Ya existe una inscripción con ese DNI.\n")
    elif e==2:
        print(inscritos)
    print("1-nueva inscripción \n2-ver inscritos \n3-salir")
    print("")
    print("0-realizar sorteo")
    print("")
    e=int(input("Elija una opción: "))
    if e==0:
        vac=int(input("Cantidad de vacantes: "))
        for a in range(vac):
            sorteo=choice(inscritos)
            print(sorteo)
print("Programa terminado")