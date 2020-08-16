def reajuste(salario,mensalidade):
    novo_salario = salario + (salario * 10/100)

    if novo_salario > 1500:
        nova_mensalidade = mensalidade - (mensalidade * 5/100)
    else:
        nova_mensalidade = mensalidade - (mensalidade * 8/100)

    return novo_salario,nova_mensalidade

sal = float(input("Digite seu salário: "))
mensalidade = float(input("Digite o valor da mensalidade:"))
valor_reajustado, mensalidade_reajustada = reajuste(sal,mensalidade)

print("Salário reajustado: " , valor_reajustado)
print("Mensalidade com desconto: ",mensalidade_reajustada )