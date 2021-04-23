salario_bruto = float(input())

if salario_bruto <= 720:
    inss = 765 / 10000 * salario_bruto
elif salario_bruto <= 1200:
    inss = 9 / 100 * salario_bruto
elif salario_bruto <= 2400:
    inss = 11 / 100 * salario_bruto
elif salario_bruto > 2400:
    inss = 11 / 100 * 2400

print("{:.2f}".format(inss))