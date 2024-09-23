def Banco(nome, extrato):
    while True:
        
        opcoes = {
            1: lambda: ExibirExtrato(extrato),
            2: lambda: Deposito(int(input("Digite a quantia a ser depositada: ")), extrato),
            3: lambda: Sacar(int(input("Digite a quantia a ser sacada: ")), extrato),
        }
        
        escolha = int(input(f"Bem Vindo {nome}! \n Escolha o tipo de operacao desejada \n [1]Exibir Extrato \n [2]Realizar Deposito \n [3]Realizar Saque \n [4]Sair\n"))
        
        if escolha == 4:
            break
        elif escolha in opcoes:
            resultado = opcoes[escolha]() 
            if resultado is not None:
                extrato = resultado
        else:
            print("Entre um valor valido")
            
def Deposito(valor, extrato):
    extratoAtualizado = extrato + valor
    print(f"Depositado {valor}, Extrato Atual {extratoAtualizado}")
    return extratoAtualizado

def Sacar(valor, extrato):
    if extrato <= 0:
        print("Saldo Insuficiente")
        return extrato
    else:
        extratoAtualizado = extrato - valor
        print(f"Sacado {valor}, Extrato Atual {extratoAtualizado}")
        return extratoAtualizado

def ExibirExtrato(extrato):
    print(f"Saldo Atual: {extrato}")

nome = "Joao"
extrato = 0

Banco(nome, extrato)