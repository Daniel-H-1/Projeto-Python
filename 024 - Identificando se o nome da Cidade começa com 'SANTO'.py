print('             >>>>>> INSTRUÇÕES DO PROGRAMA <<<<<<   ')
print('''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"''')

print(' ')
print('            >>>>>> RESOLUÇÃO DO PROGRAMA <<<<<<   ')

Cidade = str(input("Digite o nome da sua Cidade: ")).strip
Primeiro_Nome = Cidade.split()
print('O primeiro nome da cidade é Santo?')
print(Primeiro_Nome[0].lower() == 'santo')

