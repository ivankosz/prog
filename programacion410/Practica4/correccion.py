tempmax=0
tempmin=9999999
diamax=""
diamin=""
listadias=["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
for t in listadias:
    temp=float(input("Ingrese la temperatura del dia: "+t )) #el dia queda muy pegado a donde se pone la temp
    if temp > tempmax:
        tempmax=temp
        diamax=t
    if temp < tempmin:
        tempmin=temp
        diamin=t
print(f"La temperatura menor se dio el dia: {diamin}") #el resultado no incluye las temperaturas
print(f"La temperatura mayor se dio el dia: {diamax}")

#no se usaron funciones
#