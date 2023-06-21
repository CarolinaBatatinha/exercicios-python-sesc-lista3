# Faça um algoritmo para ler cinco números e imprimir o cubo e o quadrado de cada um deles.

for i in range(1, 6):
    numero = int(input('Digite um número: '))
    quadrado = numero ** 2
    cubo = numero ** 3
    
    print(f'Número: {numero}')
    print(f'Quadrado: {quadrado}')
    print(f'Cubo: {cubo}')
    print('-------------------------------')
