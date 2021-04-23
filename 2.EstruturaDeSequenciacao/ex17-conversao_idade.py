# Idade em dias
dias = int(input())

aa = dias // 365
mm = dias % 365 // 30
dd = dias % 365 % 30

print((aa), "ano(s)")
print((mm), "mes(es)")
print((dd), "dia(s)")