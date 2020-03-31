print("::RESULTADOS DA ELEIÇÃO::")

a = int(input("Digite quantos votos o candidato A recebeu: "))
b = int(input("Digite quantos votos o candidato B recebeu: "))
c = int(input("Digite quantos votos o candidato C recebeu: "))
branco = int(input("Digite a quantidade de votos brancos: "))
nulo = int(input("Digite a quantidade de votos nulos: "))

total = a + b + c + branco + nulo
totalV = a + b + c
totalBN = branco + nulo


if a < 0 or b < 0 or c < 0 or branco < 0 or nulo < 0:
    print("=====================================")
    print("Favor digite valores maiores que 0.")
else:
    print("=====================================")
    print("PERCENTUAL -> TOTAL")
    print("Número total de eleitores: ", total)
    print ("Votos válidos: ", totalV, " = ", round((totalV/total) * 100), "%")
    print("Votos Nulos: ", nulo, " = ", round((nulo/total) * 100), "%  || Votos Brancos: ", branco, " = ", round((branco/total) * 100), "%")
    print("=====================================")
    print("PERCENTUAL -> CANDIDATOS")
    print("Candidato A: ", round((a / totalV) * 100), "%")
    print("Candidato B: ", round((b / totalV) * 100), "%")
    print("Candidato C: ", round((c / totalV) * 100), "%")
    print("=====================================")
    print("PERCENTUAL -> BRACO X NULO")
    print("Votos Nulos: ", round((branco / totalBN) * 100), "%")
    print("Votos Brancos: ", round((nulo / totalBN) * 100), "%")