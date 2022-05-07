print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Crie um programa que leia uma frase qualquer e diga se 
ela é um palíndrimo, desconsiderando os espaços.

Exemplo de Frase:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
inverso = juntar[::-1]
print('O inverso de {} é {}'.format(juntar, inverso))
if juntar == inverso:
    print('A palavra é um Palíndromo, ou seja ela é a mesma de tras para frente!!!')
else:
    print('A palavra não é um Palíndromo!!!')
print('>>>>> FIM <<<<<')