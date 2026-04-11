salario = float(input("Digite o salário: R$"))
valor_prestacao = float(input("Digite o valor da prestação: R$"))

limite_prestacao = salario * 0.20

if valor_prestacao > limite_prestacao:
    print(f"Empréstimo não concedido. O valor da prestação excede 20% do valor.")
else:
    print(f"Empréstimo concedido. A prestação é de R${valor_prestacao:.2f}")