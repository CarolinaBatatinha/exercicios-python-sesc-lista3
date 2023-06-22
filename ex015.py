# Faça um algoritmo para imprimir a quantidade de números ímpares entre um intervalo especificado pelo usuário.

numA = int(input('Digite o primeiro número do intervalo: '))
numB = int(input('Digite o segundo número do intervalo: '))

for i in range (numA, numB):
    if i % 2 != 0:
        print(i)