decimal = int(input())

binario = ''

if decimal == 0:
    binario = 0
else:
    while decimal != 1:
        if decimal % 2 == 1:
            binario = '1' + binario
        else:
            binario = '0' + binario
        decimal = decimal // 2
    binario = '1' + binario
        
print(binario)