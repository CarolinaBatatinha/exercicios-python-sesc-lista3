# Uma determinada universidade pretende desenvolver uma pesquisa através dos seus alunos matriculados. Para cada aluno será digitado um dos códigos 1,2 e 3 que significam:
#     • 1 indica que o aluno cursa Administração
#     • 2 indica que o aluno cursa Administração com gestão em Informática
#     • 3 indica que o aluno cursa Sistemas de Informação.
# Deseja-se saber a porcentagem e o número de alunos por curso. Considere um número indeterminado de alunos matriculados.

matriculados = 0
alunosAdm = 0
alunosGestao = 0
alunosSI = 0

while True:
    curso = int(input('Em qual curso você está matriculado? \n(1 - Administração/ 2 - Administração com Gestão em Informática/ 3 - Sistemas de Informação/ 4 - Encerra o programa): \n'))

    matriculados += 1
    if curso == 1:
        alunosAdm += 1
    elif curso == 2:
        alunosGestao += 1
    elif curso == 3:
        alunosSI += 1
    else:
        break

    porcentAdm = (alunosAdm/ matriculados) * 100
    porcentGestao = (alunosGestao/matriculados) * 100
    porcentSI = (alunosSI/matriculados) * 100

print(f'O curso de Administração tem {alunosAdm} alunos e esse número corresponde a {porcentAdm}% dos alunos matriculados.')
print(f'O curso de Administração com Gestão em Informática tem {alunosGestao} alunos e esse número corresponde a {porcentGestao}% dos alunos matriculados.')
print(f'O curso de Sistemas de Informação tem {alunosSI} alunos e esse número corresponde a {porcentSI}% dos alunos matriculados.')

