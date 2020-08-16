numeros = ([0]*10)
soma = 0
negativos = 0

for x in range(len(numeros)):
    numeros[x] = int(input("Digite um número: "))

for x in range(len(numeros)):
    if numeros[x] > 0:
        soma += numeros[x]
print("Soma dos valores positivos: ", soma)

for x in range(len(numeros)):
    if numeros[x] < 0:
        negativos += 1
print("\nQuantidade de valores negativos: ", negativos)

