print("EXERCÍCIO 10\n")
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro e descubra se o primero é divisível pelo segundo: "))

if n1 % n2 == 0:
    print(n1, " é divisível por ", n2)
else:
    print(n1, " não é divisível por ", n2)