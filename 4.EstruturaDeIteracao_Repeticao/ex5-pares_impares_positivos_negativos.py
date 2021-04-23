valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())
valor_4 = int(input())
valor_5 = int(input())

qtd_pares = 0
qtd_impares = 0
qtd_positivos = 0
qtd_negativos = 0

for testes in [valor_1, valor_2, valor_3, valor_4, valor_5]:
    if testes % 2 == 0:
        contagem_par = 1
        contagem_impar = 0
    else:
        contagem_par = 0
        contagem_impar = 1
    qtd_pares += contagem_par
    qtd_impares += contagem_impar
    if testes > 0:
        contagem_positivo = 1
        contagem_negativo = 0
    elif testes < 0:
        contagem_positivo = 0
        contagem_negativo = 1
    else:
        contagem_positivo = 0
        contagem_negativo = 0
    qtd_positivos += contagem_positivo
    qtd_negativos += contagem_negativo


print(qtd_pares, " valor(es) par(es)")
print(qtd_impares, " valor(es) impar(es)")
print(qtd_positivos, " valor(es) positivo(s)")
print(qtd_negativos, " valor(es) negativo(s)")