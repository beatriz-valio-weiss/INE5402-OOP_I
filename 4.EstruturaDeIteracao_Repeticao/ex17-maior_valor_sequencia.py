tamanho_sequencia = int(input())
primeiro_valor = int(input())
posicao = 1

if tamanho_sequencia == 1:
    print(primeiro_valor, tamanho_sequencia)
else:
    for sequencia in range (2, tamanho_sequencia + 1):
        proximo_valor = int(input())
        maior_valor = max(proximo_valor, primeiro_valor)
        if maior_valor == proximo_valor:
            posicao = sequencia
        primeiro_valor = maior_valor


print(maior_valor, posicao)