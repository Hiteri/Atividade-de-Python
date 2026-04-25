idade = int(input("Digite a sua idade: "))
tempo_de_servico = int(input("Tempo de serviço: "))
if idade >= 65 or tempo_de_servico >= 30:
    print("Você pode se aposentar.")
elif idade >= 60 and tempo_de_servico >= 25:
    print("Você pode se aposentar com pelo menos 60 anos e trabalhando por pelo menos 25 anos.")
else:
    print("Erro! Você ainda não tem idade ou tempo de serviço para se aposentar.")