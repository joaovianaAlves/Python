from datetime import date

clientes = []
contas = []

def IniciarSistema():
    print("Bem-vindo ao Sistema Bancário")
    escolha = input("Você é administrador? (s/n): ").lower()
    if escolha == 's':
        MenuAdministrador()
    else:
        nome = input("Digite seu nome")

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

def CadastrarClientes(nome):
    cliente = {"nome": nome}
    return cliente

def CadastrarContaBancaria(cliente, transacoes, extrato):
    conta = {"nome": cliente["nome"], "transacoes": transacoes, "extrato": extrato}
    contas.append(conta)
    clientes.append(cliente)
    return conta

def ExibirClientes():
    if not clientes:
        print("Empty")
    else:
        for cliente, conta in zip(clientes, contas):
            print(f"{cliente['nome']}: {conta}")

def MenuAdministrador():
    print("Bem vindo Adm")
    while True:
        opcoes = {
                1: lambda: ExibirClientes(),
                2: lambda: CadastrarContaBancaria(CadastrarClientes(input("Digite o nome do cliente: ")), int(input("Digite o limite de transações diárias: ")), float(input("Digite o saldo inicial: "))),
        }
        escolha = int(input("Escolha o tipo de operacao desejada \n [1]Exibir Clientes \n [2]Cadastrar Clientes \n [3]Sair\n"))

        if escolha == 3:
            IniciarSistema()
        elif escolha in opcoes:
            resultado = opcoes[escolha]() 
            if resultado is not None:
                print(resultado)
            else:
                print("Entre um valor valido")

IniciarSistema()