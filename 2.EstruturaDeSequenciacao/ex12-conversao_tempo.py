# Em segundos...
numero_inteiro = int(input())

# Em horas : minutos : segundos
hh = numero_inteiro // 3600
mm = numero_inteiro % 3600 // 60
ss = numero_inteiro % 60

print("{}:{}:{}".format(hh, mm, ss))