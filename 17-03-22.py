'''Faça um programa que jogue um joguinho com o computador. O joga será interrompido quando
o jogador perder. Mostrando o total de vitórias consecutivas ou que ele conquistou no final do jogo.'''

import random
soma = 0
while True:
    computador = random.randint(0, 100)
    print('=-'*15)
    print('VAMOS JOGAR PAR OU IMPAR!')
    print('=-'*15)
    v = int(input('Digite um valor: '))
    pi = str(input('PAR OU IMPAR ? [P/I]')).upper().strip()
    result = computador + v
    final = result % 2
    if final == 0 and pi == 'P' or final == 1 and pi == 'I':
        print('VOCÊ GANHOU!')
        soma += 1
    else:
        print('VOCÊ PERDEU!')
        break
if final == 0:
    final = 'PAR'
elif final == 1:
    final = 'IMPAR'
if pi == 'P':
    pi = 'PAR'
elif pi == 'I':
     pi = 'IMPAR'
print(f'Você jogou {v} e o computador {computador}, a soma desses valores é {result}, '
      f'e este valor é {final} e você escolheu {pi}.')
print(f'FIM!, O JOGO TERMINOU COM {soma} VITÓRIAS CONSECUTIVAS!')
