from datetime import datetime
ahora=datetime.now()
print(ahora)

fecha=datetime(1986,12,24)
print(fecha)
print("Día:", fecha.day)
print("Mes:", fecha.month)
print("Año:", fecha.year)

fe1=datetime(2021,6,30,13)
fe2=datetime(2021,6,30,18,45)
print(fe1)
print(fe2)

hoy=datetime.now()
fin_curso= datetime(2022,12,16)
diferencia= (fin_curso - hoy).days #Para quedarme solo con los dias.

if hoy<fin_curso:
    print("El curso de programación aún no ha finalizado.")
    print(f"{'Falta' if diferencia==1 else 'Faltan'} {diferencia} {'día' if diferencia == 1 else 'días'} para finalizar el curso.")
elif hoy == fin_curso:
    print("¡Hoy finaliza el curso de programación!")
elif hoy>fin_curso:
    print(f"El curso de programación ha finalizado hace {abs(diferencia)} {'día' if diferencia == 1 else 'días'} .") #abs (valor absoluto) para que no de dias negativos.

fecha= datetime.now()
print(fecha.strftime("%d.%m.%Y"))
print(fecha.strftime("%d/%m/%Y %H:%M"))

