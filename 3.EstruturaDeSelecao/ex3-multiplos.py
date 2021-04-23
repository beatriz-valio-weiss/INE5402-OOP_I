a, b = [int(w) for w in input().split()]

if a % b == 0:
    print("Sao Multiplos")
elif b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")