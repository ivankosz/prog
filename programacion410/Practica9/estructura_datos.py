

class Estructura_de_datos:

    def __init__(self):
        self._items=[]

    def agregar (self, elemento):
        self._items.append(elemento)
    
    def _get_items (self):
        return self._items
    
    def vacia(self):
        return self._items==[]

    def cant_elementos(self):
        print(f"Hay {len(self._items)} {'elemento' if len(self._items)==1 else 'elementos'} en la {type(self).__name__}")
        return len(self._items)



class Pila (Estructura_de_datos):

    def apilar (self, elemento):
        super().agregar(elemento)
    
    def desapilar (self):
        try:
            return super()._get_items().pop()
        except IndexError:
            print ('La pila está vacía.')
    
    def top (self):
        return super()._get_items()[-1]


class Cola (Estructura_de_datos):

    def encolar (self, elemento):
        super().agregar(elemento)
              
    def desencolar (self):
        try:
            return super()._get_items().pop(0)
        except IndexError:
            print ('La cola está vacía.')
    
    def top (self):
        return super()._get_items()[0]

"""
pilita= Pila()
pilita.apilar(34)
pilita.apilar(2)
pilita.apilar(999)

print(pilita.top())

colita= Cola()
colita.encolar(34)
colita.encolar(2)
colita.encolar(999)

print(colita.top())

pilita.vacia()
colita.vacia()

pilita.desapilar()
colita.desencolar()
colita.desencolar()
colita.desencolar()
colita.desencolar()
pilita.cant_elementos()
colita.cant_elementos()
"""