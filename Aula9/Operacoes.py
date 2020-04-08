print("EXERCÍCIO 18\n")
opcao = int(input("Menu de Opções\n"
                  "1. Somar dois números\n"
                  "2. Raíz quadrada de um número\n"
                  "Digite a opção desejada: "))

if opcao == 1:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    print("Soma entre os dois números: ", (n1+n2))

if opcao == 2:
    n1 = float(input("Digite um número: "))
    print("Raíz quadrada: ", (n1 ** (1/2)))
else:
    print("Programa encerrado.")