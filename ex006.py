# Elabore um algoritmo para calcular a soma dos números impares de 0 a 100.
soma = 0

for num in range(0, 100):
    
    if num % 2 != 0 and num > 0 and num < 100:
        soma += num
print(f'A soma dos números ímpares compreendidos entre 0 e 100 é igual a {soma}.')
