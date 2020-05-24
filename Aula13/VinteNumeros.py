cont = 2

num1 = 0
maior = 0
menor = 0

num1 = int(input("Digite um número: "))
print("Número 1 de 20")

menor = num1
while cont <= 19:
    num1 = int(input("Digite um número: "))
    print("Número ", cont, " de 20")


    if num1 > maior:
        maior = num1

    if num1 < menor:
        menor = num1

    cont += 1
print("Maior número: ", maior)
print("Menor número: ", menor)
