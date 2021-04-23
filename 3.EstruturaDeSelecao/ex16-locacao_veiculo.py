qtd_dias = int(input())
km_rodados = float(input())

custo_fixo = 45.00
custo_km_extra = 0.50
cortesia_diaria_km = 60

preco_diaria = qtd_dias * custo_fixo

kms_extras = km_rodados - cortesia_diaria_km * qtd_dias

if kms_extras > 0:
    preco_total = preco_diaria + custo_km_extra * kms_extras
else:
    preco_total = preco_diaria

print("{:.2f}".format(round(preco_total,1)))