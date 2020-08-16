nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

def dupla(nomes):
    #nome_dupla = []

    for x in nomes:
        for y in nomes:
            if x != y: # Faz Com que Ana e Ana não aconteçam
                if nomes.index(y) > nomes.index(x): # Faz com que Ana e Bia / Bia e Ana não aconteçam

                    #nome_dupla.append(x + " e " + y)
                    #print(nome_dupla)
                    
                    print(x + " e " + y)

nome_teste = dupla(nomes)
