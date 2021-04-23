msg_codificada = input()
msg_descodificada = ""

for letra in range(len(msg_codificada)-1):
    if msg_codificada[letra] == "p":
        if msg_codificada[letra] == msg_codificada[letra+1] == "p":
            if msg_codificada[letra] == msg_codificada[letra-1] == "p":
                msg_descodificada += ""
            else:
                msg_descodificada += "p"
        else:
            msg_descodificada += ""
    else:
        msg_descodificada += msg_codificada[letra]
msg_descodificada += msg_codificada[letra+1]

print(msg_descodificada)