numero = int(input())

fatorial = 1

while numero != 1 and numero!= 0:
    fatorial *= numero * (numero-1)
    numero -= 2
    
print(fatorial)