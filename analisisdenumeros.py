def analisis_numeros():
    """Programa que analiza números ingresados por el usuario"""
    
    numeros = []
    suma = 0
    contador = 0
    pares = 0
    impares = 0
    
    print("\n" + "="*50)
    print("ANÁLISIS DE NÚMEROS")
    print("="*50)
    print("Ingresa números (escribe 0 para terminar)")
    print("="*50)
    
    while True:
        try:
            numero = int(input("\nIngresa un número: "))
            
            if numero == 0:
                break
            
            # Agregar número a la lista
            numeros.append(numero)
            contador += 1
            suma += numero
            
            # Contar pares e impares
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        
        except ValueError:
            print("❌ Por favor, ingresa un número entero válido")
    
    # Verificar si se ingresaron números
    if contador == 0:
        print("\n❌ No ingresaste ningún número")
        return
    
    # Calcular promedio
    promedio = suma / contador
    
    # Obtener mayor y menor
    mayor = max(numeros)
    menor = min(numeros)
    
    # Mostrar resultados
    print("\n" + "="*50)
    print("RESULTADOS DEL ANÁLISIS")
    print("="*50)
    print(f"✓ Cantidad total de números: {contador}")
    print(f"✓ Suma de todos: {suma}")
    print(f"✓ Promedio: {promedio:.2f}")
    print(f"✓ Número mayor: {mayor}")
    print(f"✓ Número menor: {menor}")
    print(f"✓ Cantidad de pares: {pares}")
    print(f"✓ Cantidad de impares: {impares}")
    print("="*50)
    
    # Información adicional
    print(f"\nNúmeros ingresados: {numeros}")

if __name__ == "__main__":
    analisis_numeros()