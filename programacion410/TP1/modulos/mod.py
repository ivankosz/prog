
from fileinput import filename
from msilib.schema import File
from tkinter import N


def diccionario_interactivo():
    print('¡Bienvenidx al TP1 del curso de programación!\nUsted ha ingresado al modo interactivo.')
    with open('modo_interactivo.txt', 'w', encoding='utf-8') as archivo:
        try:
            d=open('spanish.lst')
        except FileNotFoundError:
            print("No se encontró el archivo 'spanish.lst'. Descargue un diccionario antes de comenzar.")
            raise SystemExit
        except UnboundLocalError:
            print("No se encontró el archivo 'spanish.lst'. Descargue un diccionario antes de comenzar.")
            raise SystemExit
        diccionario=d.read()
        entrada=input('> ')
        cont=0
        while entrada != '@fin':
            archivo.write(entrada + "\n")
            entrada=input('> ')
    with open('modo_interactivo.txt','r',encoding='utf-8') as archivo:
        a,b='áéíóúü','aeiouu'
        l=[]
        for linea in archivo.readlines():
            low=linea.lower()
            for palabra in low.split():
                trans=str.maketrans(a,b)
                p=palabra.translate(trans)
                e=''.join(char for char in p if char.isalnum())
                if e not in diccionario:
                    cont+=1
                    l.append(e)
        print("Ha finalizado el ingreso de texto.")
        if cont==0:
            print("Todas las palabras citadas están en el diccionario.")
        else:
            print(f"El texto contiene {cont} {'palabra' if cont==1 else 'palabras'} que no {'esta' if cont==1 else 'están'} en el diccionario.")
            print("Palabras no encontradas:")
            for n in l:
                print("-"+n)

def texto_plano(file):
    with open(file,'r',encoding='utf-8') as archivo:
        try:
            d=open('spanish.lst')
        except FileNotFoundError:
            print("No se encontró el archivo 'spanish.lst'. Descargue un diccionario antes de comenzar.")
            raise SystemExit
        except UnboundLocalError:
            print("No se encontró el archivo 'spanish.lst'. Descargue un diccionario antes de comenzar.")
            raise SystemExit
        diccionario=d.read()
        l=[]
        cont=0
        a,b='áéíóúü','aeiouu'
        for linea in archivo.readlines():
            low=linea.lower()
            for palabra in low.split():
                trans=str.maketrans(a,b)
                p=palabra.translate(trans)
                e=''.join(char for char in p if char.isalnum())
                if e not in diccionario:
                    cont+=1
                    l.append(e)
        if cont==0:
            print("Todas las palabras citadas están en el diccionario.")
        else:
            print(f"El texto contiene {cont} {'palabra' if cont==1 else 'palabras'} que no {'esta' if cont==1 else 'están'} en el diccionario.")
            print("Palabras no encontradas:")
            for n in l:
                print("-"+n)
        d.close()

def sys_modo():
    import sys
    n=len(sys.argv)
    if n==1:
        diccionario_interactivo()
    else:
        texto_plano(sys.argv[1])
        
def nueva_oportunidad():
    print('¡Bienvenidx al TP1 del curso de programación!\nUsted ha ingresado al modo interactivo.')
    with open('modo_interactivo.txt', 'w', encoding='utf-8') as archivo:
        try:
            d=open('spanish.lst')
        except FileNotFoundError:
            print("No se encontró el archivo 'spanish.lst'. Descargue un diccionario antes de comenzar.")
            raise SystemExit
        except UnboundLocalError:
            print("No se encontró el archivo 'spanish.lst'. Descargue un diccionario antes de comenzar.")
            raise SystemExit
        diccionario=d.read()
        entrada=input('> ')
        cont=0
        while entrada != '@fin':
            archivo.write(entrada + "\n")
            entrada=input('> ')
    with open('modo_interactivo.txt','r',encoding='utf-8') as archivo:
        a,b='áéíóúü','aeiouu'
        l=[]
        for linea in archivo.readlines():
            low=linea.lower()
            for palabra in low.split():
                trans=str.maketrans(a,b)
                p=palabra.translate(trans)
                e=''.join(char for char in p if char.isalnum())
                if e not in diccionario:
                    cont+=1
                    l.append(e)
        d.close()
        print("Ha finalizado el ingreso de texto.")
        if cont==0:
            print("Todas las palabras citadas están en el diccionario.")
        else:
            print(f"El texto contiene {cont} {'palabra' if cont==1 else 'palabras'} que no {'esta' if cont==1 else 'están'} en el diccionario.")
            print("Palabras no encontradas:")
            for n in l:
                print("-"+n)
            for n in l:
                print(f"La palabra {n} no se encuentra en el diccionario.\n¿Qué desea hacer?")
                print("1. Agreagarla al diccionario\n2. Corregir palabra\n3. Ingorar y seguir")
                opcion=int(input("Su opción: "))
                if opcion==1:
                    d=open('spanish.lst','a', encoding='utf-8')
                    d.write('\n'+n)
                    d.close()
                    cont-=1
                elif opcion==2:
                    archivo=open('modo_interactivo.txt', 'rt', encoding="utf-8")
                    archivo2=open("modo_interactivo2.txt", 'wt', encoding="utf-8")
                    d=open('spanish.lst')
                    nuevapalabra=input("Escriba nuevamente la palabra: ")
                    diccionario=d.read()
                    a,b='áéíóúü','aeiouu'
                    low=nuevapalabra.lower()
                    trans=str.maketrans(a,b)
                    p=low.translate(trans)
                    e=''.join(char for char in p if char.isalnum())
                    print(e)
                    if e in diccionario:
                        cont-=1
                    lectura=archivo.read()         
                    archivolinea2=lectura.replace(n, nuevapalabra)
                    archivo2.write(archivolinea2)
                    archivo.close()
                    archivo2.close()
                    archivo=open('modo_interactivo.txt','w',encoding='utf-8')
                    archivo2=open('modo_interactivo2.txt','r',encoding='utf-8')
                    lectura=archivo2.read()
                    archivo.write(lectura)
                    archivo.close()
                    archivo2.close()
                elif opcion==3:
                    pass
    if cont==0:
        print("El texto no contiene palabras que no están en el diccionario.")
    else:
        print(f"El texto contiene {cont} {'palabra' if cont==1 else 'palabras'} que no {'esta' if cont==1 else 'están'} en el diccionario.")