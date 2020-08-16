salario = float(input("Digite seu salário anterior: "))
novoSalario = float(input("Digite seu salário com aumento: "))

porcent = ((novoSalario/salario)*100)-100
round(porcent, 2)

print("Seu aumento foi de: ", porcent, "%")