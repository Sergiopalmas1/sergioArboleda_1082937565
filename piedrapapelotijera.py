import random

def piedra_papel_tijera():
    """Juego de piedra, papel o tijera con contador de puntuación"""
    
    opciones = ["piedra", "papel", "tijera"]
    victorias_usuario = 0
    victorias_maquina = 0
    
    print("\n" + "="*50)
    print("JUEGO: PIEDRA, PAPEL O TIJERA")
    print("="*50)
    print("Reglas:")
    print("  • Piedra gana a Tijera")
    print("  • Tijera gana a Papel")
    print("  • Papel gana a Piedra")
    print("="*50)
    
    while True:
        print(f"\nPuntuación - Tú: {victorias_usuario} | Máquina: {victorias_maquina}")
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Ver puntuación final y salir")
        
        opcion_usuario = input("\nTu elección (1-4): ").strip()
        
        if opcion_usuario == "4":
            print("\n" + "="*50)
            print("JUEGO FINALIZADO")
            print("="*50)
            print(f"Victorias tuyas: {victorias_usuario}")
            print(f"Victorias máquina: {victorias_maquina}")
            
            if victorias_usuario > victorias_maquina:
                print(f"\n🎉 ¡GANASTE! Diferencia: {victorias_usuario - victorias_maquina}")
            elif victorias_maquina > victorias_usuario:
                print(f"\n😔 Perdiste. Diferencia: {victorias_maquina - victorias_usuario}")
            else:
                print("\n🤝 ¡Fue un empate!")
            print("="*50)
            break
        
        elif opcion_usuario not in ["1", "2", "3"]:
            print("❌ Opción inválida. Por favor, elige 1, 2, 3 o 4")
            continue
        
        # Convertir número a opción
        opcion_nombres = {"1": "piedra", "2": "papel", "3": "tijera"}
        eleccion_usuario = opcion_nombres[opcion_usuario]
        
        # Máquina elige al azar
        eleccion_maquina = random.choice(opciones)
        
        # Mostrar elecciones
        print(f"\n▶ Tú elegiste: {eleccion_usuario.upper()}")
        print(f"▶ Máquina eligió: {eleccion_maquina.upper()}")
        
        # Determinar ganador
        if eleccion_usuario == eleccion_maquina:
            print("\n🤝 ¡EMPATE!")
        
        elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
             (eleccion_usuario == "tijera" and eleccion_maquina == "papel") or \
             (eleccion_usuario == "papel" and eleccion_maquina == "piedra"):
            print("\n✓ ¡GANASTE!")
            victorias_usuario += 1
        
        else:
            print("\n✗ Perdiste esta ronda")
            victorias_maquina += 1

if __name__ == "__main__":
    piedra_papel_tijera()