# Programa para verificar se o número é divisível por 3 ou 5
print("--- Número divisível por 3 ou 5 ---")
numero = int(input("Escolha um número: "))
tres = 3
cinco = 5

if numero % tres == 0:
    print(f"{numero} é divisível por {tres}")
    if numero % cinco == 0:
        print(f"{numero} é divísível por {cinco}")
elif numero % cinco == 0:
    print(f"{numero} é divísível por {cinco}")
else:
    print("Este número não é divisível por nem por 5 nem por 3.")