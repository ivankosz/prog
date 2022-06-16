"""modulos de archivos"""

#Ej1
from email.encoders import encode_noop


def lectura(file):
    """lee el archivo"""
    with open(file, 'r', encoding='utf-8') as archivo:
        print(archivo.read())

#Ej2
def leer_n_lineas(file):
    """lee una cantidad determinada de lineas del archivo"""
    with open(file, 'r', encoding='utf-8') as archivo:
        cant=int(input("Ingrese la cantidad de lineas a leer: "))
        for a in range(cant):
            print(archivo.readline(), end="")


#Ej3
def leer_contar(file):
    "lee un archivo y cuenta las lineas que arrancan con el caracter elegido"
    "luego imprime la cantidad en pantalla"
    with open(file, 'r', encoding='utf-8') as archivo:
        i=input("Ingrese una letra a buscar: ").lower()
        c=0
        for a in archivo.readlines():
            b=a.lower()
            if i in b:
                indice=b.index(i)
                if indice==0:
                    c+=1
        print(f"La cantidad es: {c}")

#Ej4
def contar_palabras(file):
    with open(file, 'r', encoding='utf-8') as archivo:
        c=0
        for a in archivo.readlines():
            b=a.split()
            c+=len(b)
        print(c)

#Ej5
def cantidad_palabra(file):
    with open(file, 'r', encoding='utf-8') as archivo:
        palabra=input("Escriba la palabra que desea buscar: ").lower()
        c=0
        for a in archivo.readlines():
            lower=a.lower()
            b=lower.split()
            c+=b.count(palabra)
        print(f"La palabra {palabra} aparece {c} {'vez' if c==1 else 'veces'}")
#Ej5 v2.0
def cantidad_palabra2(file):
    with open(file, 'r', encoding="utf-8") as archivo:
        palabra=input("Ingrese la palabra que desea buscar: ").lower()
        lectura=archivo.read()
        low=lectura.lower()
        c=low.count(palabra)
        print(f"La palabra {palabra} aparece {c} {'vez' if c==1 else 'veces'}")

#Ej6
def palabras_cortas(file):
    with open(file, 'r', encoding='utf-8') as archivo:
        for a in archivo.readlines():
            b=a.split()
            for palabra in b:
                if len(palabra)<4:
                    print(palabra)

#Ej7
def cantidad_mayusculas(file):
    "cuenta la cantidad de mayusculas que aparecen en todo el archivo"
    "por cada linea, y por cada caracter en esa linea, cuenta las letras upper(mayusculas)"
    "Es necesario aclararle el encoding del idioma porque puede interpretar acentos y signos especiales como mays"
    with open(file, 'r', encoding='utf-8') as archivo:
        c=0
        for linea in archivo.readlines():
            for a in linea:
                if a.isupper():
                    c+=1
        print(c)

#Ej8 este ejercicio no me representa. ejercicio no reconocido.
def reemplazar_palabra(file):
    palabra=input("Ingrese una palabra para buscar: ").lower()
    archivo=open(file, 'rt', encoding="utf-8")
    archivo2=open("archivo-a", 'wt', encoding="utf-8")
    nuevapalabra=input(f"Escriba la palabra que desee reemplazar por {palabra}: ")
    lectura=archivo.read()
    low=lectura.lower()
    if palabra in low:
        archivolinea2=low.replace(palabra, nuevapalabra)
        print(archivolinea2)
        archivo2.write(archivolinea2)
    print(f"Fue reemplazada la palabra {palabra} por {nuevapalabra}")  
    archivo.close()
    archivo2.close()

#Ej8 2.0
def reemplazo_palabra2(file):
    pass

#Ej9
def agregar_contenido():
    with open('archivo_interactivo', 'w+', encoding='utf-8') as archivo:
        print("Ingrese el texto hasta que llegue una linea con 'fin': ")
        entrada=input()
        while entrada != 'fin':
            archivo.write(entrada + "\n")
            entrada=input()          
        archivo.close()
        print("Finalizó la toma de lineas")
#Ej10
def capital(file):
    with open(file, 'r', encoding='utf-8') as archivo:
        lista=[]
        for linea in archivo.readlines():
            cap=linea.replace(linea[0],linea[0].upper())
            lista.append(cap)
        op=open(file,'w',encoding='utf-8')
        op.writelines(lista)
        op.close()