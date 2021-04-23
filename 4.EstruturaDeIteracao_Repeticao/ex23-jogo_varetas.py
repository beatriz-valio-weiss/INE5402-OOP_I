numero_varetas = int(input())
qtd_lados = 0

while numero_varetas > 0:
    for n in range(numero_varetas):
        comprimento_varetas, qtd_varetas = [int(w) for w in input().split()]
        qtd_lados += qtd_varetas // 2
    print(qtd_lados // 2)
    qtd_lados = 0
    numero_varetas = int(input())