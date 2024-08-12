matrix = [[1,2,15], [3,4], [5,6]]

# matrix [linha][coluna]
# print(matrix[0][2])
# [1 -- 2]
# [3 -- 4]

doces = [["Pudim", 3], ["Brigadeiro", 1], ["Pave", 5], ["Quindim", 2], ["Torta de Limão",4]]
#colchete amarelo = lista e colchete roxo = linhas, que sempre começa no zero

print(doces[1][0], doces[1][1])
#primeiro quero saber posição e o segundo quero saber nota

doces.sort()
print(doces)
#para ordenar lista

doces.sort(key=lambda x:x[1])
print(doces)
#para ordenar a lista pela nota. x é o nome da matriz e que tenha que classificar na linha 1. se fosse na linha 10 teria que colocar x:x[9]
