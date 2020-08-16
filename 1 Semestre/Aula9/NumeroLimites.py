print("EXERCÍCIO 16\n")

n1 = float(input("Digite um número: "))

if n1 >= 0 and n1 <= 30:
    print(n1, " está entre 0 e 30.")
elif n1 >= 40 and n1 < 80:
    print(n1, " está entre 40 e 79.")
else:
    print(n1, " está fora dos limites estabelecidos.")