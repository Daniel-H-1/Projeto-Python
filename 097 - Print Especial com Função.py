# Criando a Função do Título
def escreva_titulo(titulo):
    print(' ')
    print(f'{titulo:=^40}')
    print(' ')

# Criando a Função de Print Especial
def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

escreva_titulo(' INSTRUÇÕES DO DESAFIO ')

print('''Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável. ''')

escreva_titulo(' RESOLUÇÃO DO DESAFIO ')

print("-" * 40)
print(f'{" FUNÇÃO ESCREVER ": ^40}')
print('-' * 40)

# Chamando a Função para Escrever
print('Escrevendo com a Função a Área')
print('-' * 30)

escreva('FUNÇÃO ATIVA (ONLINE)')
escreva('OBRIGADOS AMIGOS')
escreva('ATÉ A PRÓXIMA')


escreva_titulo(' FIM DO DESAFIO ')
