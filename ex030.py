# Crie uma algoritmo para imprimir todas as tabuadas do 1 até o 10.

for multiplicador in range(1, 11):
    print(f'Tabuada de {multiplicador}: ')

    for multiplicando in range(1, 11):
        resultado = multiplicador * multiplicando
        print(f'{multiplicador} x {multiplicando} = {resultado}')
    
