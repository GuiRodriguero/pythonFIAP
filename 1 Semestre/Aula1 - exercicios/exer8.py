valor = float(input("Digite o valor do boleto: "))
percent = float(input("Digite o percentual de juros cobrado: "))
dia = int(input("Digite a quantidade de dias atrasados: "))



novoValor = valor + (valor*(percent/100)) * dia

if valor > 0 and percent > 0 and dia > 0:
    print("Valor a ser pago com juros: ", novoValor)
else:
    print("Digite um valor maior que zero")