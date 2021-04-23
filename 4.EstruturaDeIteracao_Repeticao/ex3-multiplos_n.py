# Valores multiplos de n em relação ao intervalo m
n = int(input())
m = int(input())

for teste_multiplo in range(1, m+1):
    if teste_multiplo % n == 0:
        print (teste_multiplo, end=' ')