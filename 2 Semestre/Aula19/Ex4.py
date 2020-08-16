numeros_inteiros = (1, 17, 10, 20, 27, 28, 99, 100, 64, 38, 11, 19, 7, 9, 300)

def media(numeros):

    media_soma = 0 #Armazena a média

    for x in numeros:
        media_soma += x
    return media_soma/len(numeros) #Soma / Quantidade de numeros

media_numero = media(numeros_inteiros)

print("A média desta tupla é: ", media_numero)