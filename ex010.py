# Faça um algoritmo para um intervalo de números informados pelo usuário e calcular, para cada número, a raiz quadrada e sua metade.

menorNum = int(input('Digite um número para ser o menor do intervalo: '))
maiorNum = int(input('Digite um número para ser o maior do intervalo: '))

for num in range(menorNum, maiorNum + 1):
    raiz = num ** (1/2)
    metade = num / 2 

    print(f'\nNúmero: {num}\nRaíz quadrada: {raiz}\nMetade: {metade}\n -----------------')