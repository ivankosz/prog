from typing import Type


def buscar_id(file):
    import csv
    with open(file, newline='', encoding='utf-8') as archivo:
        reader=csv.DictReader(archivo)
        datos=dict()
        for row in reader:
            datos[row['id']]=row
            datos[row['id']].pop('id')
        buscar=str(input("Ingrese un Id numérico: "))
        for info, values in datos[buscar].items():
            print(f"{info}: {values}")

def generador_contraseñas():
    import string
    import random
    from random import choice
    alfamin=string.ascii_lowercase
    alfamay=string.ascii_uppercase
    numeros=string.digits
    especiales=string.punctuation
    bolsa=alfamin+alfamay+numeros+especiales

    caracter=int(input("Ingrese la cantidad de caracteres para su contraseña (min 5): "))
    while caracter<5:
        print("Cantidad mínima de caracteres: 5")
        caracter=int(input("Ingrese la cantidad de caracteres para su contraseña (min 5): "))
    cant=int(input("Ingrese la cantidad de constraseñas a generar: "))
    contraseñas=dict()
    for a in range(cant):
        l=[]
        for b in range(caracter):
            c=choice(bolsa)
            l.append(c)
        contraseñas[a+1]=l
        print(contraseñas.get(a+1))

def generador_contraseñas2():
    import string
    import random
    from random import choice
    alfamin=string.ascii_lowercase
    alfamay=string.ascii_uppercase
    numeros=string.digits
    especiales=string.punctuation
    bolsa=alfamin+alfamay+numeros+especiales

    caracter=int(input("Ingrese la cantidad de caracteres para su contraseña (min 4): "))
    while caracter<4:
        print("Cantidad mínima de caracteres: 4")
        caracter=int(input("Ingrese la cantidad de caracteres para su contraseña (min 4): "))
    cant=int(input("Ingrese la cantidad de constraseñas a generar: "))
    contraseñas=dict()
    if caracter==4:
        for a in range(cant):
            cadena=choice(alfamin)+choice(alfamay)+choice(numeros)+choice(especiales)
            l=list(cadena)
            random.shuffle(l)
            result=''.join(l)
            contraseñas[a]=result
            print(contraseñas.get(a))

    else:
        for a in range(cant):
            cadena=choice(alfamin)+choice(alfamay)+choice(numeros)+choice(especiales)
            for a in range(caracter-4):
                resto=choice(bolsa)
                cadena+=resto
                l=list(cadena)
                random.shuffle(l)
                result=''.join(l)
            contraseñas[a]=result
            print(contraseñas.get(a))

def diccionario_datos():
    print('Bienvenido al generador de diccionario del curso.')
    with open ('dict.txt', 'w') as archivo:
        print('Elija el prefijo del diccionario:\n1- 004\n2- 011\n3- 044')
        while True:
            try:
                prefijo=str(input('Su opción: '))
                if prefijo!= '004' and prefijo!= '011' and prefijo!= '044':
                    raise ValueError
                break
            except ValueError:
                print('Prefijo inválido.Intente nuevamente.')
        while True:
            try:
                empezar=input('Elija el número para empezar a generar (hasta 8 digitos): ')
                if empezar=='':
                    empezar=0 
                elif int(empezar) > 99999999:
                    raise TypeError
                break
            except TypeError:
                print('El numero ingresado no puede superar los 8 digitos.')
            except ValueError:
                print('Ingrese un valor numerico, o presione Enter para generar desde 0.')
        while True:
            try:
                termina=input('Elija el número donde temrina de generar: ')
                if termina=='':
                    termina=10000
                elif int(termina)< int(empezar):
                    raise TypeError
                elif int(termina) > 99999999:
                    raise ValueError
                break
            except ValueError:
                print('Ingrese un número válido.')
            except TypeError:
                print('El numero en que termina no puede ser menor al que empieza.')

        if prefijo == '004':
            for numero in range(int(empezar), int(termina)+1):
                archivo.write('004'+str(numero).zfill(8)+'\n')
        elif prefijo == '011':
            for numero in range(int(empezar), int(termina)+1):
                archivo.write('011'+str(numero).zfill(8)+'\n')
        elif prefijo == '044':
            for numero in range(int(empezar), int(termina)+1):
                archivo.write('044'+str(numero).zfill(8)+'\n')


        archivo.close()
