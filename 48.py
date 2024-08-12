#usuario digitará o nome e o bairro de dez pessoas.
#O programa exibirá o nome e bairro das pessoas em ordem alfabética.

cadastro = []

for i in range(0,3):
    #intervalo entre 0 e 10 posicões
    aux = []
    nome = input("Digitará seu nome: ")
    bairro = input("Digite seu bairro: ")

    aux = [nome, bairro]
    #auxiliar ajuda a lista
    cadastro.append(aux)
    #ou cadastro.append(nome, bairro)

cadastro.sort()
print(cadastro)
# ordenar a lista de cadastro