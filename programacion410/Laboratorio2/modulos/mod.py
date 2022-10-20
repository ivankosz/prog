from dataclasses import replace
from datetime import datetime, timedelta
from multiprocessing.sharedctypes import Value

def calculadora_edad():
    cumple=input("Por favor ingrese su fecha de nacimiento en formato dd.mm.yyyy: ")
    fecha = datetime.strptime(cumple, "%d.%m.%Y")
    ahora=datetime.now()
    años= int(((ahora-fecha).days)/365)
    print(f"Ud. tiene {años} años.")

    if fecha.day == ahora.day and fecha.month == ahora.month:
        print("       , , , , , ,")
        print("       |_|_|_|_|_|")
        print("      |~=,=,=,=,=~|         Feliz Cumpleaños!")
        print("      |~~~~~~~~~~~|")
        print("    |~=,=,=,=,=,=,=~|")
        print("    |~~~~~~~~~~~~~~~|")
        print("  |~=,=,=,=,=,=,=,=,=~|")
        print("  |~~~~~~~~~~~~~~~~~~~|")
        print("(^^^^^^^^^^^^^^^^^^^^^^^)")
        print(" `'-------------------'`")

def registro_horas():
    while True:
        try:
            inicio=input("Fecha inicial (formato dd-mm-yyyy): ")
            fecha0=datetime.strptime(inicio, "%d-%m-%Y")
            break
        except ValueError:
            print('Ingrese la fecha en el formato indicado. gato.')
    while True:
        try:        
            cant=int(input("Cantidad de días: "))
            break
        except ValueError:
            print('Ingrese valor numérico entero.')
    registro='registro-'+inicio+'.txt'
    archivo=open(registro, "w", encoding='UTF-8')
    tiempo_total=0
    dates=[]
    for a in range(cant):
        l=[]
        fecha_nueva=fecha0.replace(day=fecha0.day+a)
        fecha_str=datetime.strftime(fecha_nueva, '%d-%m-%Y')
        while True:
            try:
                tiempo= int(input(f"Tiempo para el día {fecha_str}: "))
                break
            except ValueError:
                print('Ingrese un valor numérico entero.')
        tiempo_total+=tiempo
        l.append(fecha_str)
        l.append(tiempo)
        dates.append(l)

    archivo.write(f'Período: {inicio} al {fecha_str}\nTotal de minutos: {tiempo_total}\nPromedio de minutos: {tiempo_total/cant} minutos por día\n--Detalle:\n')
    for dia, minutos in dates:
        archivo.write(f'{dia}: {int(minutos)}\n')
    archivo.close()
    print(f'Se ha almacenado la información en el archivo {registro}')

def reloj_español():
    user_time=input('Ingrese una hora en formato HH:mm: ')
    if user_time == '':
        time=datetime.now()
        user_time=datetime.strftime(time, '%H:%M')
        hora=datetime.strptime(user_time, '%H:%M')
    else:
        hora=datetime.strptime(user_time, '%H:%M')


    h=''
    m=''

    if hora.minute >=0 and hora.minute <=2 or hora.minute >=58:
        m='en punto'
    elif hora.minute >=3 and hora.minute <=7:
        m='y cinco'
    elif hora.minute >=8 and hora.minute <=12:
        m='y diez'
    elif hora.minute >=13 and hora.minute <=17:
        m='y cuarto'
    elif hora.minute >=18 and hora.minute <=22:
        m='y veinte'
    elif hora.minute >=23 and hora.minute <=27:
        m='y veinticinco'
    elif hora.minute >=28 and hora.minute <=32:
        m='y media'
    elif hora.minute >=33 and hora.minute <=37:
        hora+=timedelta(hours=1)
        m='menos veinticinco'
    elif hora.minute >=38 and hora.minute <=42:
        hora+=timedelta(hours=1)
        m='menos veinte'
    elif hora.minute >=43 and hora.minute <=47:
        hora+=timedelta(hours=1)
        m='menos cuarto'
    elif hora.minute >=48 and hora.minute <=52:
        hora+=timedelta(hours=1)
        m='menos diez'
    elif hora.minute >=53 and hora.minute <=57:
        hora+=timedelta(hours=1)
        m='menos cinco'


    if hora.hour==1 or hora.hour==13:
        h='la una'
    elif hora.hour==2 or hora.hour==14:
        h='las dos'
    elif hora.hour==3 or hora.hour==15:
        h='las tres'
    elif hora.hour==4 or hora.hour==16:
        h='las cuatro'
    elif hora.hour==5 or hora.hour==17:
        h='las cinco'
    elif hora.hour==6 or hora.hour==18:
        h='las seis'
    elif hora.hour==7 or hora.hour==19:
        h='las siete'
    elif hora.hour==8 or hora.hour==20:
        h='las ocho'
    elif hora.hour==9 or hora.hour==21:
        h='las nueve'
    elif hora.hour==10 or hora.hour==22:
        h='las diez'
    elif hora.hour==11 or hora.hour==23:
        h='las once'
    elif hora.hour==12 or hora.hour==0:
        h='las doce'
    
    print(f'Son {h} {m}')

reloj_español()