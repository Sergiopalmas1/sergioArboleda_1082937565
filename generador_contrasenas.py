import random
import string

def generar_contrasena(longitud):
    """Genera una contraseña aleatoria con mayúsculas, minúsculas, números y caracteres especiales"""
    
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiales = "!@#$%"
    
    # Crear lista con todos los caracteres disponibles
    todos_caracteres = mayusculas + minusculas + numeros + especiales
    
    # Garantizar que la contraseña tenga al menos un carácter de cada tipo
    contrasena = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiales)
    ]
    
    # Llenar el resto de la contraseña aleatoriamente
    for _ in range(longitud - 4):
        contrasena.append(random.choice(todos_caracteres))
    
    # Mezclar la contraseña para que no siempre comience igual
    random.shuffle(contrasena)
    
    return ''.join(contrasena)

def validar_longitud(longitud_str):
    """Valida que la longitud sea un número entre 8 y 20"""
    try:
        longitud = int(longitud_str)
        if longitud < 8:
            print("❌ La contraseña debe tener mínimo 8 caracteres")
            return False
        elif longitud > 20:
            print("❌ La contraseña debe tener máximo 20 caracteres")
            return False
        return True
    except ValueError:
        print("❌ Por favor, ingresa un número válido")
        return False

def generador_contrasenas():
    """Programa principal del generador de contraseñas"""
    
    while True:
        print("\n" + "="*50)
        print("GENERADOR DE CONTRASEÑAS SEGURAS")
        print("="*50)
        
        # Pedir longitud de la contraseña
        while True:
            longitud_str = input("\n¿Cuál es la longitud deseada? (8-20): ").strip()
            if validar_longitud(longitud_str):
                longitud = int(longitud_str)
                break
        
        # Generar la contraseña
        contrasena = generar_contrasena(longitud)
        print(f"\n✓ Tu contraseña generada es:")
        print(f"  {contrasena}")
        print(f"\n  Longitud: {len(contrasena)} caracteres")
        
        # Preguntar si desea generar otra
        while True:
            opcion = input("\n¿Deseas generar otra contraseña? (s/n): ").strip().lower()
            if opcion in ["s", "si", "yes"]:
                break
            elif opcion in ["n", "no"]:
                print("\n¡Gracias por usar el generador de contraseñas!")
                return
            else:
                print("❌ Por favor, responde 's' o 'n'")

if __name__ == "__main__":
    generador_contrasenas()