# Faça um algoritmo para calcular a tabuada de um número informado pelo usuário. O usuário, se a tabuada do 5 for selecionada, deverá visualizar o seguinte resultado: 5 x 1 = 5, ...., 5 x 10 = 50. Por fim, o algoritmo deverá calcular e imprimir a soma de todos os valores resultantes dos cálculos.

num = int(input('Digite um número inteiro: '))
print(f'==== TABUADA DE {num} =====')
soma = 0

for i in range(1, 11):
    resultado = num * i

    soma += resultado

    print(f'{num} x {i} = {resultado}')
print(f'A soma de todos os resultados da tabuada de {num} é igual a {soma}.')