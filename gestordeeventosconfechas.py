import datetime

def crear_evento(nombre, dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    evento = {"nombre": nombre, "fecha": fecha}
    return evento


def dias_hasta_evento(fecha_evento):
    hoy = datetime.date.today()
    diferencia = fecha_evento - hoy
    return diferencia.days


def evento_pasado(fecha_evento):
    hoy = datetime.date.today()
    return fecha_evento < hoy


def main():
    nombre = input("Ingresa el nombre del evento: ")
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))

    evento = crear_evento(nombre, dia, mes, año)

    dias = dias_hasta_evento(evento["fecha"])

    if evento_pasado(evento["fecha"]):
        print(f"El evento ya pasó. Fue hace {abs(dias)} días.")
    elif dias == 0:
        print("¡El evento es hoy!")
    else:
        print(f"Faltan {dias} días para tu evento.")


if __name__ == "__main__":
    main()