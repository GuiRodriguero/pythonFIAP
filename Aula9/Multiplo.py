print("EXERCÍCIO 7\n")
n1 = int(input("Digtie um número inteiro: "))

if n1 != 0:
    if n1 % 5 == 0 and n1 % 10 == 0:
        print(n1, " é múltiplo de 5 e 10")
    else:
        print(n1, " não é múltiplo de 5 e 10 ao mesmo tempo")
else:
    print(n1, " não é múltiplo de 5 e 10 ao mesmo tempo")
