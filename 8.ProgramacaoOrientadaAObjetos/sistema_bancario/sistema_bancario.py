from banco import Banco

bc = Banco("Banco XXX", 000)

while True:
    try:
        dados = input().split()
    except EOFError:
        break
    operacao = dados[0]
    if operacao == 'abre_conta':
        cpf = int(dados[1])
        nome = dados[2]
        conta = bc.abre_conta(nome, cpf)
        
    elif operacao == 'deposito':
        cpf = int(dados[1])
        valor = float(dados[2])
        nct = bc.numero_conta(cpf)
        bc.deposito(nct,valor)
        
    elif operacao == 'saque':
        cpf = int(dados[1])
        valor = float(dados[2])
        nct = bc.numero_conta(cpf)
        bc.saque(nct,valor)
        
    elif operacao == 'transferencia':
        cpf_origem = int(dados[1])
        cpf_destino = int(dados[2])
        valor = float(dados[3])
        nct_origem = bc.numero_conta(cpf_origem)
        nct_destino = bc.numero_conta(cpf_destino)
        bc.transferencia(nct_origem, nct_destino, valor)

bc.liste_cpfs_saldos()
    
