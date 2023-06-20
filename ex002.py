# Faça um algoritmo para imprimir o nome o nome da disciplina e um “beep” um número de vezes determinado pelo usuário.
beepsVezes = int(input('Digite quantas vezes vai soar o beep: '))
disciplina = input('Qual disciplina você prefere?: ')


for x in range(beepsVezes):
    print(f'{disciplina} *BEEEEEEP*')