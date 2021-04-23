print("Consumo médio de combustível gasto")

distancia = int(input("Quantos quilometros foram percorridos?"))
combustivel = float(input("Quantos litros de combustível foram gastos?"))

consumo = distancia / combustivel

print("O consumo médio de combustível foi de {} Km/l".format(round(consumo,3)))