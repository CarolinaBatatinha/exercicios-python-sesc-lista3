# Fazer um programa que calcule e escreva o valor de S.
#      37*38      36*37     35*36           1*2
# S = -------- + ------- + ------- + ... + -----
#         1        2          3             37

S = 0
divisor = 1

for numerador in range(37, 0, -1):
    termo = (numerador * (numerador + 1)) / divisor
    S += termo
    divisor += 1

print("O valor de S é:", S)
