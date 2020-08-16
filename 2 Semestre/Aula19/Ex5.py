palavras = ("Osasco", "Santos", "Itaquaquecetuba", "Acre", "Rio de Janeiro", "Diadema")

def maiorPalavra(palavras):
    maior = "" #Armazena a maior palavra encontrada
    maior_len = 0 #Armazena a quantidade de letras da maior palavra

    for x in palavras:
        if len(x) > maior_len: #Se o tamanho da palavra atual for maior do que a maior palavra já vista até então:
            maior_len = len(x) #Armazena a quantidade de letras caso a plavra atual seja a maior
            maior = x #Armazena a palavra na variável "maior"

    return "A maior palavra é: " + maior

maior_palavra = maiorPalavra(palavras)
print(maior_palavra)