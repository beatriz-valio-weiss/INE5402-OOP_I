import math

tamanho_sequencia = int(input())

menor = float("inf")
segundo_menor = float("inf")

for sequencia in range (tamanho_sequencia):
    valor = int(input())
    if valor < menor:
        segundo_menor = menor
        menor = valor
    elif valor < segundo_menor:
        segundo_menor = valor
        
print(segundo_menor)




'''tamanho_sequencia = int(input())
primeiro_valor = int(input())

if tamanho_sequencia == 1:
    print(primeiro_valor)
else:
    for sequencia in range (tamanho_sequencia - 1):
        proximo_valor = int(input())
        menor_valor = min(proximo_valor, primeiro_valor)
        primeiro_valor = menor_valor

print(menor_valor)'''