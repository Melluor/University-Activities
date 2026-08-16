# 2. Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como
# "Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" (65 anos ou mais).
idade_pessoa = int(input("DIGITE SUA IDADE: "))

if idade_pessoa <= 12:
    print("CLASSIFICAÇÃO: CRIANÇA.")
if idade_pessoa > 12 and idade_pessoa <= 17:
    print("CLASSIFICAÇÃO: ADOLESCENTE.")
if idade_pessoa > 17 and idade_pessoa <= 64:
    print("CLASSIFICAÇÃO: ADULTO.")
if idade_pessoa > 64:
    print("CLASSIFICAÇÃO: IDOSO.")