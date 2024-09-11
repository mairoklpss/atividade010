# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.
num = int(input("digite um némero: "))

# Verificar se o número é par ou ímpar.
div = num % 2
if (div == 0):
    print(f"{num} é um número par.")
else:
    print(f"{num} é um número ímpar.")
