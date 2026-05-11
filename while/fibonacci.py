limite = int(input("Digite o número limite superior: "))

a, b = 0, 1

print(f"Sequência de Fibonacci até {limite}:")

while a <= limite:
    print(a, end=" ")
    a, b = b, a + b

print(a)