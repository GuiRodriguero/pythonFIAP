h = float(input("Digite a altura da lata: "))
r = float(input("Digite o valor do raio da lata: "))

vol = 3.14 * (r*r) * h
vol = round(vol, 2)

if h > 0 and r > 0:
    print("O volume da lata é: ", vol)
else:
    print("Digite um valor maior que zero")