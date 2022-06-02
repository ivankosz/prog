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
print(f"{diccionario['clase']['estudiante']['materias'].get('geografia')}")