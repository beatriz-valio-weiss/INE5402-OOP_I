numero = int(input())

a = 0
b = 1

if numero == 1:
    n_esimo_termo = 1
else:
    for f in range (1, numero):
        c = a + b
        a = b
        b = c
        n_esimo_termo = c

print(n_esimo_termo)