venda = float(input("Digite o valor da venda: R$"))

if venda >= 100000:
    comissao = 700.00 + 0.16
    total = venda + comissao
    print(f"Comissão: R${total:.2f}")
elif venda >= 80000:
    comissao = 650.00 + 0.14
    total = venda + comissao
    print(f"Comissão: R${total:.2f}")
elif venda >= 60000:
    comissao = 600.00 + 0.14
    total = venda + comissao
    print(f"Comissão: R${total:.2f}")
elif venda >= 40000:
    comissao = 550.00 + 0.14
    total = venda + comissao
    print(f"Comissão: R${total:.2f}")
elif venda >= 20000:
    comissao = 500.00 + 0.14
    total = venda + comissao
    print(f"Comissão: R${total:.2f}")
else:
    comissao = 400.00 + 0.14
    total = venda + comissao
    print(f"Comissão: R${total:.2f}")