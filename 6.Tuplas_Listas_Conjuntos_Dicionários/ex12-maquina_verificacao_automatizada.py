pontos_conector_um = [int(x) for x in input().split()]
pontos_conector_dois = [int(x) for x in input().split()]

compatibilidade = 'Y'
for a in range(len(pontos_conector_um)):
    if pontos_conector_um[a] == pontos_conector_dois[a]:
        compatibilidade = 'N'
        break
print(compatibilidade)