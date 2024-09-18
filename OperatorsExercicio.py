import math
#Exercio 1

valor1 = float(input("Digite o primeiro número:"))
valor2 = float(input("Digite o segundo número:"))

def Calculadora():
    print(f'Soma: {valor1 + valor2}')
    print(f'Subtração: {valor1 - valor2}')
    print(f'Divisão: {valor1 / valor2}')
    print(f'Multiplicação: {valor1 * valor2}')
    
Calculadora()

#Exercicio 2
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
p1 = float(input("Peso da primeira nota:"))
p2 = float(input("Peso da segunda nota:"))
p3 = float(input("Peso da terceira nota:"))

def mediaPonderada():
    somaDosPesos = p1 + p2 + p3
    media = (n1 * p1 + n2 * p2 + n3 * p3)/somaDosPesos
    print(media)

mediaPonderada()

#Exercicio 3

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

def Delta():
    return b**2 - 4*a*c

def Bhaskara():
    delta = Delta()
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print(f"x1: {x1}, x2: {x2}")
    
Bhaskara()
    


