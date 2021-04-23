# notacao cientifica
num_string = input()
num_flutuante = float(num_string)

notacao_cientifica = "{:.4e}".format(num_flutuante)
notacao_cientifica = notacao_cientifica.upper()

if num_flutuante >= 0:
    notacao_cientifica = "+" + notacao_cientifica

print(notacao_cientifica)

'''
print("{:.4e}".format(num_flutuante))
'''