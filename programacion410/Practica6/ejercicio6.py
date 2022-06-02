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

def materia(h):
    diccionario['clase']['estudiante']['materias'][h]=diccionario['clase']['estudiante']['materias'].pop('geografia')

materia('historia')
print(diccionario)