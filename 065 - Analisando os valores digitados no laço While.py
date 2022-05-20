print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução , mostre a média entre todos os valores e qual foi o maior
e o menor valores  lidos. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar os valores.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Resposta = 'Não'
soma = 0
count = 0
while Resposta != 'N':
    n = int(input('Digite um valor: '))
    soma += n
    count += 1
    Resposta = str(input('Deseja digitar mais algum número [S/N]: ')).upper()
    if count == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
média = soma / count
print('A média dos números digitados é {:.2f}'.format(média))
print('O maior valor digitado é {} /// O menor valor digitado é {}'.format(maior, menor))
