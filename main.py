'''faça um programa que leia a ano de nascimento de uma pessoa e mostre se ela ja tem a idade de 18 anos para
tirar habilitação para dirigir, o programa deve mostrar quantas tentativas foram necessárias para conseguir!'''
import random
pessoa = ''
tentativa = 0
computador = random.randint(0, 100)
while pessoa != computador:
    pessoa = int(input('qual o número pensado pelo computador?'))
    tentativa += 1
    if computador < pessoa:
        print('MAIS...')
    if computador > pessoa:
        print('MENOS...')
print('Parabéns! você acertou o número pensado pelo computador! depois de {} tentativas'.format(tentativa))
