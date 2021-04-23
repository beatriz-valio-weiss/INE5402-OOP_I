# Tempo de trabalho
horas_normais = int(input())
horas_extras = int(input())

# Valores do Salário
normal = 2500/200
extra = normal*1.2

# Calculos
salario_bruto = horas_normais*normal + horas_extras*extra
imposto_de_renda = salario_bruto*13/100
seguridade_social = salario_bruto*9/100
salario_liquido = salario_bruto - imposto_de_renda - seguridade_social

# Impressões
print("- Salário Bruto : R$ {:.2f}".format(salario_bruto))
print("- IR (13%) : R$ {:.2f}".format(imposto_de_renda))
print("- INSS (9%) : R$ {:.2f}".format(seguridade_social))
print("- Salário Líquido : R$ {:.2f}".format(salario_liquido))