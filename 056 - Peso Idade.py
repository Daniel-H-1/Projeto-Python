print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Desenvolva um programa que leia o Nome, Idade e Sexo de 4 pessoas.
No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres possuem idade inferior a 20.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
mulheres = 0
soma = 0
maior = 0
count = 0
for pessoa in range(1, 5):
    print('-- {} PESSOA --'.format(pessoa))
    Nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    count += 1
    if pessoa == 1:
        maior = idade
        velho = Nome
    if idade > maior and Sexo == 'M':
    # if Sexo in "Mm" and idade > maior:
        maior = idade
        velho = Nome
    if Sexo == 'F' and idade < 20:
    # if Sexo in "Ff":
        mulheres += 1
média = soma / count
print('A média de idade do grupo é de {} Anos'.format(média))
print('O homem mais velho do grupo é {} e tem {} Anos'.format(velho, maior))
print('Existem {} mulher(es) que tem menos de 20 Anos'.format(mulheres))
