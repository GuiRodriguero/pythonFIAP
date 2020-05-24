import random

numero = random.randint(0,100)
chute = 0
cont = 1

print("Tente adivinhar o número entre 0 e 100")

while chute != numero:
    print("Tentativa número ", cont, ": ")
    chute = int(input(""))
    if chute < numero:
        print("***CHUTOU BAIXO***")
    else:
        print("***CHUTOU ALTO***")

    if chute == numero:
        print("ACERTOU! VOCÊ PERCISOU DE ", cont, " TENTATIVAS")

    cont += 1