numero = int(input())
resto = 0

while numero % 2 == 0:
    resto += numero / 2
    numero -= resto

while numero % 3 == 0:
    resto += numero / 3
    numero -= resto
    
while numero % 5 == 0:
    resto += numero // 5
    numero -= resto

if resto == 0:
    print(False)
else:
    print(True)