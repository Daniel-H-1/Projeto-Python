print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Desenvolva um programa que leia o cumprimento de três retas e verifique se as retas podem formar um triângulo')

print('-=' * 20)
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')

a = float(input('Digite o cumprimento da primeira reta: '))
b = float(input('Digite o cumprimento da segunda reta: '))
c = float(input('Digite o cumprimento da terceira reta: '))

# Jeito mais fácil de resolver!!!
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo com esses segmentos!!!')
else:
    print('Não é possível formar um triângulo, com esses cumprimentos!')

# Jeito mais difícil de resolver!!!!!
'''Busquei encontrar o cumprimento menor, o interdmediário (meio) e o maior,
depois somei o menor com o meio, pois se a soma do menor valor com o valor inntermediário,
for maior que o maior valor é possível formar um triângulo'''

# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Encontrando o valor intermediário
meio = a
if a == maior or a == menor:
    meio = b
    if b == maior or b == menor:
        meio = c

# Calculando o valor da soma do menor com o meio.
soma = menor + meio

# Verificando se é possível formar um triângulo.
if soma > maior:
    print('De acordo com os cumprimentos das retas, é possível formar um triângulo.')
else:
    print('De acordo com o cumprimento das retas, não é possível formar um triângulo.')
print('>>>>> FIM <<<<<')
