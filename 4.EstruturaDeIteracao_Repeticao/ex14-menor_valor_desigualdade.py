def fatorial(x):
    f = 1
    for num in range (1, x + 1):
        f *= num
    return f

x = 2
f = fatorial(x)

while f <= x**10:
    x += 1
    f = fatorial(x)

print(x)