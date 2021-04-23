A, B, C = [int(receita) for receita in input().split()]

qtd_bolo = min(A//2, B//3, C//5)

print(qtd_bolo)