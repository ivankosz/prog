diccionario = {
    "clase": {
        "estudiante": {
            "nombre": "Marcos",
            "materias": {
                "matematica": 7,
                "geografia": 8
            }
        }
    }
}

def notas(n1,n2):
    diccionario['clase']['estudiante']['materias'].update(matematica=n1)
    diccionario['clase']['estudiante']['materias'].update(geografia=n2)

notas(8,7)
print(diccionario)