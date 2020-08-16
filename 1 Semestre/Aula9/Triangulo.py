print("EXERCÍCIO 14\n")

n1 = int(input("Digite três números inteiros e descubra qual triângulo será formado: "))
n2 = int(input(""))
n3 = int(input(""))

if n1 > 0 and n2 > 0 and n3 > 0:
    if n1 == n2 and n1 == n3:
        print("Triângulo Equilátero")
    elif n1 == n2 or n1 == n3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é possível formar triângulo com medidas negativas")