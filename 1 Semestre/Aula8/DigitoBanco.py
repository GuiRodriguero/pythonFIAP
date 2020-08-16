digito = int(input("Digite o número da usa conta: "))
centena = int(digito//100)
dezena = int((digito % 100) // 10)
unidade = (digito % 10)

unidade *= 100
dezena*= 10

invertido = digito + centena + dezena + unidade

if invertido < 1000:
    centena = int(invertido // 100)
    dezena = int(((invertido % 100) // 10)*2)
    unidade = ((invertido % 10)*3)

    valor = centena + dezena + unidade
    verificador = valor % 10
else:
    milenio = int(invertido // 1000)
    centena = int(((invertido // 1000) // 100) *2)
    dezena = int(((invertido % 1000) // 10)*3)
    unidade = ((invertido % 100)*4)

    valor = milenio + centena + dezena + unidade
    verificador = valor % 10

print ("O número verificador da sua conta é: ", verificador)

