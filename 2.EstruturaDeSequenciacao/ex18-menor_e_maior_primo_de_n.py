import math

# Menor (P) e maior (M) número primo de n
n = int(input())

P = n / math.log(n)
M = 125506 / 100000 * n / math.log(n)

print("{:.1f} {:.1f}".format(P, M))