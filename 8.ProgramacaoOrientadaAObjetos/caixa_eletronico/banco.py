from ficha_bancaria import * # * importa todo o arquivo

class Banco:
    
    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__ultima_conta_criada = 0
        self.__fichario = {}
        
    def abre_conta(self, nome_cliente, cpf_cliente):
        ''' Abre uma nova conta no banco '''
        
        self.__ultima_conta_criada += 1
        
        ficha = FichaBancaria()
        ficha.set_numero(self.__ultima_conta_criada)
        ficha.set_nome(nome_cliente)
        ficha.set_cpf(cpf_cliente)
        self.__fichario[self.__ultima_conta_criada] = ficha
        return self.__ultima_conta_criada
    
    def numero_conta(self, cpf):
        for ficha in self.__fichario.values():
            if ficha.get_cpf() == cpf:
                return ficha.get_numero()
        return 0            
  
    def deposito(self, numero_conta, valor):
        ''' Realiza um depósito numa conta '''
        
        if numero_conta in self.__fichario:
            self.__fichario[numero_conta].credite(valor)
            return True
        else:
            return False
            
    def saque(self, numero_conta, valor):
        ''' Realiza um saque numa conta '''
        if numero_conta in self.__fichario:
            if valor <= self.__fichario[numero_conta].get_saldo():
                self.__fichario[numero_conta].debite(valor)
                return True
            else:
                return False
        else:
            return False
    
    def transferencia(self, nct_origem, nct_destino, valor):
        ''' Realiza transferência entre duas contas '''
        if nct_origem in self.__fichario and nct_destino in self.__fichario:
            ficha_origem = self.__fichario[nct_origem]
            if ficha_origem.get_saldo() >= valor:
                ficha_origem.debite(valor)        
                self.__fichario[nct_destino].credite(valor)
                return True
            else:
                return False
        else:
            return False

    def saldo(self, numero_conta):       
        ''' Obtém o saldo de uma conta '''
        if numero_conta in self.__fichario:
            return self.__fichario[numero_conta].get_saldo()
        else:
            return 0
 
    def encerra_conta(self, numero_conta):
        ''' Encerra uma conta '''
        
        if numero_conta in self.__fichario and self.saldo(numero_conta) == 0:
            del self.__fichario[numero_conta]
            return True
        else:
            return False
        
    def conta_maior_saldo(self):
        '''Obtém o nº da conta do cliente com maior saldo'''
        
        maior_saldo = -math.inf
        nct = 0
        for ficha in self.__fichario.values():
            if ficha.get_saldo() > maior_saldo:
                maior_saldo = ficha.get_saldo()
                nct = ficha.get_numero()
        return nct

    def saldo_medio(self):
        '''Cálcula o saldo médio dos correntistas'''
        soma = 0
        for ficha in self.__fichario.values():
            soma += ficha.get_saldo()
        return soma / len(self.__fichario)      
    
    def cpfs_duplicados(self):
        ''' Obtém os cpfs duplicados (em mais de uma conta) '''
        cpfs = set()
        cpfs_duplicados = set()
        for ficha in self.__fichario.values():
            if ficha.get_cpf() in cpfs:
                cpfs_duplicados.add(ficha.get_cpf())
            else:
                cpfs.add(ficha.get_cpf())
        return cpfs_duplicados
    
    def liste_cpfs_saldos(self):
        cpfs = dict()
        for ficha in self.__fichario.values():
            cpf = ficha.get_cpf()
            saldo = ficha.get_saldo()
            cpfs[cpf] = saldo
        cpfs_ordenados = list(cpfs.keys())
        cpfs_ordenados.sort()
        for cpf in cpfs_ordenados:
            print(cpf, cpfs[cpf])
        
            