# Escrever um algoritmo que um número indefinido de valores, para cada entrada de dados a entrada de 2 valores, o primeiro representando o número de um aluno, e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e do mais baixo, junto com suas alturas.

alunoMaisAlto = 0
maiorAltura = 0
alunoMenosAlto = 0 
menorAltura = float('inf') # um valor infinito para garantir que a primeira altura inserida será menor

while True:
    numeroAluno = int(input('Digite o número do aluno, ou digite 0 para encerrar o programa: '))

    if numeroAluno == 0:
        break

    altura = int(input('Digite a altura desse aluno em centímetros (cm): '))
    
    if altura > maiorAltura:
        maiorAltura = altura
        alunoMaisAlto = numeroAluno
        
    if altura < menorAltura:
        menorAltura = altura
        alunoMenosAlto = numeroAluno

# Exibe o número e a altura do aluno mais alto e do mais baixo
print(f'Aluno mais alto: Número {alunoMaisAlto} - Altura {maiorAltura}cm')
print(f'Aluno mais baixo: Número {alunoMenosAlto} - Altura {menorAltura}cm')
