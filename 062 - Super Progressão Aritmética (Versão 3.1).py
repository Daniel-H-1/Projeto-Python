print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end="")
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantas termos você quer mostrar mais? '))
print('Progressão Finalizada com {} termos mostrados'.format(total))
print('>>>>> FIM <<<<<')

