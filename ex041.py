#41. Repita o exercício anterior para um número indefinido de bois.

maior_peso = float('-inf')
menor_peso = float('inf')
soma_pesos = 0
contador = 0
bois_mais_pesados = []
bois_mais_magros = []

while True:
    peso = float(input("Digite o peso do boi (ou 0 para sair): "))
    
    if peso == 0:
        break

    contador += 1
    soma_pesos += peso
    
    if peso > maior_peso:
        maior_peso = peso
        bois_mais_pesados = [contador]
    elif peso == maior_peso:
        bois_mais_pesados.append(contador)
    
    if peso < menor_peso:
        menor_peso = peso
        bois_mais_magros = [contador]
    elif peso == menor_peso:
        bois_mais_magros.append(contador)

mensagem_mais_pesados = ""
mensagem_mais_magros = ""

if len(bois_mais_pesados) > 1:
    mensagem_mais_pesados = "Há mais de um boi com o maior peso."
if len(bois_mais_magros) > 1:
    mensagem_mais_magros = "Há mais de um boi com o menor peso."

media_pesos = soma_pesos / contador

print("\n--- Resultados ---")
print(f"Número do boi mais pesado: {bois_mais_pesados}kg")
print(f"Número do boi mais magro: {bois_mais_magros}kg")
print(f"Média de pesos dos bois: {media_pesos}kg")
print(mensagem_mais_pesados)
print(mensagem_mais_magros)
