# def analise_vendas(vendas):
#         total_vendas,media_vendas = calcula_vendas(vendas)
#         return f"{total_vendas}, {media_vendas:.2f}"
    
# def calcula_vendas(vendas):
#     total = sum(vendas)
#     media = total / len(vendas)
    
#     return total,media

# def obter_entrada_vendas():
#     entrada = input()
#     sales = [int(value) for value in entrada.split(",")]
#     return sales

# vendas = obter_entrada_vendas()
# print(analise_vendas(vendas))

def analise_vendas(vendas):
    mais_vendido = verificar_mais_vendido(vendas)
    return mais_vendido

def verificar_mais_vendido(vendas):
    contagem = {}
    for produto in vendas:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
            
    return max(contagem, key=contagem.get)
            
        

def obter_entrada_vendas():
    entrada = input()
    sales = [value.strip() for value in entrada.split(",")]
    return sales
    
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))