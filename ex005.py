# Faça um algoritmo que imprima todos os números de 1 até um número especificado pelo usuário e a soma deles.
soma = 0
num = int(input('Digite um número inteiro: '))

for i in range(1, num + 1):
    
    soma += i

print(soma)