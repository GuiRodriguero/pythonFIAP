escolha = "S"
while escolha == "S":
    tabuada = int(input("Digite um número para descobrir a sua tabuada: "))
    multiplicador = 1
    resultado = 0

    while multiplicador <= 10:
        resultado = tabuada * multiplicador
        print(tabuada, " x ", multiplicador, " = ", resultado)
        multiplicador += 1

    escolha = input("Deseja contnuar? (S/N) ").upper()


