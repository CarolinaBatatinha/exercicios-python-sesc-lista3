# Será digitado uma série de números inteiros. Faça um algoritmo para calcular e imprimir o produto desses valores, isto é, o resultado da multiplicação de todos os números. Número de entrada desconhecido.

produto = 1  

while True:
    try:
        numero = int(input('Digite um número inteiro (ou qualquer outro caractere para sair): '))
        produto *= numero  
    except ValueError: #ValueError é uma exceção que o Python usa para indicar que algo anormal aconteceu durante a execução do  código
        break  # Sai do loop se um valor não numérico for fornecido

print("O produto dos números é:", produto)
