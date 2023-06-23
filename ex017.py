# Desenvolva um algoritmo para calcular o fatorial de um número. Por exemplo: 0! = 1, 1! = 1 e 5!= 5x4x3x2x1 = 120. Lembre-se, não existe fatorial de número negativo e de número real.

num = int(input('Digite um número inteiro não negativo: '))
fatorial = 1

if num < 0:
    print('O número não pode ser negativo.')
else:
    for i in range(2, num + 1):
        fatorial *= i

print(f'O fatorial de {num} é igual a {fatorial}.')

# ou

# from math import factorial 
#se fosse importada toda a biblioteca, precisaria escrever "math.factorial", por exemplo

# num = int(input('Digite um número: '))

# fatorial = factorial(num)

#print(fatorial)