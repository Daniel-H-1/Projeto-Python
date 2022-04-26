print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Crie um programa que faça o computador jogar JOKENPÔ com você')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
import random
Pedra = 1
Papel = 2
Tesoura = 3
Lista = random.choices([Pedra, Papel, Tesoura])

print('''Vamos jogar Jokenpô!!!!
[1] Digite um para escolher, PEDRA.
[2] Digite dois para escolher, PAPEL.
[3] Digite três para escolher, TESOURA''')
escolha = int(input('Digite a sua escolha: '))

if escolha == 1 or 2 or 3:
    if Lista == [1] and escolha == 2:
        print('Pedra x Papel')
        print('PARÁBENS VOCÊ GANHOU!!!')
    elif Lista == [1] and escolha == 3:
        print('Pedra x Tesoura')
        print('VOCÊ PERDEU, LOGO O PROGRAMA GANHOU!!!')
    elif Lista == [2] and escolha == 3:
        print('Papel x Tesoura')
        print('VOCÊ GANHOU PARÁBENS!!!')
    elif Lista == [2] and escolha == 1:
        print('Papel x Pedra')
        print('VOCÊ PERDEU, LOGO O PROGRAMA GANHOU!!!')
    elif Lista == [3] and escolha == 1:
        print('Tesoura x Pedra')
        print(' VOCÊ GANHOU!!!')
    elif Lista == [3] and escolha == 2:
        print('Tesoura x Papel')
        print('VOCÊ PERDEU, LOGO O PROGRAMA GANHOU!!!')
    else:
        print('HOUVE UM EMPATE!!!')
else:
    print('Número Digitado Inválido')
print('>>>>>> FIM <<<<<')

