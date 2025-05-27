from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p ==0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Digite o valor Inicial: '))
fim = int(input('Digite o último valor possível: '))
passos = int(input('Digite se a contagem  aumenta de 1 e 1 ou mais, ou diminue de 1 em 1 ou mais : '))