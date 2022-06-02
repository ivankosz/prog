temp = {
    'domingo': 23.3,
    'lunes': 22.6,
    'martes': 18.9,
    'miercoles': 17.2,
    'jueves': 19.4,
    'viernes': 20.0,
    'sabado': 24.1
}
def min_temp(t):
    dmin="."
    min=9999
    for key, value in t.items():
        if value<min:
            min=value
            dmin=key
    print(f'El día con menor temperatura fue el {dmin} con {min}°C')

min_temp(temp)