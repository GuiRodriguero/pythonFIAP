# total_vendas = ([0]*10)
# comissao = ([0]*10)
# nomes = ([""]*10)

total_vendas = [100,200,1000]
comissao = [20,30,50]
nomes = ["João", "José", "Joaquim"]

soma_venda = 0

maior = 0
menor = total_vendas[0]

#A
print("Nomes: ", end="")
for nome in range(len(nomes)):
    print("  ", nomes[nome], "", end="")

print("\nComissão: R$ ", end="")
for comissao_i in range(len(comissao)):
    print(comissao[comissao_i], "   ", end="")

#B
for soma in range(len(total_vendas)):
    soma_venda += total_vendas[soma]
print("\n\nTotal de venda dos funcioários: R$ ", soma_venda)

#C
for x in range(len(total_vendas)):
    nome_maior = 0 #pega o indice do maior
    if total_vendas[x] > maior:
        maior = total_vendas[x]
        nome_maior = x

print("\nMaior Valor: R$ ", maior)
print("Funcionário: ", nomes[nome_maior])

#D
for y in range(len(total_vendas)):
    nome_menor = 0 #pega o indice do menor
    if total_vendas[y] <= menor:
        menor = total_vendas[y]
        nome_menor = y

print("\nMenor Valor: R$ ", menor)
print("Funcionário: ", nomes[nome_menor])
