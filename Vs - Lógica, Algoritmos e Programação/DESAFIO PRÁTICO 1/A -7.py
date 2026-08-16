'''7. Uma empresa de vendas possui corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for até R$ 500.000 a comissão será de 6% do valor vendido. Se o valor da venda do corretor estiver acima de R$ 500.000 até R$ 700.000 a comissão será de 8.5%. Se o valor da venda do corretor estiver acima de R$ 700.000 até R$ 1.000.000 a comissão será de 10%. Se o valor da venda de um corretor for maior que R$ 1.000.000 a comissão será de 12% do valor vendido. Escreva um código que imprima um relatório contendo o nome, valor da venda e a comissão do corretor.'''
nome_corretor = input("DIGITE O NOME DO CORRETOR: ").capitalize()
valor_venda = float(input("DIGITE O VALOR DA VENDA: "))

if valor_venda <= 500000: #6%
    comissao = valor_venda * 0.06
    print(f"O Corretor {nome_corretor} realizou uma venda no valor de R$ {valor_venda:.2f} e adquiriu uma comissão de R$ {comissao:.2f}")
elif valor_venda > 500000 and valor_venda <= 700000: #8.5%
    comissao = valor_venda * 0.085
    print(f"O Corretor {nome_corretor} realizou uma venda no valor de R$ {valor_venda:.2f} e adquiriu uma comissão de R$ {comissao:.2f}")
elif valor_venda > 700000 and valor_venda <= 1000000: #10%
    comissao = valor_venda * 0.10
    print(f"O Corretor {nome_corretor} realizou uma venda no valor de R$ {valor_venda:.2f} e adquiriu uma comissão de R$ {comissao:.2f}")
else: #12%
    comissao = valor_venda * 0.12
    print(f"O Corretor {nome_corretor} realizou uma venda no valor de R$ {valor_venda:.2f} e adquiriu uma comissão de R$ {comissao:.2f}")