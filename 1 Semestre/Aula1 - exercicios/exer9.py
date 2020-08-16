print("Get Rich or Die Tryin'.")
sal = float(input("Digite seu salário: "))
desp = float(input("Digite suas despezas mensais: "))

sobra = sal - desp
milionario =  1000000 / sobra
ano = milionario / 12
meses = milionario % 12
ano = round(ano, 2)
meses = round(meses, 2)

if ano < 1:
    ano = 0
    
if sal > 0 and desp > 0:
    print("\n Você levará ", ano, "  ano(s) ", " e ", meses, " meses para ser milionário.")
else:
    print("Digite um valor maior que zero")