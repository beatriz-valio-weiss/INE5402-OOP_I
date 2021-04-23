qtd_praias = int(input())

praia_a, distancia_a = input().split(';')
distancia_a = int(distancia_a)

soma_distancias = distancia_a
nome_praia = praia_a
if distancia_a <= 20 and distancia_a >= 15:
    qtd_perto_centro = 1
else:
    qtd_perto_centro = 0

praia_referencia = 0

if qtd_praias > 1:
    for qtd in range (qtd_praias - 1):
        praia_b, distancia_b = input().split(';')
        distancia_b = int(distancia_b)
        soma_distancias += distancia_b
        if distancia_b <= 20 and distancia_b >= 15:
            qtd_perto_centro += 1
        praia_mais_distante = max(distancia_a, distancia_b, praia_referencia)
        praia_referencia = praia_mais_distante
        if praia_referencia == distancia_b:
            nome_praia = praia_b
        praia_a = praia_b
        distancia_a = distancia_b


media = soma_distancias / qtd_praias

print("{};{};{:.1f}".format(nome_praia, qtd_perto_centro, round(media,1)))

'''
praia_referencia = max(praia_mais_distante, praia_referencia)
        if praia_referencia == distancia_a:
            nome_praia = praia_a
        elif praia_referencia == distancia_b:
            nome_praia = praia_b
        
for q in range (qtd_praias):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    if distancia <= 20 and 15 <= distancia:
        qtd_perto_centro += 1
    else:
        qtd_perto_centro += 0
    soma_distancias += distancia
    praia_mais_distante = max(distancia_1, distancia)
    if praia_mais_distante == distancia_1:
        nome_praia = praia_1
    elif praia_mais_distante == distancia:
        nome_praia = praia
    praia_1 = praia
    distancia_1 = distancia
'''