num_competidores, qtd_total_folhas, qtd_folhas_competidor = [int(folhas) for folhas in input().split()]

qtd_folhas = qtd_total_folhas / (qtd_folhas_competidor * num_competidores)

if qtd_folhas >= 1:
    print("S")
else:
    print("N")