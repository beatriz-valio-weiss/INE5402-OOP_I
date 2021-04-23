n = int(input())

while n != 0:
    mary = 0
    john = 0
    jogadas = [str(n) for n in input().split()]
    mary = jogadas.count('0')
    john = jogadas.count('1')
    print("Mary won {} times and John won {} times".format(mary, john))
    n = int(input())