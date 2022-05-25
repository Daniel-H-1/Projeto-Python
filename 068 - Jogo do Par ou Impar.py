print('''Faça um programa que jogue Par ou Ímpar com o computador.
jogo só será interrompido  quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
from random import randint
vitória = 0
while True:
    print('JOGO DO PAR OU ÍMPAR')
    print('=' * 30)
    n_escolhido = int(input('Digite um valor: '))
    sorteio = randint(0, 10)
    total = n_escolhido + sorteio
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip()[0]
    print(f'Você escolheu o número {n_escolhido} e o computador {sorteio}. Total de {total}.')
    if total % 2 == 0:
        print(f'{total} é PAR!')
    else:
        print(f'{total} é ÍMPAR!')
    if tipo == 'P' or 'p':
        if total % 2 == 0:
            print('VOCÊ VENCEU!!!')
            vitória += 1
        else:
            print('VOCÊ PERDEU!')
    elif tipo == 'I' or 'i':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitória += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print('>>>>> FIM <<<<<')
