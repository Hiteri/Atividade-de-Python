print("=== CÁLCULO DE CONSUMO DE COMBUSTÍVEL ===")
quilometro = float(input("Quilômetros rodados: "))
litro = float(input("Litros abastecidos: "))
calculo = quilometro / litro

if calculo < 8:
    print(f"Consumo total: {calculo:.2f} km/l")
    print("Venda o carro!")
elif 8 <= calculo < 12:
    print(f"Consumo total: {calculo:.2f} km/l")
    print("Econômico!")
else:
    print(f"Consumo total: {calculo:.2f} km/l")
    print("Super econômico!")