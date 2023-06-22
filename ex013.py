# Desenvolva um programa que permite para calcular a soma de números a partir do número 1 até um número informado pelo usuário. Por exemplo, se o usuário informar o número 5, o programa deverá calcular: 1 + 2 + 3 + 4 + 5 = 15, e mostrar o resultado para o usuário.
soma = 0
num = int(input('Digite um número inteiro: '))

if num <= 0:
    print('Digite um valor positivo.')
else:
    for cont in range(1, num + 1):
        soma += cont

    print(f'A soma dos valores de 1 à {num} é igual a {soma}.')