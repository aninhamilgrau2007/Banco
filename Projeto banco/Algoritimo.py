import os
from Classe import *


banco = Banco()


def def_cadastro():
    x = 1
    while x == 1:
        os.system("cls")
        banco.adicionar_conta()
        banco.setNome(input("Digite o nome do cliente.\n-"))
        banco.setIdade(input("Digite a idade do cliente.\n-"))
        banco.setCpf(input("Digite o CPF do cliente.\n-"))
        banco.setSaldo(input("Digite o saldo do cliente.\n-"))
        print("Número da conta:", banco.getConta())
        os.system("pause")
        x = 2

def def_excluir():
    x = 1
    while x == 1:
        os.system("cls")
        banco.excluir(input("Digite o número da conta a ser excluído.\n"))
        print ("Excluído. Lista:\n", clientes)
        os.system("pause")
        x = 2

def def_alterar():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def def_saque():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def def_deposito():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2
    
def def_transferencia():
    x = 1
    while x == 1:
        os.system("cls")

        os.system("pause")
        x = 2

def main():
    while True:
        try:
            
            print("Bem Vindo ao PazBank")
            print("[1] - Cadastrar cliente")
            print("[2] - Excluir cliente")
            print("[3] - Alterar cliente")
            print("[4] - Realizar saque")
            print("[5] - Realizar depósito")
            print("[6] - Realizar transferência")
            print("[7] - Sair")

            op = int(input("Digite o número equivalente à opção que deseja:\n"))
            match op:
                case 1:
                    def_cadastro()
                case 2:
                    def_excluir()
                case 3:
                    def_alterar()
                case 4:
                    def_saque()
                case 5:
                    def_deposito()
                case 6:
                    def_transferencia()
                case 7: 
                    print("Saindo...")
                
                case _:
                    print("Essa opção não consta na lista.")
        except Exception:
            print("Algo deu errado. Tente novamente.\n")