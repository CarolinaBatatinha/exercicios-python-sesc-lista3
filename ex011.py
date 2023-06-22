# Faça um algoritmo para ler 100 números, calcular a soma dos números, a média e o maior e menor número encontrados

soma = 0
maior = float('-inf')  # Inicializando com o menor valor possível
menor = float('inf')  # Inicializando com o maior valor possível
#float('-inf') representa o menor número possível no tipo de dado float em Python. Essa é uma convenção para inicializar a variável maior antes de começar a comparar os números.
#float('inf') inicializa variável menor antes de começar a comparar os números.

for i in range(1, 101):
    numero = float(input(f'Digite o {i}º número: '))

    soma += numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

media = soma / 100

print(f'Soma: {soma}')
print(f'Média: {media}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
