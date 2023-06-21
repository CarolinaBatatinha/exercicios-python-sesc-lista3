# Faça um algoritmo para calcular o cubo e o quadrado de todos os números pertencentes a um intervalo, incluindo o limite superior e inferior.

menorNum = int(input('Digite um número para ser o menor do intervalo: '))
maiorNum = int(input('Digite um número para ser o maior do intervalo: '))

for num in range (menorNum, maiorNum + 1):
    quadrado = num ** 2
    cubo = num ** 3

    print(f'Número: {num} \nQuadrado: {quadrado}\nCubo: {cubo}\n ---------------')