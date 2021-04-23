frase = input()

while frase != "*":
    lista = sorted(frase.split())
    letras_iniciais = ''
    eh_tautograma = "Y"
    for palavra in (lista):
        letras_iniciais =  letras_iniciais + palavra[0] + " "
    letras_iniciais = letras_iniciais.lower()
    iniciais = sorted(letras_iniciais.split())
    for i in iniciais:
        if iniciais.count(i) != len(iniciais):
            eh_tautograma = "N"
            break
        else:
            break
    print(eh_tautograma)
    frase = input()