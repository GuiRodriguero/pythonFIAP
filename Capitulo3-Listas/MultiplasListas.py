equipamento = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamento)):
    print("\nEquipamento: ", [indice+1])
    print("Nome: ", equipamento[indice])
    print("Valor: ", valores[indice])
    print("Serial: ", seriais[indice])
    print("Departamento: ", departamentos[indice])

busca = input("\n Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
        print("Valor: ", valores[indice])
        print("Serial: ", seriais[indice])


depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamento)): # Passa por toda a lista
    if depreciacao == equipamento[indice]: # Compara os nomes
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

serial = int(input("\n Digite o serial do equipamento que será excluído"))
for indice in range (0,len(departamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamento[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamento)):
    print("\nEquipamento: ", [indice+1])
    print("Nome: ", equipamento[indice])
    print("Valor: ", valores[indice])
    print("Serial: ", seriais[indice])
    print("Departamento: ", departamentos[indice])