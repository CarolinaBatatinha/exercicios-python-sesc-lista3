# Faça um programa para escrever os números primos até um número informado pelo usuário.

limite = int(input("Digite um número: "))

if limite < 2:
    print("Não existem números primos até o número informado.")
else:
    print(f"Números primos até {limite}: ")
    for num in range(2, limite + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
