num2 = 1
numAtual = 1
aux = 1

escolha = int(input("Digite  a quantidade de números que você deseja na sequência Fibonacci: "))
cont = 3

print(num2)
print(num2)

while cont <= escolha:
    numAtual = aux
    numAtual += num2
    aux = num2
    num2 = numAtual
    print(numAtual)

    cont += 1

