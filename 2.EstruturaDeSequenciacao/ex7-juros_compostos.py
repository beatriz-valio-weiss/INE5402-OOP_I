capital = float(input())
n_meses = int(input())
taxa_escala_0a100 = float(input())

montante = capital*(1 + (taxa_escala_0a100/100))**n_meses

print(round(montante,2))