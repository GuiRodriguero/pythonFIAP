num = 0
soma = 0
cont = 1

while cont <= 500: #500/3 == 166,6
    num += 1
    if num % 2 == 1 and num % 3 == 0:
        soma += num
    cont += 1
print("Soma total: ", soma)