import datetime

def crear_evento(nombre, dia, mes, ano):
    """
    Crea un evento con nombre y fecha.
    
    Args:
        nombre (str): Nombre del evento.
        dia (int): Día del evento.
        mes (int): Mes del evento.
        ano (int): Año del evento.
    
    Returns:
        dict: Diccionario con nombre y fecha.
    """
    fecha = datetime.date(ano, mes, dia)
    return {"nombre": nombre, "fecha": fecha}

def dias_hasta_evento(fecha_evento):
    """
    Calcula los días hasta el evento desde hoy.
    
    Args:
        fecha_evento (datetime.date): Fecha del evento.
    
    Returns:
        int: Número de días (positivo si futuro, negativo si pasado).
    """
    hoy = datetime.date.today()
    diferencia = fecha_evento - hoy
    return diferencia.days

def evento_pasado(fecha_evento):
    """
    Verifica si el evento ya pasó.
    
    Args:
        fecha_evento (datetime.date): Fecha del evento.
    
    Returns:
        bool: True si ya pasó, False si no.
    """
    hoy = datetime.date.today()
    return fecha_evento < hoy

def main():
    """
    Función principal que solicita datos, crea el evento y muestra información.
    """
    nombre = input("Ingresa el nombre del evento: ")
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    ano = int(input("Ingresa el año: "))
    
    evento = crear_evento(nombre, dia, mes, ano)
    fecha_evento = evento["fecha"]
    
    if evento_pasado(fecha_evento):
        dias = abs(dias_hasta_evento(fecha_evento))
        print(f"El evento ya pasó. Fue hace {dias} días.")
    else:
        dias = dias_hasta_evento(fecha_evento)
        print(f"Faltan {dias} días para tu evento.")

if __name__ == "__main__":
    main()