soma = 0
quantidade = 0
num = int(input("Digite um número (Digite 0 para sair): "))

if num != 0:
    maior = num
    menor = num

while num != 0:
    soma += num
    quantidade += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num 
    num = int(input("Digite um número (Digite 0 para sair): "))

if quantidade > 0:
    media = soma / quantidade
    print(f"\nSoma dos números: {soma}")
    print(f"Quantidade de números: {quantidade}")
    print(f"Média dos números: {media:.2f}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
else:
    print("Nenhum número foi digitado.")