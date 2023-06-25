#25. Escrever um algoritmo que leia 10 valores, um de cada vez, e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.

somaDentroIntervalo = 0
somaForaIntervalo = 0 

for n in range (1, 11):
    numeroDigitado = int(input(f'Digite o {n}º valor: '))
    #if 10 <= numeroDigitado <= 20:
    #if numeroDigitado >= 10 and numeroDigitado <= 20:
    if numeroDigitado in range (10, 21):
        somaDentroIntervalo += 1
    else:
        somaForaIntervalo += 1 
print(f'Dentro do intervalo: {somaDentroIntervalo}')
print(f'Fora do intervalo: {somaForaIntervalo}')