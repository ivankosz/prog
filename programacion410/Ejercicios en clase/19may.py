palabra=input("Ingrese una palabra: ")

def histograma(unaPalabra):
    d=dict()
    for a in unaPalabra:
        d[a]=unaPalabra.count(a)
    print(d)
histograma(palabra)