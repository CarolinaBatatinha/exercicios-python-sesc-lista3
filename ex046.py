# 46. Faça um algoritmo para calcular a conta de um número indefinidos de mesas de uma lanchonete. Considere que o usuário possa informar através de um menu os seguintes itens:
# - As bebidas e as quantidades vendidas
# - Os lanches e as quantidades vendidas
# - As porções e as quantidades consumidas
# No final do processamento (no final do cálculo de todas as contas das mesas) as seguintes informações devem ser impressas:
# a. A maior e a menor conta
# b. A média de gasto por mesa
# c. A média de gasto por pessoa
# d. A média de lanches consumidos por mesa
# e. A média de lanches consumidos por pessoas
# f. A média de porções consumidas por mesa
# g. O total de lanche e de porções

maiorConta = 0
menorConta = float('inf')
somaContas = 0
somaPessoas = 0
somaLanches = 0
somaPorcoes = 0
totalLanches = 0
totalPorcoes = 0
quantidadeMesas = 0

while True:
    opcao = input("Deseja calcular a conta de uma mesa? (S/N): ")

    if opcao.upper() == 'N':
        break

    qtdeBebidas = int(input("Digite a quantidade de bebidas vendidas: "))
    qtdeLanches = int(input("Digite a quantidade de lanches vendidos: "))
    qtdePorcoes = int(input("Digite a quantidade de porções consumidas: "))

    qtdePessoas = int(input("Digite o número de pessoas na mesa: "))

    valorBebidas = qtdeBebidas * 2.50
    valorLanches = qtdeLanches * 10.00
    valorPorcoes = qtdePorcoes * 15.00
    valorConta = valorBebidas + valorLanches + valorPorcoes

    maiorConta = max(maiorConta, valorConta)
    menorConta = min(menorConta, valorConta)
    somaContas += valorConta
    somaPessoas += qtdePessoas
    somaLanches += qtdeLanches
    somaPorcoes += qtdePorcoes
    totalLanches += qtdeLanches
    totalPorcoes += qtdePorcoes

    quantidadeMesas += 1

if quantidadeMesas > 0:
    mediaGastoMesa = somaContas / quantidadeMesas
    mediaGastoPessoa = somaContas / somaPessoas
    mediaLanchesMesa = somaLanches / quantidadeMesas
    mediaLanchesPessoa = somaLanches / somaPessoas
    mediaPorcoesMesa = somaPorcoes / quantidadeMesas
else:
    mediaGastoMesa = 0
    mediaGastoPessoa = 0
    mediaLanchesMesa = 0
    mediaLanchesPessoa = 0
    mediaPorcoesMesa = 0

print("\nRESUMO DAS CONTAS DAS MESAS")
print(f"Maior conta: R$ {maiorConta:.2f}")
print(f"Menor conta: R$ {menorConta:.2f}")
print(f"Média de gasto por mesa: R$ {mediaGastoMesa:.2f}")
print(f"Média de gasto por pessoa: R$ {mediaGastoPessoa:.2f}")
print(f"Média de lanches consumidos por mesa: {mediaLanchesMesa:.2f}")
print(f"Média de lanches consumidos por pessoa: {mediaLanchesPessoa:.2f}")
print(f"Média de porções consumidas por mesa: {mediaPorcoesMesa:.2f}")
print(f"Total de lanches vendidos: {totalLanches}")
print(f"Total de porções consumidas: {totalPorcoes}")
