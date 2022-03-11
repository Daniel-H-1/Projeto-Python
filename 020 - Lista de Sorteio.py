import random
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos.\n'
      'Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
print(' ')

Aluno1 = input('Digite o nome do Primeiro Aluno: ')
Aluno2 = input('Digite o nome do Segundo Aluno: ')
Aluno3 = input('Digite o nome do Terceiro Aluno: ')
Aluno4 = input('Digite o nome do Quarto Aluno: ')
Lista = [Aluno1, Aluno2, Aluno3, Aluno4]
random.shuffle(Lista)

print('Os sorteados foram\n', Lista)



