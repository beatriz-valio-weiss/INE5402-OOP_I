postos, distancia_maxima = [int(x) for x in input().split()]
posicao_postos = [int(x) for x in input().split()]

for n in range(len(posicao_postos)-1):
    if abs(posicao_postos[n] - posicao_postos[n+1]) <= distancia_maxima:
        atleta_consegue = "S"
    else:
        atleta_consegue = "N"
        break
print(atleta_consegue)