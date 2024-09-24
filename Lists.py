import random

def evenOrOdd(numberList):
    for item in numberList:
        print(f'{item} : {"Even" if item % 2 == 0 else "Odd"}')

def generateNumbers(i):
    numberList = []
    numbers = [str(i) for i in range(10)]
    for _ in range(i):
        digits = random.randint(1, 5)
        randomNumber = ''.join(random.choice(numbers) for _ in range(digits))
        numberList.append(int(randomNumber))
    return numberList

evenOrOdd(generateNumbers(10))