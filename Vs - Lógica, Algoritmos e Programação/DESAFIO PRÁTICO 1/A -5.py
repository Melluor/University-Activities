'''5. Solicite os coeficientes a, b e c de uma equação do segundo grau (ax² + bx + c = 0). Determine e mostre o número de raízes reais distintas que a equação possui. Regra: O número de raízes reais depende do discriminante (delta), Δ = b² - 4ac:
• Δ > 0: Duas raízes reais distintas.
• Δ = 0: Uma raiz real (ou duas raízes reais iguais).
• Δ < 0: Nenhuma raiz real (duas raízes complexas).'''
print("DETERMINANDO A QUANTIDADE DE RAIZES DE UM DELTA")
coeficiente_a = float(input("DIGITE O COEFICIENTE A: "))
coeficiente_b = float(input("DIGITE O COEFICIENTE B: "))
coeficiente_c = float(input("DIGITE O COEFICIENTE C: "))

delta = (coeficiente_b ** 2) - (4 * coeficiente_a * coeficiente_c)

if delta > 0:
    print(f"O delta tem um valor maior que 0 ({delta}) e possui duas raízes reais distintas!")
elif delta == 0:
    print(f"O delta tem um valor igual a 0 ({delta}) e possui uma raiz real!")
else:
    print(f"O delta tem um valor menor que 0 ({delta}) e não possui nenhuma raiz real!")