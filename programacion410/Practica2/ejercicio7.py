nota1=int(input("Ingrese la nota en el primer examen: "))
nota2=int(input("Ingrese la nota en el segundo examen: "))
nota3=int(input("Ingrese la nota en el tercer examen: "))
promedio=((nota1+nota2+nota3)/3)
promocion=8
reprobado=5
if promedio<promocion:
    print(f"La o el alumno NO promocionó la materia, su promedio fue de {str(promedio)}")
elif nota1<=reprobado or nota2<=reprobado or nota3<=reprobado:
    print(f"La o el alumno NO promocionó la materia por sacar <6 en un examen")
elif promedio>=promocion:
    print(f"!La o el alumno promocionó la materia con un promedio de {str(promedio)}!")