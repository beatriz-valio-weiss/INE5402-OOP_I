# Especificações da mesa
comprimento = float(input())
largura = float(input())
qtd_gavetas = int(input())
tipo_madeira = input()

superficie = comprimento * largura

# Valores da mesa
valor_minimo = 200.00
valor_metro_quadrado = 100.00
acrescimo_metro_quadrado = 50.00
valor_gaveta = 30.00
valor_mogno = 150.00
valor_carvalho = 125.00

# Preço superficie
if superficie > 2:
    preco_superficie = superficie * valor_metro_quadrado + acrescimo_metro_quadrado
else:
    preco_superficie = superficie * valor_metro_quadrado

# Preço pela quantidade de gavetas
preco_gaveta = valor_gaveta * qtd_gavetas

# Preço pelo tipo de madeira
if tipo_madeira == "mogno":
    preco_madeira = valor_mogno
elif tipo_madeira == "carvalho":
    preco_madeira = valor_carvalho
elif tipo_madeira != "mogno" and tipo_madeira != "carvalho":
    preco_madeira = 0.00

# Preço total da mesa
preco_da_mesa = preco_superficie + preco_gaveta + preco_madeira

# Preço final
if preco_da_mesa <= 200:
    preco_final = 200
else:
    preco_final = preco_da_mesa

print("{:.1f}".format(round(preco_final,2)))