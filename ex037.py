# Agora repita o exercício anterior para um número indefinido de pessoas.

while True:
    salarioMedio = 0
    somaSalario = 0
    nome = input('Digite seu nome: ')
    salario = float(input('Digite seu salário em reais (R$): '))
    filhos = int(input('Digite seu número de filhos: '))

    if 1 <= filhos <=2:
        i += 1
        somaSalario+= salario
        salarioMedio = somaSalario / i
        print(salarioMedio)
    if filhos == 0:
        i += 1
        somaSalario+= salario
        salarioMedio = somaSalario / i

    print(salarioMedio)
