import math

numero = float(input("Digite um número positivo (0 ou negativo para sair): "))

while numero > 0:
    quadrado = numero * numero
    cubo = numero ** 3
    raiz = math.sqrt(numero)
    print(f"Número: {numero}")
    print(f"Quadrado: {quadrado}")
    print(f"Cubo: {cubo}")
    print(f"Raiz Quadrada: {raiz:.2f}")

    numero = float(input("Digite um número positivo (0 ou negativo para sair): "))

print("\nPrograma encerrado.")