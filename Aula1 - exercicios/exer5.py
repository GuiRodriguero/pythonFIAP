litroP = float(input("Digite o preço do litro da gasolina: "))
pag = float(input("Digite quantos reais o cliente deseja gastar com a gasolina: "))

if litroP > 0 and pag > 0:
    print("A gasolina custa ", litroP, " o litro, e o motorista deseja abastecer ", pag, " reais.")
    print("Serão comprados ", pag/litroP, " litros de gasolina.")
else:
    print("Digite um valor maior que zero")