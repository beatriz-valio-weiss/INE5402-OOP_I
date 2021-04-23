a = int(input())
b = int(input())

tamanho = abs(a - b) + 1

if a < 0 and b < 0:
    tamanho = abs(a + b) - 1
elif a < 0:
    tamanho = b - a + 1  
elif b < 0:
    tamanho = a - b + 1
    
print(tamanho)