numeros_inteiros = (1, 17, 10, 20, 27, 28, 99, 100, 64, 38, 11, 19, 7, 9, 300)

def maior(numeros):

    maior_retorno = 0 #Armazena o maior número

    for x in numeros:
        if maior_retorno < x:
            maior_retorno = x

    return maior_retorno

maior_numero = maior(numeros_inteiros)

print("O maior número é: ", maior_numero)