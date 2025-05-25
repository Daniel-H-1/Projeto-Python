print(f'{" INSTRUÇÕES DO DESAFIO ":=^40}')
print('''Faça um programa que tenha uma Função chamada "área()", que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a Área do Terreno.''')

print(' ')
print(f'{" RESOLUÇÃO DO DESAFIO ":=^40}')

print("-" * 40)
print(f'{" FUNÇÃO ÁREA ": ^40}')
print('-' * 40)

# Criando a Função
def área(largura, comprimento):
    calcular_area = largura * comprimento
    print(f'Á área de um terreno {largura} x {comprimento} é de {calcular_area}m².')

# Chamando a Função para calcular a Área
print('Descobrindo a Área')
print('-' * 30)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)


print(f'{" FIM DO DESAFIO ":=^40}')



