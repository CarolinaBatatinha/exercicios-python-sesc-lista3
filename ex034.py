# #Uma empresa está fazendo análise de uma 1000 pessoas do sexo masculino . Os seguintes dados são obtidos das pessoas:
# a. Idade
# b. Cor de Cabelos (Castanhos, Pretos, Loiros ou Outro)
# c. Altura
# d. Peso
# e. Sexo (Masculino ou Feminino)
# Faça um algoritmo para mostrar, ao final do processamento os seguintes dados:
# a. Quantas pessoas possuem idade superior a 18 anos
# b. Qual é a média das idades, a idade da pessoa mais idosa e a idade da pessoa mais jovem?
# c. Quantas pessoas em porcentagem possuem cabelos castanhos, pretos, loiros e outros?
# d. Quantas pessoas possuem altura superior a 1,70 m
# e. Quantas pessoas peso superior a 80 kg.
# f. Quantas pessoas em porcentagem são do sexo masculino e quantas são do sexo feminino.
# # No final do exercício, imprima também quantas pessoas não são do sexo masculino

idade_superior_18 = 0
idade_total = 0
idade_mais_idosa = 0
idade_mais_jovem = 0
cabelos_castanhos = 0
cabelos_pretos = 0
cabelos_loiros = 0
cabelos_outros = 0
altura_superior_170 = 0
peso_superior_80 = 0
sexo_masculino = 0
sexo_feminino = 0
pessoas_nao_masculinas = 0

for _ in range(1000):
    idade = int(input("Digite a idade: "))
    cor_cabelo = input("Digite a cor do cabelo (Castanhos, Pretos, Loiros ou Outro): ")
    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em kg): "))
    sexo = input("Digite o sexo (Masculino ou Feminino): ")

    if idade > 18:
        idade_superior_18 += 1

    idade_total += idade

    if idade > idade_mais_idosa:
        idade_mais_idosa = idade

    if idade < idade_mais_jovem or idade_mais_jovem == 0:
        idade_mais_jovem = idade

    if cor_cabelo == "Castanhos":
        cabelos_castanhos += 1
    elif cor_cabelo == "Pretos":
        cabelos_pretos += 1
    elif cor_cabelo == "Loiros":
        cabelos_loiros += 1
    else:
        cabelos_outros += 1

    if altura > 1.70:
        altura_superior_170 += 1

    if peso > 80:
        peso_superior_80 += 1

    if sexo == "Masculino":
        sexo_masculino += 1
    else:
        sexo_feminino += 1

porcentagem_masculino = (sexo_masculino / 1000) * 100
porcentagem_feminino = (sexo_feminino / 1000) * 100

pessoas_nao_masculinas = 1000 - sexo_masculino

print("a. Pessoas com idade superior a 18 anos:", idade_superior_18)
print("b. Média das idades:", idade_total / 1000)
print("   Idade da pessoa mais idosa:", idade_mais_idosa)
print("   Idade da pessoa mais jovem:", idade_mais_jovem)
print("c. Porcentagem de pessoas com cabelos castanhos:", (cabelos_castanhos / 1000) * 100)
print("   Porcentagem de pessoas com cabelos pretos:", (cabelos_pretos / 1000) * 100)
print("   Porcentagem de pessoas com cabelos loiros:", (cabelos_loiros / 1000) * 100)
print("   Porcentagem de pessoas com cabelos de outra cor:", (cabelos_outros / 1000) * 100)
print("d. Pessoas com altura superior a 1.70 m:", altura_superior_170)
print("e. Pessoas com peso superior a 80 kg:", peso_superior_80)
print("f. Porcentagem de pessoas do sexo masculino:", porcentagem_masculino)
print("   Porcentagem de pessoas do sexo feminino:", porcentagem_feminino)
print("   Quantidade de pessoas não do sexo masculino:", pessoas_nao_masculinas)
