n_perguntas, n_referencia = [int(x) for x in input().split()]

while n_perguntas != 0 and n_referencia != 0:
    perguntas = [int(x) for x in input().split()]
    contador_perguntas = dict()
    for n in (perguntas):
        if n in contador_perguntas:
            contador_perguntas[n] += 1
        else:
            contador_perguntas[n] = 1
    perguntas_adicionadas = 0
    for pergunta, qtd in contador_perguntas.items():
        if qtd >= n_referencia:
            perguntas_adicionadas += 1
    print(perguntas_adicionadas)
    n_perguntas, n_referencia = [int(x) for x in input().split()]