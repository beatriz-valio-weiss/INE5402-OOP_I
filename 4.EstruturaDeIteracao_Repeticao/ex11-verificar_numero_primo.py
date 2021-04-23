numero = int(input())
divisores_possiveis = 0

for tentativa in range (1, numero+1):
    if numero % tentativa == 0:
        divisores_possiveis += 1
    else:
        divisores_possiveis += 0
        
if divisores_possiveis == 2:
    print(True)
else:
    print(False)