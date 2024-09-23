def criarCarro(ano, modelo, marca, placa):
    print(f'Carro criado: {ano}-{modelo}-{marca}-{placa}')

criarCarro(ano= 2004, modelo="Palio", marca="Fiat", placa="ABC-12345")

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def Calculadora(a,b,funcao):
    resultado = funcao(a,b)
    print(resultado)
    
Calculadora(10,10, somar)
Calculadora(12,10, subtrair)