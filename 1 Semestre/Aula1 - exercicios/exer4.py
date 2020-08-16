dolar = float(input("Quanto está a cotação do dólar no dia de hoje? "))
real = float(input("Quantos reais você possui? "))

if dolar > 0 and real > 0:
    print("Você poderá comprar ", real/dolar, " dólares.")
else:
    print("Digite um valor maior que zero")