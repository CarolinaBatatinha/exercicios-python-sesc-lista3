# Elabore um algoritmo para gerar uma tabela de conversão entre milhas e Km, iniciando em 0 Km e finalizado em 1000 Km, e varie de 100 Km em 100 Km, sabendo-se que : 1 Milha = 1852 m.

milhaEmMetros = 1852
inicioKm = 0
fimKm = 1000
variacaoKm = 100

print("Tabela de conversão entre Milhas e Quilômetros:")
print("=============================================")


for km in range(inicioKm, fimKm + 1, variacaoKm):
    milhas = km * milhaEmMetros / 1000
    print( 'Milhas\t\tQuilômetros')
    print('{:.2f}\t\t{}'.format(milhas, km))


