print(":::CALCULE SUA VELOCIDADE MÉDIA:::\n")

metros = float(input("Digite quantos metros você percorreu: "))
segundos = float(input("Digite em quantos minutos você percorreu estes metros: "))

vm = metros/segundos

print(".:VELOCIDADE MÉDIA:.\n")
print(vm, " m/s")
print((vm*3.6), "km/h")