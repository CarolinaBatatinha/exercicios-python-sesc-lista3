# Faça um algoritmo para ler um número até que o usuário deseja terminar a entrada dos dados e, receber as seguintes informações: a média dos números, o maior e o menor número.
maiorNum = float('-inf')
menorNum = float('inf')
soma = 0
cont = 0

while True:
    num = int(input('Digite um número inteiro positivo. Para encerrar o programa, digite um número negativo: '))
    if num < 0:
        break
    
    if num >= 0:
        soma += num
        cont +=1

    if num > maiorNum:
        maiorNum = num

    if num < menorNum:
        menorNum = num

media = soma / cont

print(f'A média dos números digitados é {media}.')
print(f'O maior número digitado foi {maiorNum}.')
print(f'O menor número digitado foi {menorNum}.')
