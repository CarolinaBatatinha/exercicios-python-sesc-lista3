# Faça um programa que calcule a soma dos números pares e impares a partir de um valor inicial e final informados pelos usuários. Por exemplo, se usuário informou 120 e 130, o programa deverá calculara soma dos números pares : 120 + 122 + 124 + 126 +128 + 130, além dos números impares: 121 + 123 + 125 + 127 + 129.
somaPares = 0 
somaImpares = 0 
valorInicial = int(input('Digite o valor inicial: '))
valorFinal = int(input('Digite o valor final: '))

for cont in range(valorInicial, valorFinal + 1):
    if cont % 2 == 0:
        somaPares += cont
    
    if cont % 2 != 0:
        somaImpares += cont

print("Soma dos pares: ", somaPares)
print("Soma dos ímpares: ", somaImpares)


