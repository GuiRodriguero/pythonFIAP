print("Notas: A - Ótimo B – Bom C – Regular D – Ruim E - Péssimo")

notaA = 0
notaB = 0
notaC = 0
notaD = 0
notaE = 0

maiorIdadeE = 0

qtdeNotaD = 0
idadeD = 0

qtdeNotaA = 0

cont = 0
while cont < 100:
    nota = input("Digite a nota para o filme: ").upper()
    idade = int(input("Digite a sua idade: "))

    if nota == "A":
        notaA += 1
        qtdeNotaA += 1

    if nota == "B":
        notaB += 1

    if nota == "C":
        notaC += 1

    if nota == "D":
        notaD += 1
        qtdeNotaD += 1
        idadeD += idade

    if nota == "E":
        notaE += 1
        if idade > maiorIdadeE:
            maiorIdadeE = idade

    cont += 1

print(qtdeNotaA, " pessoa(s) acharam o filme ÓTIMO.")
if qtdeNotaD > 0:
    print("Média de idade das pessoas que acharam o filme RUIM = ", (idadeD/qtdeNotaD))
else:
    print("Média de idade das pessoas que acharam o filme RUIM = 0")
print(notaE, "% julgaram o filme PÉSSIMO e a maior idade que escolheu essa opção foi ", maiorIdadeE," anos")
print((notaB+notaC), " pessoa(s) acharam o filme BOM ou REGULAR")