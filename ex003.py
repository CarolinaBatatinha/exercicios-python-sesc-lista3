# Faça um algoritmo para imprimir a soma dos números entre um intervalo determinado pelo usuário, incluindo os limites inferiores e superiores.

menorNumero = int(input('Digite o menor número do intervalo: '))
maiorNumero = int(input('Digite o maior número do intervalo: '))

soma = 0

for numero in range(menorNumero, maiorNumero):
    soma = soma + numero

print(f'A soma dos números entre o intervalo é igual a {soma}')