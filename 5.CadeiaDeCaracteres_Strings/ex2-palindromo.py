frase = input()
frase_limpa = ''

for letra in frase.lower():
    if letra.isalpha():
        frase_limpa += letra

suposto_palindromo = frase_limpa[::-1]

print(frase_limpa == suposto_palindromo)