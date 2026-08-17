'''Classificador de Triângulos. Peça ao usuário para digitar o comprimento de três lados de um triângulo. Determine se os lados formam um triângulo válido e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno.
Regras:
a) Para ser um triângulo, a soma de dois lados deve ser maior que o terceiro
lado (a + b > c, a + c > b, b + c > a).
b) Equilátero: Todos os três lados são iguais.
c) Isósceles: Dois lados são iguais.
d) Escaleno: Todos os três lados são diferentes.'''
print("CLASSIFICADOR DE TRIÂNGULOS")
primeiro_lado = int(input("DIGITE O COMPRIMENTO DO PRIMEIRO LADO DO TRIÂNGULO: "))
segundo_lado = int(input("DIGITE O COMPRIMENTO DO SEGUNDO LADO DO TRIÂNGULO: "))
terceiro_lado = int(input("DIGITE O COMPRIMENTO DO TERCEIRO LADO DO TRIÂNGULO: "))

#Matematicamente, para lados a, b e c, todas as seguintes condições devem ser satisfeitas simultaneamente: a < b + c || b < a + c || c < a + b
if (primeiro_lado < (segundo_lado + terceiro_lado)) and (segundo_lado < (primeiro_lado + terceiro_lado)) and (terceiro_lado < (primeiro_lado + segundo_lado)):
    print("É um triângulo válido!")
    if primeiro_lado == segundo_lado == terceiro_lado:
        print("CLASSIFICAÇÃO: Triângulo Equilátero. Todos os três lados são iguais.")
    elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
        print("CLASSIFICAÇÃO: Triângulo Isósceles. Dois lados são iguais.")
    else:
        print("CLASSIFICAÇÃO: Triângulo Escaleno. Todos os três lados são diferentes.")
else:
    print("Com as medidas definidas, o triângulo não é considerado válido.")