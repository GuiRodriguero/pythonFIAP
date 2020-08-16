destino = int(input("Digite seu DESTINO: 1- Norte | 2- Nordeste | 3- Centro-Oeste : "))
if destino == 1 or destino == 2 or destino == 3:
    ida_volta = input("\nÉ uma passagem de Ida e Volta? (S/N) : ").upper()

    if ida_volta == "S" or "s":
        if destino == 1:
            print("Preço da Passagem Ida e Volta para Norte: R$400")
        if destino == 2:
            print("Preço da Passagem Ida e Volta para Nordeste: R$628")
        if destino == 3:
            print("Preço da Passagem Ida e Volta para Centro-Oeste: R$1100")

    elif ida_volta == "N" or "n":
        if destino == 1:
            print("Preço da Passagem de Ida para Norte: R$280")
        if destino == 2:
            print("Preço da Passagem de Ida para Nordeste: R$380")
        if destino == 3:
            print("Preço da Passagem de Ida para Centro-Oeste: R$620")

    else:
        print("Valor inválido")

