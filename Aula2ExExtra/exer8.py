preco = float(input("Digite o preço de um produto: "))
desconto = float(input("Desconto: %"))

desconto = desconto / 100
valorDesconto = preco * desconto
novoPreco = preco - valorDesconto

print("Valor do desconto: ", valorDesconto)
print("Preço com desconto: ", novoPreco)