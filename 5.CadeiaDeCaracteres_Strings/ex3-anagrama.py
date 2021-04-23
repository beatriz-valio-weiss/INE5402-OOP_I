palavra_1 = input()
palavra_2 = input()

eh_anagrama = True

if palavra_1 == palavra_2 or len(palavra_1) != len (palavra_2):
    eh_anagrama = False
else:  
    for letra in palavra_1:
        if palavra_1.count(letra) != palavra_2.count(letra):
            eh_anagrama = False
            break

print(eh_anagrama)