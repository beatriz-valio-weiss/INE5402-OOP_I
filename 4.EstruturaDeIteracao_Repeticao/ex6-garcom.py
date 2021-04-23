Num_bandejas = int(input())

qtd_copos_quebrados = 0

for N in range(Num_bandejas):
    latas, copos = [int(w) for w in input().split()]
    if latas > copos:
        qtd_copos_quebrados += copos
        
print(qtd_copos_quebrados)