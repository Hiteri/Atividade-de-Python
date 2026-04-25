print("===== CARDÁPIO ======")
codigo = int(input("Digite um código para selecionar: (101, 102, 103, 104, 105, 106): "))


if codigo == 100:
    print("Cachorro-quente")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    hotdog = 1.20 * quantidade
    print(f"Valor total: R${hotdog:.2f}")
elif codigo == 101:
    print("Bauru simples")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    bauru = 1.30 * quantidade
    print(f"Valor total: R${bauru:.2f}")
elif codigo == 102:
    print("Bauru com ovo")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    bauru_com_ovo = 1.50 * quantidade
    print(f"Valor total: R${bauru_com_ovo:.2f}")
elif codigo == 103:
    print("Hamburguer")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    hamburguer = 1.20 * quantidade
    print(f"Valor total: {hamburguer:.2f}")
elif codigo == 104:
    print("Cheeseburguer")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    cheeseburguer = 1.70 * quantidade
    print(f"Valor total: {cheeseburguer:.2f}")
elif codigo == 105:
    print("Suco")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    suco = 2.20 * quantidade
    print(f"Valor total: {suco:.2f}")
elif codigo == 106:
    print("Refrigerante")
    quantidade = int(input("Digite a quantidade do cardápio: "))
    refrigerante = 1.00 * quantidade
    print(f"Valor total: {refrigerante:.2f}")
else:
    print("❌ Erro! Código inválido.")