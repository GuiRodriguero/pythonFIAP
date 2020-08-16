print("EXERCÍCIO 15\n")

nome = input("Digite o nome do Aluno: ")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira aula do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

aulas = 80
porcentFalta = faltas/aulas
media = (n1+n2+n3)/3

if porcentFalta > 0.25:
    print("\n\Aluno(a) ", nome, " reporvado(a) por falta.")
elif media < 7:
    print("\nAluno(a) ", nome, " reprovado(a) por média.")
else:
    print("\nAluno(a) ", nome, " passou de ano!")