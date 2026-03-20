# Programa de registro de estudiantes con validación

estudiantes = []

for i in range(5):
    print(f"\nEstudiante {i+1}:")

    # Pedir nombre
    nombre = input("Nombre: ")

    # Pedir edad con validación
    while True:
        try:
            edad = int(input("Edad: "))
            if 5 <= edad <= 100:
                break
            else:
                print("Edad inválida. Debe estar entre 5 y 100 años.")
        except ValueError:
            print("Por favor, ingrese un número entero para la edad.")

    # Pedir calificación con validación
    while True:
        try:
            calificacion = float(input("Calificación: "))
            if 0 <= calificacion <= 5:
                break
            else:
                print("Calificación inválida. Debe estar entre 0 y 5.")
        except ValueError:
            print("Por favor, ingrese un número decimal para la calificación.")

    # Agregar estudiante a la lista
    estudiantes.append({
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion
    })

# Calcular estadísticas
if estudiantes:
    # Inicializar con el primer estudiante
    estudiante_max = estudiantes[0]
    estudiante_min = estudiantes[0]
    suma_calificaciones = 0

    for estudiante in estudiantes:
        suma_calificaciones += estudiante["calificacion"]
        if estudiante["calificacion"] > estudiante_max["calificacion"]:
            estudiante_max = estudiante
        if estudiante["calificacion"] < estudiante_min["calificacion"]:
            estudiante_min = estudiante

    promedio = suma_calificaciones / len(estudiantes)

    # Mostrar resultados
    print("\n" + "="*50)
    print("RESULTADOS:")
    print("="*50)
    print(f"Estudiante con la calificación más alta: {estudiante_max['nombre']} ({estudiante_max['calificacion']})")
    print(f"Estudiante con la calificación más baja: {estudiante_min['nombre']} ({estudiante_min['calificacion']})")
    print(f"Calificación promedio: {promedio:.2f}")
else:
    print("No se registraron estudiantes.")
