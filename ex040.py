# Um Frigorífico possui 500 bois, e deseja saber o número do boi que possui o peso mais gordo e do boi que possui o peso mais magro e média de pesos dos bois. Cada boi possui um número de identificação. Faça o mesmo programa utilizando while, for ou do...while. Observação: se houver dois bois ou mais bois com o peso maior ou menor peso, o programa deverá informar o usuário no final da execução.

#Usando for

total_bois = 500
soma_pesos = 0
maior_peso = float("-inf")
menor_peso = float("inf")
bois_mais_gordos = []
bois_mais_magros = []

for contador in range(1, total_bois + 1):
    peso = float(input(f"Digite o peso do boi {contador}: "))
    soma_pesos += peso

    if peso > maior_peso:
        maior_peso = peso
        bois_mais_gordos = [contador]
    elif peso == maior_peso:
        bois_mais_gordos.append(contador)

    if peso < menor_peso:
        menor_peso = peso
        bois_mais_magros = [contador]
    elif peso == menor_peso:
        bois_mais_magros.append(contador)

media_pesos = soma_pesos / total_bois

print("\nResultado:")
print(f"O boi com o peso mais gordo é o boi(s) {bois_mais_gordos}, com peso {maior_peso}kg.")
print(f"O boi com o peso mais magro é o boi(s) {bois_mais_magros}, com peso {menor_peso}kg.")
print(f"A média de pesos dos bois é {media_pesos:.2f}kg.")
