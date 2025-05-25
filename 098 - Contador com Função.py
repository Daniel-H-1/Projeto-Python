# Criando a Função do Título
def escreva_titulo(titulo):
    print(' ')
    print(f'{titulo:=^40}')
    print(' ')

def executando_programa(texto):
    print("-" * 40)
    print(f'{texto: ^40}')
    print('-' * 40)


# Função de Contador
def contadores_padrao():

    print('')
    print('Contagem Crescente')
    for num in range(1, 10, 1):
        print(num)

    print('')
    print('Contagem Descrescente')
    for num in range(10, 0, -2):
        print(num)

# Função de Contador Personalizada com os Dados do
def contador_personalizado(inicio, fim, passos):
    print('')
    print('Contagem Personalizada')
    if passos == 0:
        passos = 1
    for num in range(inicio, fim, passos):
        print(num)
    print('')

escreva_titulo(' INSTRUÇÕES DO DESAFIO ')

print('''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
                                                                                                                                                                            
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2                                                                                  
c) uma contagem personalizada''')

escreva_titulo(' RESOLUÇÃO DO DESAFIO ')
executando_programa(' CONTADORES DA FUNÇÃO ')

contadores_padrao()

inicio = int(input('Digite o valor Inicial: '))
fim = int(input('Digite o último valor possível: '))
passos = int(input('Digite se a contagem  aumenta de 1 e 1 ou mais, ou diminue de 1 em 1 ou mais : '))
(contador_personalizado(inicio, fim, passos))

escreva_titulo(' FIM DO DESAFIO ')