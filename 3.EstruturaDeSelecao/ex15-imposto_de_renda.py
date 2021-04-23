salario_bruto = float(input())
numero_dependentes = int(input())

desconto_dependentes = numero_dependentes * 137.99

if salario_bruto <= 720.00:
    INSS = salario_bruto * 765 / 10000
elif salario_bruto <= 1200.00:
    INSS = salario_bruto * 9 / 100
elif salario_bruto <= 2400.00:
    INSS = salario_bruto * 11 / 100
elif salario_bruto > 2400.00:
    INSS = 2400.00 * 11 / 100

if salario_bruto <= 1372.81:
    aliquota = 0
    deducao = 0.00
elif salario_bruto <= 2743.25:
    aliquota = 15 / 100
    deducao = 205.92
elif salario_bruto > 2743.25:
    aliquota = 275 / 1000
    deducao = 548.82

IRRF = (salario_bruto - desconto_dependentes - INSS) * aliquota - deducao

if IRRF < 0:
    IRRF = 0
else:
    IRRF = IRRF
    
print("{:.2f}".format(IRRF))