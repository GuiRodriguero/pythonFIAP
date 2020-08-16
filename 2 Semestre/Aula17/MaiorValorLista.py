def maior(lista):
    #Inicializando os valores de retorno
    maior = 0
    posicao = 0


    #Fazendo com funções prontas
    #maior = max(lista)
    #posica = lista.index(maior)


    #Verifiçação do maior número passando pela lista completa
    for x in range(len(lista)):
        if lista[x] > maior:
            maior = lista[x]
            posicao = x
    return maior, posicao

#A respota para o exercício
maiorNumero = 0
posicaoMaior = 0

#Lista dos números a serem analisados
numeros = []

#Quantos números terá sua lista?
quantidadeNumero = int(input("Quantos números você deseja cadastrar? "))

#Laço para cadastrar os números
for num in range (quantidadeNumero):
    #Pedindo o número e cadastrando na lista
    numeros.append(int(input("Digite o número : ")))

#Atribuindo as repsotas e executando o método
maiorNumero, posicaoMaior = maior(numeros)

#Exibindo o resultado
print("O maior número presente na lista é o ", maiorNumero, " e está na posição: ", (posicaoMaior+1))


