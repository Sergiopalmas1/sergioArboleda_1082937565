# Programa que pide 10 números al usuario, cuenta cuántos son pares e impares
# y muestra los contadores.

def main():
    pares = 0
    impares = 0

    for i in range(10):
        while True:
            try:
                valor = int(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número entero.")

        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")


if __name__ == "__main__":
    main()