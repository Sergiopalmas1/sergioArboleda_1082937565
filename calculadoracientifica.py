import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): Radio del círculo.
    
    Returns:
        float: Área del círculo redondeada a 2 decimales.
    """
    area = math.pi * (radio ** 2)
    return round(area, 2)

def calcular_hipotenusa(cateto1, cateto2):
    """
    Calcula la hipotenusa de un triángulo rectángulo.
    
    Args:
        cateto1 (float): Longitud del primer cateto.
        cateto2 (float): Longitud del segundo cateto.
    
    Returns:
        float: Longitud de la hipotenusa.
    """
    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    return hipotenusa

def calcular_potencia(base, exponente):
    """
    Calcula la potencia de una base elevada a un exponente.
    
    Args:
        base (float): Base.
        exponente (float): Exponente.
    
    Returns:
        float: Resultado de la potencia.
    """
    return math.pow(base, exponente)

def main():
    """
    Función principal con menú para calcular área de círculo, hipotenusa o potencia.
    """
    while True:
        print("\nMenú:")
        print("1. Calcular área de círculo")
        print("2. Calcular hipotenusa")
        print("3. Calcular potencia")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es {area}")
        elif opcion == "2":
            cateto1 = float(input("Ingresa el primer cateto: "))
            cateto2 = float(input("Ingresa el segundo cateto: "))
            hipotenusa = calcular_hipotenusa(cateto1, cateto2)
            print(f"La hipotenusa es {hipotenusa}")
        elif opcion == "3":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            potencia = calcular_potencia(base, exponente)
            print(f"El resultado de {base} elevado a {exponente} es {potencia}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
