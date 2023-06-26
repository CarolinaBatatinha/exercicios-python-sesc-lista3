# Faça um algoritmo para imprimir uma tabela de conversão entre Dólar e Real. A cotação de um Dólar em real deve ser fornecida pelo usuário. A tabela deve conter até 1000 Dólares.

cotacaoDolar = float(input('Digite a cotação do dólar em reais: '))

print("Tabela de conversão de Dólar(US$) para Real(R$):")
print("======================================")
print("US$\t\tR$")

for dolar in range(1, 1001):
    real = dolar * cotacaoDolar
    print(f'{dolar}\t\t{real:.2f}')
