contaCorrente = 0
saque = 1000
deposito = 2000



def getSaldo():
    return contaCorrente
    
def Depositar():
    global contaCorrente
    contaCorrente += deposito
    print(f"Depostidado: {deposito}, Saldo: {getSaldo()}")
    
def Saque():
    global contaCorrente
    if contaCorrente <= 0:
        print("Nao foi posivel sacar pois sua contaesta zerada")  
    else:
        contaCorrente -= saque
        print(f"Sacado: {saque}, Saldo: {getSaldo()}")
    
    
getSaldo()
Depositar()
Saque()