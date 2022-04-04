print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('Escreva um programa que  pergunte o valor do salário de um funcionário e calcule o valor do seu aumento')
print('Para salário superiores a R$1.250,00, calcule um aumento de 10%.')
print('Para salários inferiores ou iguais, o aumento é de 15%.')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Salario = float(input('Digite o valor do seu salario: '))
if Salario > 1250.00:
    print('Você terá um aumento de 10%, e isso significa que seu salario agora é: R${:.2f}'.format(Salario + (Salario * 10/100) ))
else:
    print('O seu Salario com aumento de 15% é R${:.2f}'.format(Salario + Salario * 0.15))
print('>>>>> FIM <<<<<')
