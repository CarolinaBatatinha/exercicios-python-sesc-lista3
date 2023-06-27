# Suponha que serão digitados 100 números inteiros via teclado, faça um algoritmo para:
#    • Somar os números positivos
#    • Contar os números negativos.
#    • A média dos números negativos e a média dos números positivos.
#    • A diferença entre o total de números positivos e negativos

somaPositivos = 0
contPositivos = 0
somaNegativos = 0
contNegativos = 0

for cont in range (1,11):
    numeroDigitado = int(input('Digite um número: '))
    if numeroDigitado > 0:
        somaPositivos += numeroDigitado
    if numeroDigitado < 0:
        somaNegativos += numeroDigitado
        contNegativos+= 1

print('Soma dos numeros positivos: ', somaPositivos)
print('Contagem dos numeros negativos: ', contNegativos)
print('Média dos números positivos: ', (somaPositivos/contPositivos))
print('Média dos números negativos: ', (somaNegativos/contNegativos))
print('Diferença é: ', somaPositivos - abs(somaNegativos)) #abs mostra o número absoluto
