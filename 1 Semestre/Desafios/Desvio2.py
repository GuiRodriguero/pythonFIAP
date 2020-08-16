print("========================ESTACIONAMENTO SEMPRE BEM-VINDO ========================")
veiculo = input("O cliente deixou um carro ou uma moto? C/M ")
veiculo.upper()
tempo = int(input("Digite o tempo em minutos que o veículo ficou no estacionamento: "))

if tempo > 0:
    if tempo <= 15:
        preco = 0
    if tempo > 15 and tempo <= 180:
        if veiculo == "C":
            preco = 17
            print(" O cliente deixou estacionado seu carro por " + tempo + " minutos, então ele deve pagar R$" + preco + ",00")
        elif veiculo == "M":
            preco = 20
            print(" O cliente deixou estacionado sua moto por " + tempo + " minutos, então ele deve pagar R$" + preco + ",00")
    if tempo > 180:
        if veiculo == "C":
            adicional = (180 - tempo) * 0.1
            preco = 17 + adicional
            print(" O cliente deixou estacionado seu carro por " + tempo + " minutos, então ele deve pagar R$" + preco + ",00 (R$ 17,00 + " + adicional + ")")
        if veiculo == "M":
            adicional = (180 - tempo) * 0.15
            preco = 17 + adicional
            print(" O cliente deixou estacionado sua moto por " + tempo + " minutos, então ele deve pagar R$" + preco + ",00 (R$ 20,00 + " + adicional + ")")
else:
    print("Digite um tempo maior que 0!")