tamanho_sequencia = int(input())
primeiro_valor = float(input())

if tamanho_sequencia == 1:
    print(primeiro_valor)
else:
    for sequencia in range (tamanho_sequencia - 1):
        proximo_valor = float(input())
        menor_valor = min(proximo_valor, primeiro_valor)
        primeiro_valor = menor_valor
    print(menor_valor)
