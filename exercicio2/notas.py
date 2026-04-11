n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 * 1 + n2 * 1 + n3 * 2) / 4
print(f"Média da prova: {media:.2f}")

if media >= 60:
    print("Aprovado")
else:
    print("Reprovado")