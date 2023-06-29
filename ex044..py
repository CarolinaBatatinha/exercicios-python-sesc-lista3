# 44. Faça um algoritmo para calcular a conta das mesas de uma lanchonete com base no consumo de seus clientes. Considere que o usuário pode escolher os seguintes itens do menu:
# 1 – lanches:
#    X-Tudo R$ 4,00
#    X-Bacon R$ 3,00
#    X-Salada R$ 2,00
# 2 – Bebidas:
#    Refrigerante R$ 1,50
#    Cerveja R$ 1,80
#    Agua Mineral R$ 0,80
# O programa deverá ler as quantidades dos itens e calcular o valor total da conta. Isso será realizado até que o usuário deseja sair do programa. No entanto, é necessário saber no final do processamento do cálculo das mesas, os valores da maior conta, menor conta e a média dos valores das contas das mesas.

maior_conta = 0
menor_conta = float('inf')
soma_contas = 0
quantidade_mesas = 0

while True:
    opcao = input("Deseja calcular a conta de uma mesa? (S/N): ")
    
    if opcao.upper() == 'N':
        break
    
    qtd_lanches_xtudo = int(input("Digite a quantidade de X-Tudo: "))
    qtd_lanches_xbacon = int(input("Digite a quantidade de X-Bacon: "))
    qtd_lanches_xsalada = int(input("Digite a quantidade de X-Salada: "))
    qtd_bebidas_refri = int(input("Digite a quantidade de Refrigerante: "))
    qtd_bebidas_cerveja = int(input("Digite a quantidade de Cerveja: "))
    qtd_bebidas_agua = int(input("Digite a quantidade de Água Mineral: "))
    
    valor_lanches = qtd_lanches_xtudo * 4.00 + qtd_lanches_xbacon * 3.00 + qtd_lanches_xsalada * 2.00
    valor_bebidas = qtd_bebidas_refri * 1.50 + qtd_bebidas_cerveja * 1.80 + qtd_bebidas_agua * 0.80
    valor_conta = valor_lanches + valor_bebidas
    
    maior_conta = max(maior_conta, valor_conta)
    menor_conta = min(menor_conta, valor_conta)
    soma_contas += valor_conta
    quantidade_mesas += 1

if quantidade_mesas > 0:
    media_contas = soma_contas / quantidade_mesas
else:
    media_contas = 0

print("\n--- Resumo das contas das mesas ---")
print(f"Maior conta: R$ {maior_conta:.2f}")
print(f"Menor conta: R$ {menor_conta:.2f}")
print(f"Média das contas: R$ {media_contas:.2f}")
