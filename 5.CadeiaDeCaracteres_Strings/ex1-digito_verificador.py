numero = input()

digito_verificador = int(numero[-1])

soma_ponderada = 0
ponderamento = len(numero)

for digito in range(len(numero)-1):
    soma_ponderada += int(numero[digito]) * ponderamento
    ponderamento -= 1

resto_divisao_11 = soma_ponderada % 11

digito_verificador_calculado = 11 - resto_divisao_11
if digito_verificador_calculado >= 10:
    digito_verificador_calculado = 0

print(digito_verificador == digito_verificador_calculado)