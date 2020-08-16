numeros = ([0]*15)

for x in range(len(numeros)):
    numeros[x] = int(input("Digite um número: "))



print("Número igual a 30 nas posições: ", end ="")

for y in range(len(numeros)):
    if numeros[y] == 30:
        print(y+1, " ", end="")
