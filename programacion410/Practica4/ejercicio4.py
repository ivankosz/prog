semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

def max(n1,n2,dia):
    if n1 > n2:
        global diamax
        diamax=dia 
        return n1
    else:
        return n2
def min(n1, n2,dia):
    if n1 < n2:
        global diamin
        diamin=dia
        return n1
    else:
        return n2

tempmax=-1
tempmin=9999
diamax="string"
diamin="string"

for a in semana:
    temp=float(input(f"Ingrese la temperatura media del {a}: "))
    tempmax=max(temp, tempmax,a)
    tempmin=min(temp,tempmin,a)
print(f"La máxima se dió el dia {diamax}, con {tempmax}°C")
print(f"La mínima se dió el dia {diamin}, con {tempmin}°C")