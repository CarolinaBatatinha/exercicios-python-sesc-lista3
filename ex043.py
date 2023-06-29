# 43. Uma confecção vende conjuntos de malha em dois tamanhos: pequeno a R$ 50.00 e grande R$ 70,00 cada. Para pedidos superiores a 200 conjuntos os valores são reduzidos em 10 %. Se o pedido for superior a 1000 unidades a confecção oferece um desconto de 15 % para o tamanho grande e 13 % para o tamanho pequeno. Faça um algoritmo para ler o nome do cliente e um pedido (tamanho e quantidade) e imprimir o nome do cliente, o valor bruto, o desconto concedido e o valor a pagar.

nomeCliente = input("Digite o nome do cliente: ")
tamanho = input("Digite o tamanho do conjunto (P - Pequeno, G - Grande): ")
quantidade = int(input("Digite a quantidade de conjuntos: "))

if tamanho.upper() == 'P':
    valorUnitario = 50.00
elif tamanho.upper() == 'G':
    valorUnitario = 70.00
else:
    print("Tamanho de conjunto inválido. Encerrando o programa.")
    exit()

valorBruto = valorUnitario * quantidade

if quantidade > 200:
    valorDesconto = valorBruto * 0.10
elif quantidade > 1000:
    if tamanho.upper() == 'P':
        valorDesconto = valorBruto * 0.13
    else:
        valorDesconto = valorBruto * 0.15
else:
    valorDesconto = 0.00

valorAPagar = valorBruto - valorDesconto

print("\n-RESUMO DO PEDIDO")
print(f"Nome do cliente: {nomeCliente}")
print(f"Valor bruto: R$ {valorBruto:.2f}")
print(f"Desconto concedido: R$ {valorDesconto:.2f}")
print(f"Valor a pagar: R$ {valorAPagar:.2f}")
