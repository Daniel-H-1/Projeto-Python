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


# Função que descobre o Maior
def maior(* numeros):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

escreva_titulo(' INSTRUÇÕES DO DESAFIO ')

print('''Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e 
dizer qual deles é o maior.

''')

escreva_titulo(' RESOLUÇÃO DO DESAFIO ')
executando_programa(' FUNÇÃO QUE DESCOBRE O MAIOR ')

# Programa Principal
maior(99,3,5,9,4,6,8)
maior(22,33,55,1)
maior(2,4,3,9,5,8,99)
maior(5,2,2,3,1)

escreva_titulo(' FIM DO DESAFIO ')