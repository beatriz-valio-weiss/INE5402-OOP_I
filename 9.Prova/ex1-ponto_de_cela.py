# Coleta os dados, montando a matriz
linhas, colunas = [int(x) for (x) in input().split()]
matriz = []
for l in range(linhas):
    matriz.append([int(x) for (x) in input().split()])

# Inicia as listas dos dados a serem verificados
lista_menores_linha = []
lista_maiores_coluna = []
lista_coordenadas = []
saida = []

# Verifica o menor elemento de cada linha e os insere na lista respectiva
for l in range(linhas):
    menor_elemento_linha = float("inf")
    coordenada = []
    for c in range(colunas):
        if matriz[l][c] < menor_elemento_linha:
            menor_elemento_linha = matriz[l][c]
            coordenada = l, c
    lista_menores_linha.append(menor_elemento_linha)
    lista_coordenadas.append(coordenada)

# Verifica o maior elemento de cada coluna e os insere na lista respectiva
for l in range(colunas):
    maior_elemento_coluna = float("-inf")
    for c in range(linhas):
        if matriz[c][l] > maior_elemento_coluna:
            maior_elemento_coluna = matriz[c][l]
    lista_maiores_coluna.append(maior_elemento_coluna)

# Verifica se há elemento comum entre as duas listas (ou seja, cumpre os dois requisitos), retornando a resposta:
    # Coordenada do elemento que é o menor da respectiva linha e o maior da respectiva coluna ou 'False' caso não cumpra os requisitos.
for elemento in range(len(lista_menores_linha)):
    if lista_menores_linha[elemento] in lista_maiores_coluna:
        coordenada = lista_coordenadas[elemento]
        l, c = coordenada
        saida = l + 1, c + 1
        print(*saida)
        break
if saida == []:
    print(False)