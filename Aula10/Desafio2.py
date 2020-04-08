horaExtra = float(input("Digite o número de horas extras do funcionário: "))
horaFalta = float(input("Digite o número de horas que o funcionário faltou: "))

h = horaExtra - ((2/3)*(horaExtra - horaFalta))

if horaExtra >= 0 and horaFalta >= 0:
    if h >= 2400:
        print("O funcioário receberá R$1500,00 de bonificação")
    if h < 2400 and h >= 1800:
        print("O funcioário receberá R$1000,00 de bonificação")
    if h < 1800 and h >= 1200:
        print("O funcioário receberá R$890,00 de bonificação")
    if h < 1200:
        print("O funcioário receberá R$500,00 de bonificação")
else:
    print("Valor de horas inválido.")