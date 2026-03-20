persona= {"nombre": "Sergio", "edad": 16, "ciudad": "Santa Marta"}

for clave in persona:
    print(clave)

for clave, valor in persona.items():
    print(clave + ": " + str(valor))