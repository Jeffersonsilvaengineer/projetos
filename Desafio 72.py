contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
             'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input('Escolha um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {contagem[numero]} ')
    if 0 > numero > 20:
        input('Número inválido, digite um número entre 0 e 20')
    cont = input('Quer continuar? [S/N]').strip().upper()
    if cont in 'N':
        break


