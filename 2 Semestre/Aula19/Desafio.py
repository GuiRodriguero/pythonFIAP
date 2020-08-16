valores_produtos = (10.75, 9.78, 100.60)
print("------------------------------ \n        LISTA DE PREÇOS      \n------------------------------")
for x in range(len(valores_produtos)):
    strNumero = str('{:.2f}'.format(valores_produtos[x])) #Transforma em string para alinha-lo já formatado com 2 casas após a vírgula
    print("PRODUTO", (x+1) , ".......... " + "R$ " + strNumero.rjust(6))
strSoma = str(sum(valores_produtos))
print("------------------------------ \nTOTAL............... " + "R$ " + strSoma.rjust(6))