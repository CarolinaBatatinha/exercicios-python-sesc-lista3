#Crie uma tabela de conversão de polegada para centímetros. A tabela deve conter valores de 1 a 100 polegadas. Cada polegada equivale a 2,54 cm.
polegadaEmCm = 2.54

print("Tabela de conversão de Polegadas para Centímetros:")
print("===============================================")
print("Polegadas\tCentímetros")

for polegada in range(1, 101):
    cm = polegada * polegadaEmCm
    print(f'{polegada}\t\t{cm:.2f}')
