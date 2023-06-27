# Uma empresa está fazendo análise de uma determinada população. Os seguintes dados são obtidos das pessoas:
#     a. Idade
#     b. Cor de Cabelos (Castanhos, Pretos, Loiros ou Outro)
#     c. Altura   
#     d. Peso
#     e. Sexo (Masculino ou Feminino)
# Faça um algoritmo para mostrar, ao final do processamento os seguintes dados:
#     a. Quantas pessoas possuem idade superior a 18 anos
#     b. Qual é a média das idades, a idade da pessoa mais idosa e a idade da pessoa mais jovem?
#     c. Quantas pessoas em porcentagem possuem cabelos castanhos, pretos, loiros e outros?
#     d. Quantas pessoas possuem altura superior a 1,70 m
#     e. Quantas pessoas peso superior a 80 kg.
#     f. Quantas pessoas em porcentagem são do sexo masculino e quantas são do sexo feminino.

idadeSuperior18 = 0
somaIdades = 0
qtdePessoas = 0
maiorIdade = 0
menorIdade = float('inf')
cabeloCastanho = 0
cabeloPreto = 0
cabeloLoiro = 0
cabeloOutro = 0
alturaMaior170 = 0
pesoSuperior80 = 0
qtdeMasc = 0
qtdeFem = 0

while True:
    idade = int(input('Digite sua idade: '))

    if idade < 0:
        break

    corCabelo = input('Digite a cor do seu cabelo(Castanho/ Preto/ Loiro/ Outro): ')
    altura = float(input('Digite sua altura em metros: '))
    peso = float(input('Digite seu peso em kg: '))
    genero = input('Digite seu gênero: ')

    if idade > 18:
        idadeSuperior18 += 1
    
    somaIdades += idade
    qtdePessoas += 1

    if idade > maiorIdade:
        maiorIdade = idade

    if idade < menorIdade:
        menorIdade = idade

    if corCabelo == "Castanho":
        cabeloCastanho += 1
    elif corCabelo == "Preto":
        cabeloPreto += 1
    elif corCabelo == "Loiro":
        cabeloLoiro += 1
    else:
        cabeloOutro += 1

    if altura > 1.70:
        alturaMaior170 += 1
    
    if peso > 80:
        pesoSuperior80 += 1

    if genero == "feminino":
        qtdeFem += 1
    elif genero ==" masculino":
        qtdeMasc += 1

    mediaIdade = somaIdades / qtdePessoas

    porcentCastanho = (cabeloCastanho / qtdePessoas) * 100
    porcentPreto = (cabeloPreto / qtdePessoas) * 100
    porcentLoiro = (cabeloLoiro / qtdePessoas) * 100
    porcentOutro = (cabeloOutro / qtdePessoas) * 100

    porcentMasc = (qtdeMasc / qtdePessoas) * 100
    porcentFem = (qtdeFem / qtdePessoas) * 100

print(f'Quantidade de pessoas com idade superior a 18 anos: {idadeSuperior18} ')
print(f'Média das idades: {mediaIdade}')
print(f'Idade da pessoa mais idosa: {maiorIdade}')
print(f'Idade da pessoa mais jovem: {menorIdade}')
print(f'Porcentagem de pessoas com cabelos castanhos: {porcentCastanho:.2f}%')
print(f'Porcentagem de pessoas com cabelos pretos: {porcentPreto:.2f}%')
print(f'Porcentagem de pessoas com cabelos loiros: {porcentLoiro:.2f}%')
print(f'Porcentagem de pessoas com cabelos outros: {porcentOutro:.2f}%')
print(f'Quantidade de pessoas com altura superior a 1,70 m: {alturaMaior170}')
print(f'Quantidade de pessoas com peso superior a 80 kg: {pesoSuperior80}')
print(f'Porcentagem de pessoas do sexo masculino: {porcentMasc:.2f}%')
print(f'Porcentagem de pessoas do sexo feminino: {porcentFem:.2f}%')
