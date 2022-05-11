print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Desenvolva um programa que leia o sexo biológico de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
sexo = str(input('Digite seu sexo biológico [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
        sexo = str(input('Sexo inexistente!!! Digite um valor valido: ')).strip().upper()[0]

print('Obrigado pela cooperação!!! Dado Registrado com Sucesso!')
print('>>>>> FIM <<<<<')
