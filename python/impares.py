# Programa para somar numeros impares em um intervalo definido pelo usuário

inicio = int(input("Digite um valor inicial: "))
final = int(input("Digite um valor final: "))

if inicio > final:
    print("❌ Erro! Intervalo de valores inválidos.")
else:
    soma = sum(range(inicio, final, 2))
    print(f"A soma é: {soma}")