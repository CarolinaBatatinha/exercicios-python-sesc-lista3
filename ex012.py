# Faça um algoritmo para calcular a media de n números informados pelo usuário. Para sair do cálculo, o usuário deverá digitar um número negativo.

soma = 0
cont = 0

while True:
    num = int(input('Digite um número inteiro. Caso queira sair do programa, digite um número negativo. '))

    if num < 0:
        break

    soma += num
    cont += 1

if cont > 0:
    media = soma / cont
    print(f'A média dos {cont} números informados é {media}')
else:
    print('Nenhum número foi digitado.')

