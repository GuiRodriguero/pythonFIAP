alunoCTP = int(input("Quantos alunos temos na disciplina CTP? "))
alunoDDD = int(input("Quantos alunos temos na disciplina DDD? "))

ctp = ([0]*alunoCTP)
ddd = ([0]*alunoDDD)

print("Alunos de CTP: ")
for x in range(len(ctp)):
    print(x+1, ": ",  end="")
    ctp[x] = input("Digite a matrícula do aluno: ")

print("===============================")

print("Alunos de DDD: ")
for x in range(len(ddd)):
    print(x+1, ": ",  end="")
    ddd[x] = input("Digite a matrícula do aluno: ")

print("Nª matrículas CTP: ", ctp)
print("Nª matrículas DDD", ddd)