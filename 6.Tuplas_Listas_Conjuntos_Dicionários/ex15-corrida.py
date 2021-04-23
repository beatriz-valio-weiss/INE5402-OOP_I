qtd_carros, qtd_voltas = [int(x) for x in input().split()]

tempo_carros = []
for a in range(qtd_carros):
    tempo_carros.append(sum([int(x) for x in input().split()]))

ordem_carros = sorted(tempo_carros)

for i in range(len(tempo_carros)):
    if ordem_carros[0] == tempo_carros[i]:
        print(i+1)
for i in range(len(tempo_carros)):
    if ordem_carros[1] == tempo_carros[i]:
        print(i+1)
for i in range(len(tempo_carros)):
    if ordem_carros[2] == tempo_carros[i]:
        print(i+1)