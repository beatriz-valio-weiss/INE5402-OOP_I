cartas_tiradas = [int(x) for x in input().split()]
cartas_crescentes = sorted(cartas_tiradas)
cartas_decrescentes = sorted(cartas_tiradas, reverse = True)

if cartas_tiradas == cartas_crescentes:
    print("C")
elif cartas_tiradas == cartas_decrescentes:
    print("D")
else:
    print("N")