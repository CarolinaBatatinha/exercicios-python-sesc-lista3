# Faça um algoritmo para imprimir os múltiplos de 5 em um intervalo informado pelo usuário.

numA = int(input('Digite um número: '))
numB = int(input('Digite outro número: '))

for num in range(numA, numB):
    if num % 5 == 0:
        print(num)