import random
class Cliente:

    def sacar(self, valor,saldo):
        if valor > saldo:
            print("Não é possível sacar esse valor")
        else:
            self.saldo -= valor
            print("Valor sacado com sucesso! O saldo agora é de R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print("Valor depositado com sucesso! O saldo agora é de R$", self.saldo)

    def transferencia(self, num_conta1, num_conta2, valor):
        num_conta1.saldo=self.saldo - valor
        num_conta2.saldo=self.saldo + valor
        return num_conta1.saldo, num_conta2.saldo

class Banco:

    def adicionar_conta(self):
        self.num_conta = random.randint(1000,9999)
        self.nome = ""
        self.idade = 0
        self.cpf = 0
        self.saldo = 0
        conta = {'conta': self.num_conta, 'nome': self.nome, 'idade': self.idade, 'cpf': self.cpf, 'saldo' : self.saldo}
        clientes.append(conta)
    
    def getConta(self):
        return self.num_conta
   
    def getNome(self):
        return self.nome
    
    def setNome(self,x):
        self.nome = x
        
    def getIdade(self):
        return self.idade
    
    def setIdade(self,x):
        self.idade = x

    def getCpf(self):
        return self.cpf
    
    def setCpf(self,x):
        self.cpf = x
        
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self,x):
        self.saldo = x

    def excluir(self, num_conta):
        del num_conta

clientes = []