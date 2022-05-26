print('''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa  cadastrada, o programa devefrá perguntar se o usuário
quer ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
resposta = "S"
cadastro_homens = mulheres = cadastros = maiores = idade = 0
while True:
    print('-' * 30)
    print('CADASTRO DE PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    while sexo not in 'MmFf':
        print('Digite valor válido!!!')
        sexo = str(input('Sexo [M/F]: '))
    cadastros += 1
    if sexo not in "Ff":
        cadastro_homens += 1
    if sexo not in "Mm" and idade < 20:
        mulheres += 1
    if idade > 18:
        maiores += 1
    resposta = str(input('Deseja cadastrar mais alguém [S/N]:  '))[0]
    while resposta not in "SsNn":
        print('Resposta inválida!')
        resposta = str(input('Deseja cadastar mais alguém [S/N]: '))[0]
    if resposta in "Nn":
        print('-' * 30)
        break

print(f"Foram cadastrados {cadastros} Pessoa(s) no Total.")
print(f'Foram cadastrados {maiores} Pessoa(s) com idade superior a 18.')
print(f'Foram cadastrados {cadastro_homens} homens.')
print(f"Foram cadastradas {mulheres} mulher(es) com idade menor de 20 Anos.")