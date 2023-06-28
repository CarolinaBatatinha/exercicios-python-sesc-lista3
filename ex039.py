# Para eleição de representantes de classe de uma universidade há três candidatos. Os votos são informados através de código: 1,2 ou 3, voto para os respectivos candidatos, 5 voto nulo e 6 voto em branco. Faça um algoritmo que calcule e escreva:
# a. A porcentagem e o total de votos para cada candidato
# b. Total de votos nulos
# c. Total de votos em branco
# d. Percentual de votos em brancos e nulos
# e. Classificação dos candidatos
# f. Total de votos

# Inicialização das variáveis
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_nulos = 0
votos_em_branco = 0
total_votos = 0

# Loop para receber os votos até que seja digitado -1
while True:
    voto = int(input("Digite o código do candidato (1, 2, 3), 5 para voto nulo, 6 para voto em branco, ou -1 para encerrar: "))

    if voto == -1:
        break

    # Contabiliza os votos
    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1

    total_votos += 1

# Cálculo das porcentagens
porcentagem_candidato_1 = (votos_candidato_1 / total_votos) * 100
porcentagem_candidato_2 = (votos_candidato_2 / total_votos) * 100
porcentagem_candidato_3 = (votos_candidato_3 / total_votos) * 100
porcentagem_nulos = (votos_nulos / total_votos) * 100
porcentagem_em_branco = (votos_em_branco / total_votos) * 100

# Exibição dos resultados
print("Resultado da eleição:")
print("Total de votos para o candidato 1:", votos_candidato_1)
print("Total de votos para o candidato 2:", votos_candidato_2)
print("Total de votos para o candidato 3:", votos_candidato_3)
print("Total de votos nulos:", votos_nulos)
print("Total de votos em branco:", votos_em_branco)
print("Percentual de votos nulos:", porcentagem_nulos, "%")
print("Percentual de votos em branco:", porcentagem_em_branco, "%")

# Classificação dos candidatos
if votos_candidato_1 > votos_candidato_2 and votos_candidato_1 > votos_candidato_3:
    print("O candidato 1 foi o mais votado.")
elif votos_candidato_2 > votos_candidato_1 and votos_candidato_2 > votos_candidato_3:
    print("O candidato 2 foi o mais votado.")
elif votos_candidato_3 > votos_candidato_1 and votos_candidato_3 > votos_candidato_2:
    print("O candidato 3 foi o mais votado.")
else:
    print("Houve um empate entre os candidatos.")

print("Total de votos:", total_votos)
