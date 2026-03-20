def cajero_automatico():
    saldo = 1000
    
    while True:
        print("\n" + "="*40)
        print("CAJERO AUTOMÁTICO")
        print("="*40)
        print(f"Saldo actual: ${saldo:.2f}")
        print("\n1. Ver saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        print("="*40)
        
        opcion = input("\nElige una opción (1-4): ").strip()
        
        if opcion == "1":
            print(f"\n✓ Tu saldo es: ${saldo:.2f}")
        
        elif opcion == "2":
            try:
                monto = float(input("\n¿Cuánto dinero deseas depositar? $"))
                if monto <= 0:
                    print("❌ El monto debe ser mayor a $0")
                else:
                    saldo += monto
                    print(f"✓ Depósito exitoso. Tu nuevo saldo es: ${saldo:.2f}")
            except ValueError:
                print("❌ Por favor, ingresa un valor numérico válido")
        
        elif opcion == "3":
            try:
                monto = float(input("\n¿Cuánto dinero deseas retirar? $"))
                if monto <= 0:
                    print("❌ El monto debe ser mayor a $0")
                elif monto > saldo:
                    print(f"❌ No tienes suficiente saldo. Tu saldo es: ${saldo:.2f}")
                else:
                    saldo -= monto
                    print(f"✓ Retiro exitoso. Tu nuevo saldo es: ${saldo:.2f}")
            except ValueError:
                print("❌ Por favor, ingresa un valor numérico válido")
        
        elif opcion == "4":
            print("\n¡Gracias por usar el cajero automático!")
            print(f"Saldo final: ${saldo:.2f}")
            break
        
        else:
            print("❌ Opción inválida. Por favor, elige una opción entre 1 y 4")

if __name__ == "__main__":
    cajero_automatico()