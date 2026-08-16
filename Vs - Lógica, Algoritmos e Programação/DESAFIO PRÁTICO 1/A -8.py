'''8. Ajude um hotel da cidade a calcular o valor da hospedagem. O hotel cobra R$ 290,00 a diária e mais uma taxa de serviços. A taxa de serviços é de:
• R$ 6,50 por dia, se o número de diárias for maior que 7;
• R$ 12,00 por dia, se o número de diárias for igual a 7;
• R$ 16,50 por diária, se o número de diárias for menor que 7.
Você deve pedir a informação de quantos dias o hóspede ficou hospedado. Construa um código que mostre o nome do hóspede e o total da conta a pagar.'''
nome_hospede = input("DIGITE O NOME DO HÓSPEDE: ").capitalize()
qtd_diaria = int(input("DIGITE A QUANTIDADE DE DIAS HOSPEDADO: ")) # 290 + dias 

if qtd_diaria > 7:
    valor_cobrado = 290 + (6.50 * qtd_diaria)
    print(f"O hóspede {nome_hospede} terá que pagar R$ {valor_cobrado:.2f}.")
elif qtd_diaria == 7:
    valor_cobrado = 290 + (12 * qtd_diaria)
    print(f"O hóspede {nome_hospede} terá que pagar R$ {valor_cobrado:.2f}.")
else:
    valor_cobrado = 290 + (16.50 * qtd_diaria)
    print(f"O hóspede {nome_hospede} terá que pagar R$ {valor_cobrado:.2f}.")