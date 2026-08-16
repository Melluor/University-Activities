# 3. Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher entre as operações de soma, subtração, multiplicação e divisão. Peça dois números e a operação desejada. Imprima o resultado.
operacao = int(input('''
== ESCOLHA A OPERAÇÃO ==
1. SOMA
2. SUBTRAÇÃO
3. MULTIPLICAÇÃO
4. DIVISÃO
'''))

numero_1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
numero_2 = float(input("DIGITE O SEGUNDO NÚMERO: "))

match operacao:
    case 1:
        soma = numero_1 + numero_2
        print(f"O resultado da soma dos números é: {soma}")
    case 2:
        subtracao = numero_1 - numero_2
        print(f"O resultado da subtração dos números é: {subtracao}")
    case 3:
        multiplicacao = numero_1 * numero_2
        print(f"O resultado da multiplicação dos números é: {multiplicacao}")
    case 4:
        if numero_2 == 0:
            print('Operação inválida! Não é possível dividir por 0.')
        divisao = numero_1 / numero_2
        print(f"O resultado da divisão dos números é: {divisao}")
    case _:
        print(f"Não foi possível realizar a operação escolhida. Por favor, digite uma escolha válida.")