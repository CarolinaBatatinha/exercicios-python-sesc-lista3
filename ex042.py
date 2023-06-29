#42. Você foi contratado pelo melhor time de futebol do mundo, para fazer um programa que: durante um jogo de futebol, leia um fato ocorrido no jogo, este fato pode ser :
# 0- Fim da partida
# 1- Faltas cometidas
# 2- Faltas recebidas
# 3- Escanteios a Favor
# 4- Passes Errados
# 5- Chutes a gol
# Ao final da partida o programa deverá imprimir os totais de cada fato.

fimPartida = 0
faltasCometidas = 0
faltasRecebidas = 0
escanteios = 0
passesErrados = 0
chutesGol = 0

while True:
    fato = int(input("Digite o código do fato ocorrido (0 - Fim da partida, 1 - Faltas cometidas, 2 - Faltas recebidas, 3 - Escanteios a Favor, 4 - Passes Errados, 5 - Chutes a gol): "))

    if fato == 0:
        fimPartida += 1
        break
    elif fato == 1:
        faltasCometidas += 1
    elif fato == 2:
        faltasRecebidas += 1
    elif fato == 3:
        escanteios += 1
    elif fato == 4:
        passesErrados += 1
    elif fato == 5:
        chutesGol += 1
    else:
        print("Código de fato inválido. Tente novamente.")

print("\n===== Totais de fatos ocorridos no jogo =====")
print(f"Fim da partida: {fimPartida}")
print(f"Faltas cometidas: {faltasCometidas}")
print(f"Faltas recebidas: {faltasRecebidas}")
print(f"Escanteios a favor: {escanteios}")
print(f"Passes errados: {passesErrados}")
print(f"Chutes a gol: {chutesGol}")
