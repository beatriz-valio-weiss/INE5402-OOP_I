consumo_kWh = int(input())

# Tarifas kWh cheios
tarifa_30 = 30 * 0.09556
tarifa_100 = 70 * 0.16698
tarifa_200 = 100 * 0.25052

if consumo_kWh <= 30:
    valor_energia = consumo_kWh * 0.09556
elif consumo_kWh <= 100:
    valor_energia = tarifa_30 + (consumo_kWh - 30) * 0.16698
elif consumo_kWh <= 200:
    valor_energia = tarifa_30 + tarifa_100 + (consumo_kWh - 100) * 0.25052
else:
    valor_energia = tarifa_30 + tarifa_100 + tarifa_200 + \
    (consumo_kWh - 200) * 0.27836
    
print("{:.2f}".format(round(valor_energia,2)))