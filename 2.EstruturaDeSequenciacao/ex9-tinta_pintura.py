# Galão de tinta de 3,6litros, 25reais, 1l cobre área de 18m²
area_cobertura = int(input())

galao_cobre = 3.6 * 18
n_galao = max(round(area_cobertura / galao_cobre),1)
valor_total = n_galao*25

print("- área de cobertura: {}".format(area_cobertura))
print("- número de galões: {}".format(n_galao))
print("- valor a ser pago: R$ {:.2f}".format(valor_total))