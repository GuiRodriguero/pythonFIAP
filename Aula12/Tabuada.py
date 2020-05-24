tabuada = 1
multiplicador = 1
resultado = 0

while tabuada < 10:

    while multiplicador <= 10:
        resultado = tabuada * multiplicador
        print(tabuada, " x ", multiplicador, " = ", resultado)
        multiplicador += 1

        if multiplicador > 10:
            print("\n")

    multiplicador = 1
    tabuada += 1