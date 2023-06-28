# 36. Faça um algoritmo que leia o nome, salário e número de filhos de 100 pessoas, e calcule:
    # • O salário médio das pessoas que possuam 2 filhos
    # • O salário médio das que não possuem filhos
    # • Qual a média salarial maior, entre os que têm um e dois filhos
    # • O salário médio geral
salarioMedio = 0
somaSalario = 0
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário em reais (R$): '))
filhos = int(input('Digite seu número de filhos: '))

for i in range(1,101):
    if 1 <= filhos <=2:
        i += 1
        somaSalario+= salarios
        salarioMedio = somaSalario / i
        print(salarioMedio)
    if filhos == 0:
        i += 1
        somaSalario+= salario
        salarioMedio = somaSalario / i
print(salarioMedio)
    
        
