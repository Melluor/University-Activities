# 1. Verificador de Par ou Ímpar. Peça ao usuário um número inteiro e diga se ele é par ou ímpar.
numero = int(input("DIGITE UM NÚMERO: "))

if (numero % 2) == 0:
    print("O número digitado é par!")
else:
    print("O número digitado é ímpar!")