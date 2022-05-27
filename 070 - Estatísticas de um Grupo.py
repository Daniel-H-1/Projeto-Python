print('''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato. ''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
resposta = 'S'
count = maior_1000 = gasto_total = 0
while True:
    print('=' * 40)
    print('{:^40}'.format('ÁNALISE DE GASTOS'))
    print('=' * 40)
    nome_produto = str(input('Digite o nome do produto: '))
    custo_produto = float(input('Preço (R$125.99): '))
    count += 1
    gasto_total += custo_produto
    if count == 1:
        mais_barato = nome_produto
        menor_valor = custo_produto
    if custo_produto < menor_valor:
        mais_barato = nome_produto
        menor_valor = custo_produto
    if custo_produto > 1000.00:
        maior_1000 += 1
    resposta = str(input('Deseja adicionar outro produto [S/N]: '))[0]
    while resposta not in "SsNn":
        print('VALOR INVÁLIDO')
        resposta = str(input('Deseja adicionar outro produto [S/N]: '))[0]
    if resposta == 'N' or 'n':
        break
print('=' * 40)
print('{:^40}' .format('ESTATÍSTICAS DOS GASTOS'))
print('-' * 40)
print(f"O Total gasto é {gasto_total:.2f} Reais.")
print(f"{maior_1000} Produto(s) tem o valor acima de R$1000.")
print(f'O nome do produto mais barato é {mais_barato}, e custa R${menor_valor}.')
print('>>>>> FIM <<<<<')
