num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    diferenca = num1 - num2
    print(f"{num1} é maior que {num2}\nDiferença: {diferenca}")
else:
    diferenca = num2 - num1
    print(f"{num2} é maior que {num1}\nDiferença: {diferenca}")