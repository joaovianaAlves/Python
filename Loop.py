# texto = input("Digite uma palavra: ")
# vogais = "AEIOU"

# for letra in texto:
#     if letra.upper() in vogais:
#         print(letra, end="")22
# for numero in range(10):
#     print(numero, end=" ")
  
# for numero in range(0, 51, 5):
#     print(numero, end=" ")

opcao = -1
    
while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Depositar \n [0] Sair \n"))
    print("sacando...") if opcao == 1 else print("exibindo extrato") if opcao == 2 else None
    if opcao == 0:
        print("Saindo...")
        break
    else:
        continue
    