
#Serão lidos N número, faça um algortimo que escreva o maior e o menor valor informado

N = int(input('Quantos números serão digitados: '))
maiorNumero = 0
menorNumero = 0
for numero in range (1, N+1):
  numeroDigitado =int(input("Digite um número: "))
  if numero == 1:
    maiorNumero = numeroDigitado
    menorNumero = numeroDigitado
  if maiorNumero < numeroDigitado: maiorNumero = numeroDigitado
  if menorNumero > numeroDigitado: menorNumero = numeroDigitado

print(f'O menor numero é {menorNumero}.')
print(f'O maior numero é {maiorNumero}.')
