salario_atual = float(input())
valor_salario_minimo = float(input())

qtd_salario_minimo = salario_atual / valor_salario_minimo

if qtd_salario_minimo <= 3:
    reajuste_salario = salario_atual * 20 / 100
elif qtd_salario_minimo <= 5:
    reajuste_salario = salario_atual * 15 / 100
elif qtd_salario_minimo > 5:
    reajuste_salario = salario_atual * 10 / 100

salario_ajustado = salario_atual + reajuste_salario

if salario_ajustado < 1.5 * valor_salario_minimo:
    novo_salario = 1.5 * valor_salario_minimo
elif salario_ajustado <= 20 * valor_salario_minimo:
    novo_salario = salario_ajustado
elif salario_ajustado > 20 * valor_salario_minimo:
    novo_salario = 20 * valor_salario_minimo

print("{:.2f}".format(novo_salario))