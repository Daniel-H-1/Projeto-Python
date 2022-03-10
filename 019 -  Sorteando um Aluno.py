import random
print('Um professor quer sortear um do seus quatro alunos para apagar o quadro. \n'
      'Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido')
print(' ')

Aluno1 = input('Digite o nome do Primeiro Aluno: ')
Aluno2 = input('Digite o nome do Segundo Aluno: ')
Aluno3 = input('Digite o nome do Terceiro Aluno: ')
Aluno4 = input('Digite o nome do Quarto Aluno: ')
sorteio = random.choices([Aluno1, Aluno2, Aluno3, Aluno4])

print(' ')
print('O nome do aluno sorteado é', sorteio)