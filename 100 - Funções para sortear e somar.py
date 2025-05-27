from random import randint
from time import sleep

# Criando a Função do Título
def escreva_titulo(titulo):
    print(' ')
    print(f'{titulo:=^40}')
    print(' ')


#Função título do programa
def executando_programa(texto):
    print("-" * 40)
    print(f'{texto: ^40}')
    print('-' * 40)


# Função SORTEAR
def sorteia(lista):
    print('Sorteando 5 valores da Lista: ', end='')
    for contador in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

# Função Soma PAR
def somaPar(lista):
    soma = 0
    for valor in lista:
            if valor % 2 == 0:
                soma += valor
                print(f'Somando os valores Pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)


