class Animal:

    def __init__(self, talk):
        self._talk= talk

    def hablar(self):
        print (f"{self._talk}!")

    def quien_sos(self):
        print (f"Soy un {type(self).__name__}")


class Gato (Animal):

    def __init__(self):
        super().__init__('Miau')

class Perro (Animal):

    def __init__(self):
        super().__init__('Guau')

class Pollo (Animal):

    def __init__(self):
        super().__init__('Pio')

class Humano (Animal):

    def __init__(self):
        super().__init__('Hola')

    def hablar(self):
        return f"¡{self._talk}!"

gatito= Gato()
perrito= Perro()
pollito= Pollo()
persona= Humano()

gatito.quien_sos()
gatito.hablar()
perrito.quien_sos()
perrito.hablar()
pollito.quien_sos()
pollito.hablar()
persona.quien_sos()
persona.hablar()
