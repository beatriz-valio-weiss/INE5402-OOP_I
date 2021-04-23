valores_romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
numero_romano = input()

numero_decimal = 0

for n in range(len(numero_romano)-1):
    valor_decimal = numero_romano[n]
    valor_decimal_seguinte = numero_romano[n + 1]
    if valores_romanos[valor_decimal] >= valores_romanos[valor_decimal_seguinte]:
        numero_decimal += valores_romanos[valor_decimal]
    else:
        numero_decimal -= valores_romanos[valor_decimal]
numero_decimal += valores_romanos[numero_romano[-1]]

print(numero_decimal)