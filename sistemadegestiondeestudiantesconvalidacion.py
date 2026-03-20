import re

def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10


def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def validar_calificaciones(calificaciones):
    for nota in calificaciones:
        if nota < 0 or nota > 5:
            return False
    return True


def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return round(promedio, 2)


def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None

    promedio = calcular_promedio(calificaciones)

    estudiante = {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }

    return estudiante


def listar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\nCédula      | Nombre           | Promedio | Desempeño")
    print("-" * 55)

    for est in lista_estudiantes:
        desempeño = clasificar_desempeño(est["promedio"])
        print(f"{est['cedula']:10} | {est['nombre']:15} | {est['promedio']:8} | {desempeño}")


def main():
    estudiantes = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")

            calificaciones_input = input("Calificaciones (separadas por coma): ")

            try:
                calificaciones = [float(n) for n in calificaciones_input.split(",")]
            except:
                print("Error en el formato de calificaciones.")
                continue

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante is None:
                print("Datos inválidos. No se pudo crear el estudiante.")
            else:
                estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print(f"Estudiante agregado exitosamente. Promedio: {estudiante['promedio']} | Desempeño: {desempeño}")

        elif opcion == "2":
            listar_estudiantes(estudiantes)

        elif opcion == "3":
            cedula_buscar = input("Cédula a buscar: ")
            encontrado = False

            for est in estudiantes:
                if est["cedula"] == cedula_buscar:
                    desempeño = clasificar_desempeño(est["promedio"])
                    print(f"{est['nombre']} | Promedio: {est['promedio']} | Desempeño: {desempeño}")
                    encontrado = True
                    break

            if not encontrado:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()