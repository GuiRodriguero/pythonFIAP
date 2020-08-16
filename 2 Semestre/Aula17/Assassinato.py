#Lista de Perguntas
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ",
             "Devia para a vítima? ", "Já trabalhou com a vítima? "]

def perguntar(perguntas):
    respostas_positivas = 0

    #Passa por todas as perguntas
    for x in range(len(perguntas)):
        #Inicializa a variável de resposta atual
        resposta_atual = ""

        #Validação para aceitar somente S ou N
        while resposta_atual != "N" or resposta_atual !="S":
            print(perguntas[x] + "Responda com S/N") #Mostra a pergunta
            resposta_atual = input("").upper() #Recebe a resposta

            # Se a resposta for S ou N ele sai do laço While
            if resposta_atual == "S" or resposta_atual == "N":
                break

        #Soma as respostas positivas
        if resposta_atual == "S":
            respostas_positivas += 1

    return respostas_positivas

resultado = perguntar(perguntas) #Recebe como retorno o número de respostas positivas

print("\n:::RESULTADO:::")

if resultado == 2:
    print("SUSPEITO")
elif resultado == 3 or 4:
    print("CÚMPLICE")
elif resultado == 5:
    print("ASSASSINO")
else:
    print("INOCENTE")


