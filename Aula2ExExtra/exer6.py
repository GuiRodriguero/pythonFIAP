num = int(input("Digite um número entre 0 e 99: "))

if num >= 0 and num < 100:
    dezena = num // 10
    unidade = num % 10

    print("DEZENA: ", dezena)
    print("UNIDADE: ", unidade)
else:
    print("DIGITE UM NÚMERO ENTRE 0 E 99")