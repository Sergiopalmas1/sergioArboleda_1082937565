def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    
    Args:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.
    
    Returns:
        float: IMC redondeado a 2 decimales.
    """
    imc = peso / (altura ** 2)
    return round(imc, 2)

def clasificar_imc(imc):
    """
    Clasifica el IMC según las categorías estándar.
    
    Args:
        imc (float): Valor del IMC.
    
    Returns:
        str: Clasificación del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    """
    Función principal que solicita datos al usuario, calcula el IMC y muestra la clasificación.
    """
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)
    print(f"Tu IMC es {imc} y tu clasificación es: {clasificacion}")

if __name__ == "__main__":
    main()
