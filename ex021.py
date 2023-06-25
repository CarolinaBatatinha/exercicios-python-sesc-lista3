# 21. Faça um programa que calcule e escreva o valor de S.
#         1         3         5             99
# S = -------- + ------- + ------- + ... + -----
#         1         2         3             50

soma = 0

for cont in range(1, 51):
    numerador = 2 * cont - 1
    denominador = cont
    termo = numerador / denominador
    soma += termo

print(f'O valor de S é {soma:.2f}.')
