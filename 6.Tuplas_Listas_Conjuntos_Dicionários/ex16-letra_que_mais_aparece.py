frase = input().lower()
contador_letras = dict()

maior_ocorrencia = -1
letra_mais_aparece = ''

for letra in frase:
    if letra != ' ':
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
            
for letra, qtd in contador_letras.items():
    if qtd > maior_ocorrencia:
        maior_ocorrencia = qtd
        letra_mais_aparece = letra

print(letra_mais_aparece)