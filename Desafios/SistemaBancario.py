from datetime import date
def Banco(nome, extrato, transacao, data):
    ultima_data = data
    while True:
        data_atual = date.today()
        print(f"Data atual no sistema: {data_atual}")
        transacao = resetarTransacao(ultima_data, data_atual, transacao)
        opcoes = {
            1: lambda: ExibirExtrato(extrato, transacao),
            2: lambda: print("Limite de Transações Diarias Atingidas")if transacao <= 0 else Deposito(int(input("Digite a quantia a ser depositada: ")), extrato, transacao),
            3: lambda: print("Limite de Transações Diarias Atingidas")if transacao <= 0 else Sacar(int(input("Digite a quantia a ser sacada: ")), extrato, transacao),
        }
        
        escolha = int(input(f"Bem Vindo {nome}! \n Escolha o tipo de operacao desejada \n [1]Exibir Extrato \n [2]Realizar Deposito \n [3]Realizar Saque \n [4]Sair\n"))
        
        if escolha == 4:
            break
        elif escolha in opcoes:
            resultado = opcoes[escolha]() 
            if resultado is not None:
                extrato, transacao = resultado
        else:
            print("Entre um valor valido")

def verificarStatusTransacao(transacao):
    transacaoAtualizada = transacao - 1
    return transacaoAtualizada

def resetarTransacao(ultima_data, data_atual, transacao):
    if data_atual > ultima_data:
        print(f"Dia novo detectado: {data_atual}. Transações resetadas.")
        return 10
    return transacao
    
        
def Deposito(valor, extrato, transacao):
    extratoAtualizado = extrato + valor
    transacaoAtualizada = verificarStatusTransacao(transacao)
    print(f"Depositado {valor}, Extrato Atual {extratoAtualizado}, Transaçoes: {transacaoAtualizada}")
    return extratoAtualizado, transacaoAtualizada

def Sacar(valor, extrato, transacao):
    if extrato <= 0:
        print("Saldo Insuficiente")
        return extrato
    else:
        extratoAtualizado = extrato - valor
        transacaoAtualizada =verificarStatusTransacao(transacao)
        print(f"Depositado {valor}, Extrato Atual {extratoAtualizado}, Transaçoes: {transacaoAtualizada}")
        return extratoAtualizado, transacaoAtualizada

def ExibirExtrato(extrato, transacao):
    print(f"Saldo Atual: {extrato}, Transacoes: {transacao}")

def CadastrarClienta():
    return ""

def CadastrarContaBancaria():
    return ""

nome = "Joao"
extrato = 0
transacao = 10
data = date(2023,7,1)

Banco(nome, extrato, transacao, data)