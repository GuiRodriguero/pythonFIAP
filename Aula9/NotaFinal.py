print("EXERCÍCIO 1\n")
trabalho = float(input("Digite a nota (0 a 10) do trabalho de laboratório: "))
avaliacao = float(input("Digite a nota (0 a 10) da avaliação semestral: "))
exameF = float(input("Digite a nota (0 a 10) do exame final: "))
conceito = ''
if trabalho >= 0 and avaliacao >=0 and exameF >= 0 and trabalho <= 10 and avaliacao <= 10 and trabalho <= 10:

    media = ((trabalho*2) + (avaliacao*3) + (exameF*5)) / 10
    if media < 5:
        conceito = 'E'
    elif media < 6:
        conceito = 'D'
    elif media < 7:
        conceito = 'C'
    elif media < 8:
        conceito = 'B'
    else:
        conceito = 'A'

    print("Nota de conceito: " + conceito)
else:
    print("Nota inválida")