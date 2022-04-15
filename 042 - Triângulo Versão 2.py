print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar \n'
      'que tipo de triângulo será formado:\n'
      '- Equilátero: todos os lados iguais.\n'
      '- Isósceles: dois lados iguais.\n'
      '- Escaleno: todos os lados diferentes.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
a = float(input('Digite o cumprimento da primeira reta: '))
b = float(input('Digite o cumprimento da segunda reta: '))
c = float(input('Digite o cumprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo com esses segmentos!!!')
    if a == b and a == c:
          print('O triângulo será Equilátero.')
    elif a == b or b == c or a == c:
          print('O triângulo será Isóscceles.')
    elif a != b and a != c:
          print('O triângulo será Escaleno.')
else:
      print('Não é possível formar um triângulo!!!')
print('>>>>> FIM <<<<<')
