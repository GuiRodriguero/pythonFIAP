#1) Faça um programa  em Python que receba do usuário sete números inteiros, calcule e mostre:
#a) Os números múltiplos de 2;
#b) Os números múltiplos de 3;

numeros = ([0]*7)
dois = ([0]*7)
tres = ([0]*7)

for x in range(len(numeros)):
    numeros[x] = int(input("Digite um número: "))

print("Número múltiplo de 2 = ", end="")
for dois in range(len(numeros)):
    if numeros[dois] % 2 == 0:
        print(dois + 1, " ", end="")


print("\nNúmero múltiplo de 3 = ", end="")
for impar in range(len(numeros)):
    if numeros[impar] % 3 == 0:
        print(impar + 1, " ", end="")