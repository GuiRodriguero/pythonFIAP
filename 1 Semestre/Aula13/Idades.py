nIdade = int(input("Quantas idades você deseja inserir? "))

idade18 = 0
maior18 = 0
menor18 = 0

somaIdades = 0

maiorIdade = 0
qtdeMaiorIdade = 0

menorIdade = 0
qtdeMenorIdade = 0

cont = 1
while cont <= nIdade:
    idade = int(input("Digite a idade: "))
    if idade >= 0:

        if cont == 1: #primeira vez que entra no laço
            menorIdade = idade
            maiorIdade = idade

        if cont >= 1:
            if idade < 18:
                menor18 += 1
            if idade == 18:
                idade18 += 1
            if idade > 18:
                maior18 += 1

            if maiorIdade <= idade:
                if maiorIdade < idade:
                    maiorIdade = idade
                    qtdeMaiorIdade = 1
                else:
                    qtdeMaiorIdade += 1

            if menorIdade >= idade:
                if menorIdade > idade:
                    menorIdade = idade
                    qtdeMenorIdade = 1
                else:
                    qtdeMenorIdade += 1

        somaIdades += idade
        cont += 1
    else:
        print("Digite uma idade maior ou igual a 0")

print(idade18, " pessoa(s) tem 18 anos")
print(maior18, " pessoa(s) tem mais que 18 anos")
print(menor18, " pessoa(s) tem menos que 18 anos")
print("A soma de todas as idades é: ", somaIdades)
print("A média das idades digitadas é: ", somaIdades/nIdade)
print("A maior idade é: ", maiorIdade, " e ", qtdeMaiorIdade, " pessoa(s) tem essa idade")
print("A menor idade é: ", menorIdade, " e ", qtdeMenorIdade, " pessoa(s) tem essa idade")

