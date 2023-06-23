# Elabore um algoritmo para ler os números N e P, e calcule a exponenciação de N^P.
import math
n = int(input('Digite um número inteiro: '))
p = int(input('Digite outro número inteiro: '))

calculo = math.pow(n, p)

print(f'O resultado de {n} elevado a {p} é igual a {calculo}.')