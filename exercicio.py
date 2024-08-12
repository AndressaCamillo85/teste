#Exercício
'''O usuario digitara dez numeros. O programa devera calcular quantos deles são maiores que dez'''
controle = 0
for i in range(0, 2):
    entrada = input('Digite um numero: ')
    numero = int(entrada)

    if numero > 10:
       controle+=1

print('Existem' , controle, 'numero(s) maiores que 10')