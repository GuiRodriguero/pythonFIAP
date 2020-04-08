preco = float(input("Digite o preço do produto: "))
categoria = int(input("Digite a categoria do produto: (1 - limpeza, 2 - alimentação ou 3 - vestuário): "))
situacao = input("Digite a situação do produto:  (R - produtos que necessitam de refrigeração e N - produtos que não necessitam de refrigeração): ").upper()

if preco > 0:
    if preco <= 25:
        if categoria == 1:
            precoAumentado = preco * 0.05
            print("Valor do aumento: ", precoAumentado)
        if categoria == 2:
            precoAumentado = preco * 0.08
            print("Valor do aumento: ", precoAumentado)

        if categoria == 3:
            precoAumentado = preco * 0.1
            print("Valor do aumento: ", precoAumentado)

    if preco > 25:
        if categoria == 1:
            precoAumentado = preco * 1.12
            print("Valor do aumento: ", precoAumentado)
        if categoria == 2:
            precoAumentado = preco * 1.15
            print("Valor do aumento: ", precoAumentado)
        if categoria == 3:
            precoAumentado = preco * 1.18
            print("Valor do aumento: ", precoAumentado)

    if categoria == 2 or situacao == "R":
        precoImposto = preco * 0.05
        print("Valor do imposto: ", precoImposto)
    else:
        precoImposto = preco * 0.08
        print("Valor do imposto: ", precoImposto)

    novoPreco = (preco + precoAumentado) - precoImposto

    if novoPreco <= 50:
        classificacao = "Barato"
    elif novoPreco > 50 and novoPreco <= 120:
        classificacao = "Normal"
    else:
        classificacao = "Caro"

    print("Novo preço do produto: ", novoPreco)
    print("Classificação do produto: " + classificacao)

else:
    print("Valor inválido!")

