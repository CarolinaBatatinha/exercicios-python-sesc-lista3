# Elabore um algoritmo para calcular a soma dos números impares de 1000 a 10.
soma = 0

for num in range(10, 1000):
    if num % 2 != 0 and num > 10 and num < 1000:
        soma += num
        
print(f'A soma de todos os números ímpares compreendidos entre 1000 e 10 é igual a {soma}.')
