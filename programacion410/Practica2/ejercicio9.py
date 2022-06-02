import random

num = random.randint(1, 6)
dado=int(input("Ingrese un numero del 1 al 6: "))


while dado!=num:
    if dado > 6 or dado < 1:                                            #se pueden anidar uno o varios if y while dentro de un loop.
        print("Número inválido")
    dado=int(input("Fallaste. Ingrese un numero del 1 al 6: "))

print(f"¡Muy bién! el numero era {str(num)}")                            #el print se pone por fuera del loop de while, en la misma tab.