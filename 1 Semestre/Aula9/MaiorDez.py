print("EXERCÍCIO 8\n")
n1 = float(input("Digite um número"))
n2 = float(input("Digite outro número e descubra se a soma deles é maior que 10"))
soma = n1+n2

if soma > 10:
    print("Soma entre ", n1, "+", n2," maior que 10")
elif soma < 10:
    print("Soma entre ", n1, "+", n2," menor que 10")
else:
    print("Os números são iguais")
