# Medidas Conteineres e Navio
a, b, c = [int(conteiner) for conteiner in input().split()]
x, y, z = [int(navio) for navio in input().split()]

# Calculos
largura = x // a
comprimento = y // b
altura = z // c

qtd_conteineres = largura * comprimento * altura

print(qtd_conteineres)