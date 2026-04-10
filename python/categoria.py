print("=== Verificação de Categoria ===")
idade = int(input("Digite a sua idade: "))

if idade == 5 and idade <= 7:
    categoria = "Infantil A"
    print(categoria)
elif idade == 8 and idade <= 10:
    categoria = "Infantil B"
    print(categoria)
elif idade == 11 and idade <= 13:
    categoria = "Juvenil A"
    print(categoria)
elif idade == 14 and idade <= 17:
    categoria = "Juvenil B"
    print(categoria)
elif idade >= 18:
    categoria = "Senior"
    print(categoria)
else:
    print("🚩 Você não tem idade o suficiente para participar.")