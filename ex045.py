# 45. Faça um algoritmo para calcular a conta de um número indefinidos de mesas de uma pizzaria. Considere que o usuário possa informar através de um menu os seguintes itens:
#  - As bebidas e as quantidades vendidas
#  - As pizzas e as quantidades vendidas
#  - As sobremesas e as quantidades vendidas
# No final do processamento (no final do cálculo de todas as contas das mesas) as seguintes informações devem ser impressas:
#   a. A maior e a menor conta
#   b. A média de gasto por mesa
#   c. A média de gasto por pessoa
#   d. A média de pizzas consumida por mesa
#   e. A média de pedaços de pizzas consumidas por pessoas
#   f. A média de cervejas consumidas por mesas

maior_conta = 0
menor_conta = float('inf')
soma_contas = 0
soma_pessoas = 0
soma_pizzas = 0
soma_pedaços_pizzas = 0
soma_cervejas = 0
quantidade_mesas = 0

while True:
    opcao = input("Deseja calcular a conta de uma mesa? (S/N): ")

    if opcao.upper() == 'N':
        break

    qtd_bebidas = int(input("Digite a quantidade de bebidas vendidas: "))
    qtd_pizzas = int(input("Digite a quantidade de pizzas vendidas: "))
    qtd_sobremesas = int(input("Digite a quantidade de sobremesas vendidas: "))

    qtd_pessoas = int(input("Digite o número de pessoas na mesa: "))

    valor_bebidas = qtd_bebidas * 2.50
    valor_pizzas = qtd_pizzas * 25.00
    valor_sobremesas = qtd_sobremesas * 7.00
    valor_conta = valor_bebidas + valor_pizzas + valor_sobremesas

    maior_conta = max(maior_conta, valor_conta)
    menor_conta = min(menor_conta, valor_conta)
    soma_contas += valor_conta
    soma_pessoas += qtd_pessoas
    soma_pizzas += qtd_pizzas
    soma_pedaços_pizzas += qtd_pizzas * 8  # considerando que cada pizza tem 8 pedaços
    soma_cervejas += qtd_bebidas

    quantidade_mesas += 1

if quantidade_mesas > 0:
    media_gasto_mesa = soma_contas / quantidade_mesas
    media_gasto_pessoa = soma_contas / soma_pessoas
    media_pizzas_mesa = soma_pizzas / quantidade_mesas
    media_pedaços_pizzas_pessoa = soma_pedaços_pizzas / soma_pessoas
    media_cervejas_mesa = soma_cervejas / quantidade_mesas
else:
    media_gasto_mesa = 0
    media_gasto_pessoa = 0
    media_pizzas_mesa = 0
    media_pedaços_pizzas_pessoa = 0
    media_cervejas_mesa = 0

print("\n--- Resumo das contas das mesas ---")
print(f"a) Maior conta: R$ {maior_conta:.2f} // Menor conta: R$ {menor_conta:.2f}")
print(f"b) Média de gasto por mesa: R$ {media_gasto_mesa:.2f}")
print(f"c) Média de gasto por pessoa: R$ {media_gasto_pessoa:.2f}")
print(f"d) Média de pizzas consumidas por mesa: {media_pizzas_mesa:.2f}")
print(f"e) Média de pedaços de pizzas consumidos por pessoa: {media_pedaços_pizzas_pessoa:.2f}")
print(f"f) Média de cervejas consumidas por mesa: {media_cervejas_mesa:.2f}")
