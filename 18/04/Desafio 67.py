'''faça um programa que leia um numero inteiro e mostre sua tabuada!'''

while True:
    n = int(input('Qual tabuada voê deseja? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('PROGRAMA FINALIZADO!')
