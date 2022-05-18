print('>>>>> INSTRUÇÕES DO PROGRAMA <<<<<')
print('''Melhore o  Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.''')

print(' ')
print('>>>>> RESOLUÇÃO DO PROGRAMA <<<<<')
Termo = int(input('Digite o primeiro termo da PA: '))
Razão = int(input('Digite a Razão da PA: '))
count = 1
termosextra = 0
while count < 11:
    print('{}'.format(Termo), end=" -> ")
    Termo += Razão
    count += 1
    if count == 11:
        print('PAUSA')
        print('Você deseja mostra mais algum termo?? Se deseja digite a seguir')
        termosextra = int(input('Termos a mais: '))
        count -= termosextra
print('>>>>> FIM <<<<<')
