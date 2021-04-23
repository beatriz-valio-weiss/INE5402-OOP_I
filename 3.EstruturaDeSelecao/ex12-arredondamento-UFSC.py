nota = float(input())

resto = nota % 1

if resto < 0.25:
    arredondamento = 0
elif resto == 0.25 or resto < 0.75:
    arredondamento = 0.5
elif resto >= 0.75:
    arredondamento = 1

nota_arredondada = nota - resto + arredondamento

print(nota_arredondada)