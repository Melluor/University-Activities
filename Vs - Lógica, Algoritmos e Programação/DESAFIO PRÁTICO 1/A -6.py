'''6. Peça ao usuário a temperatura da água (em graus Celsius). Determine o estado físico da água (sólido, líquido ou gasoso). Regras:
• Temperatura <= 0: Sólido
• 0°C < Temperatura < 100°C: Líquido
• Temperatura >= 100°C: Gasoso'''
temperatura = float(input("DIGITE A TEMPERATURA DA ÁGUA (EM °C): "))

if temperatura <= 0:
    print("ESTADO FÍSICO: SÓLIDO.")
elif temperatura > 0 and temperatura < 100:
    print("ESTADO FÍSICO: LÍQUIDO.")
else:
    print("ESTADO FÍSICO: GASOSO.")