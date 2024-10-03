from datetime import date

dados_clientes = {
    'joao': {
        'extrato': 0.0,
        'transacoes': 10
    }
}

def IniciarSistema():
    print("Bem-vindo ao Sistema Bancário")
    escolha = input("Você é administrador? (s/n): ").lower()
    if escolha == 's':
        MenuAdministrador()
    else:
        nome = input("Digite seu nome: ")
        resultado = AcharDadosCliente(nome)
        if resultado:
            extrato, transacao, ultima_data = resultado
            Banco(nome, extrato, transacao, ultima_data)
        else:
            print(f"Cliente {nome} não encontrado.")
            IniciarSistema()

def Banco(nome, extrato, transacao, data):
    ultima_data = data
    while True:
        data_atual = date.today()
        print(f"Data atual no sistema: {data_atual}")
        transacao = resetarTransacao(ultima_data, data_atual, transacao)
        opcoes = {
            1: lambda: ExibirExtrato(extrato, transacao),
            2: lambda: print("Limite de Transações Diárias Atingido") if transacao <= 0 else Deposito(int(input("Digite a quantia a ser depositada: ")), extrato, transacao),
            3: lambda: print("Limite de Transações Diárias Atingido") if transacao <= 0 else Sacar(int(input("Digite a quantia a ser sacada: ")), extrato, transacao),
        }
        
        escolha = int(input(f"Bem vindo, {nome}! \n Escolha o tipo de operação desejada: \n [1]Exibir Extrato \n [2]Realizar Depósito \n [3]Realizar Saque \n [4]Sair\n"))
        
        if escolha == 4:
            SalvarDadosCliente(nome, extrato, transacao)
            IniciarSistema()
        elif escolha in opcoes:
            resultado = opcoes[escolha]() 
            if resultado is not None:
                extrato, transacao = resultado
        else:
            print("Digite um valor válido")

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
    print(f"Depositado {valor}, Extrato Atual {extratoAtualizado}, Transações: {transacaoAtualizada}")
    return extratoAtualizado, transacaoAtualizada

def Sacar(valor, extrato, transacao):
    if extrato < valor:
        print("Saldo Insuficiente")
        return extrato, transacao
    else:
        extratoAtualizado = extrato - valor
        transacaoAtualizada = verificarStatusTransacao(transacao)
        print(f"Sacado {valor}, Extrato Atual {extratoAtualizado}, Transações: {transacaoAtualizada}")
        return extratoAtualizado, transacaoAtualizada

def ExibirExtrato(extrato, transacao):
    print(f"Saldo Atual: {extrato}, Transações restantes: {transacao}")

def CadastrarClientes(nome):
    cliente = {"nome": nome}
    return cliente

def CadastrarContaBancaria(cliente, transacoes, extrato):
    conta = {"transacoes": transacoes, "extrato": extrato}
    dados_clientes[cliente] = conta
    return conta

def AcharDadosCliente(nome):
    if nome in dados_clientes:
        dados = dados_clientes[nome]
        return dados['extrato'], dados['transacoes'], date.today()
    return None

def ExibirClientes():
    if not dados_clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in dados_clientes:
            print(f"{cliente}: {dados_clientes[cliente]}")
            
def SalvarDadosCliente(nome, extrato, transacao):
    if nome in dados_clientes:
        dados_clientes[nome]['extrato'] = extrato
        dados_clientes[nome]['transacoes'] = transacao

def MenuAdministrador():
    print("Bem vindo, Administrador!")
    while True:
        opcoes = {
            1: lambda: ExibirClientes(),
            2: lambda: CadastrarContaBancaria(CadastrarClientes(input("Digite o nome do cliente: ")), int(input("Digite o limite de transações diárias: ")), float(input("Digite o saldo inicial: "))),
        }
        escolha = int(input("Escolha o tipo de operação desejada: \n [1]Exibir Clientes \n [2]Cadastrar Cliente \n [3]Sair\n"))

        if escolha == 3:
            IniciarSistema()
        elif escolha in opcoes:
            resultado = opcoes[escolha]() 
            if resultado is not None:
                print(resultado)
            else:
                print("Operação realizada com sucesso.")
        else:
            print("Digite um valor válido.")

IniciarSistema()
