print("EXERCÍCIO 17\n")

valorCompra = float(input("Digite o valor de compra do produto: "))
lucro = 0

if valorCompra > 0:
    if valorCompra < 20:
         valorCompra *=  1.45
         print("Valor final: ", valorCompra)
    else:
        valorCompra *= 1.3
        print("Valor final: ", valorCompra)
else:
    print("Valor inválido.")
