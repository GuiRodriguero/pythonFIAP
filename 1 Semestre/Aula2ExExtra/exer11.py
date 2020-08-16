rm = int(input("Digite seu RM: "))
cont = 0
divisor = 10000
total = 0
nrm = rm

print("RM: ", rm)

while cont < 5:

    nrm = rm // divisor
    rm = rm % divisor

    print(nrm, "+ ", end="")

    cont += 1
    divisor = divisor / 10

    total = total + nrm

print(" = ", total)