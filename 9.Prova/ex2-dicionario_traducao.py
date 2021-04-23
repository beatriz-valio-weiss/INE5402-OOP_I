# Coleta a quantidade de instancias
qtd_instancias = int(input())

# Para cada instancia T, desenvolve a saida das N linhas
for t in range(qtd_instancias):
    # Coleta as M linhas de traducoes e elabora o dicionario
    qtd_palavras_dic, qtd_linhas_musica = [int(x) for x in input().split()]
    dicionario = {}
    for m in range(qtd_palavras_dic):
        japones = input()
        portugues = input()
        dicionario.update({japones: portugues})
    
    # Coleta as N linhas da letra da musica
    saida = []
    for n in range(qtd_linhas_musica):
        letra_musica = input().split()
        # Para cada palavra na linha da letra da musica, analisa se consta no dicionario:
            # Se constar, soma na traducao a letra em portugues, se não, soma na traducao a letra em japones
        traducao = ''
        for palavra in range(len(letra_musica)):
            if letra_musica[palavra] in dicionario:
                traducao += dicionario[letra_musica[palavra]] + ' '
            else:
                traducao += letra_musica[palavra] + ' '
        # Corrige a traducao com os criterios 'letras todas minusculas' e 'frase sem espacos antes ou depois'
        traducao = traducao.lower()
        traducao = traducao.strip()
        # Alimenta a lista de saida com as traducoes de cada linha
        saida.append(traducao)
    # Para cada instancia T, imprime as N linhas traduzidas guardadas na lista de saida
    for n in range(qtd_linhas_musica):
        print(saida[n])
    # Imprime uma linha em branco após tradução, inclusive após a última
    print()