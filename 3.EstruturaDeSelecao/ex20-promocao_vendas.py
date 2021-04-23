compra_cliente = float(input())

if compra_cliente > 1000.00:
    desconto = compra_cliente * (20 / 100 + 10 / 100) + (compra_cliente - 1000) * 15 / 100
elif compra_cliente >= 500.00:
    desconto = compra_cliente * (20 / 100 + 10 / 100)
else:
    desconto = compra_cliente * 20 / 100
    
valor_promocional = compra_cliente - desconto

print("{:.2f}".format(valor_promocional))