preco = float(input("Digite o seu salário: R$"))
estado = input("Digite o estado (MG, SP, RJ, MS): ").upper()

if estado == "MG":
    imposto = preco * 0.07
    total = preco + imposto
    print(f"Valor total (Minas Gerais): R${total:.2f}")
elif estado == "SP":
    imposto = preco * 0.12
    total = preco + imposto
    print(f"Valor total (São Paulo): R${total:.2f}")
elif estado == "RJ":
    imposto = preco * 0.15
    total = preco + imposto
    print(f"Valor total (Rio de Janeiro): R${total:.2f}")
elif estado == "MS":
    imposto = preco * 0.08
    total = preco + imposto
    print(f"Valor total (Mato Grosso do Sul): R${total:.2f}")
else:
    print("❌ Erro! Estado inválido.")