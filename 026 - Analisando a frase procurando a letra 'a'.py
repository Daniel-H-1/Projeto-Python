print('             >>>>>> INSTRUÇÕES DO PROGRAMA <<<<<<   ')
print('''CRIE UM PROGRAMA QUE LEIA UMA FRASE ESCRITA E MOSTRE:

1 - Quantas vezes a letra "A".
2 - Em que posição ela aparece a primeira vez.
3 - Em que posição ela aparece a última vez.
''')

print('            >>>>>> RESOLUÇÃO DO PROGRAMA <<<<<<   ')

Frase = str(input('Digite uma frase: ')).strip()

print('A frase possui {} Letra(s) "A" '.format(Frase.lower().count('a')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(Frase.lower().find('a')+1))
print('A letra "A" aparece pela última vez na posição: {}'.format(Frase.lower().rfind('a')+1))
