# Construir um programa que calcule a soma dos N primeiros números inteiros, onde N será digitado pelo usuário. Por exemplo, soma = 1 + 2 + 3 + 4 + ..... + N.
soma =  0
num = int(input('Insira um número inteiro: '))

for i in range(1, num + 1):
    soma += i
print(f'A soma dos {num} números inteiros é igual a {soma}.')
