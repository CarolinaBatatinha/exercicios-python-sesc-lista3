# 47. Agora desenvolva o algoritmo para informatizar o cálculo de uma churrascaria, considerando os menus:
# - Bebidas
# - Sobremesas
# No final do processamento (no final do cálculo de todas as contas das mesas) as seguintes informações devem ser impressas:
# a. A maior e a menor conta
# b. A média de gasto por mesa
# c. A média de gasto por pessoa
# d. A média de rodízios por mesa

maiorConta = 0
menorConta = float('inf')
somaContas = 0
somaPessoas = 0
somaRodizios = 0
quantidadeMesas = 0

while True:
    opcao = input("Deseja calcular a conta de uma mesa? (S/N): ")

    if opcao.upper() == 'N':
        break

    qtdeBebidas = int(input("Digite a quantidade de bebidas vendidas: "))
    qtdeRodizios = int(input("Digite a quantidade de rodízios consumidos: "))
    qtdeSobremesas = int(input("Digite a quantidade de sobremesas consumidas: "))

    qtdePessoas = int(input("Digite o número de pessoas na mesa: "))

    valorBebidas = qtdeBebidas * 7.50
    valorRodizios = qtdeRodizios * 70.00
    valorSobremesas = qtdeSobremesas * 12.00
    valorConta = valorBebidas + valorRodizios + valorSobremesas

    if valorConta > maiorConta:
        maiorConta = valorConta

    if valorConta < menorConta:
        menorConta = valorConta

    somaContas += valorConta
    somaPessoas += qtdePessoas
    somaRodizios += qtdeRodizios

    quantidadeMesas += 1

mediaGastoMesa = somaContas / quantidadeMesas
mediaGastoPessoa = somaContas / somaPessoas
mediaRodiziosMesa = somaRodizios / quantidadeMesas

print("\nRESUMO DAS CONTAS DAS MESAS")
print(f"Maior conta: R$ {maiorConta:.2f}")
print(f"Menor conta: R$ {menorConta:.2f}")
print(f"Média de gasto por mesa: R$ {mediaGastoMesa:.2f}")
print(f"Média de gasto por pessoa: R$ {mediaGastoPessoa:.2f}")
print(f"Média de rodízios por mesa: {mediaRodiziosMesa:.1f}")
