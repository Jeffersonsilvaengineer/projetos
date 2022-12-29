'''Faça um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final mostre: Qual o total da compra, quantos produtos custam
 mais de R$ 1000 reais, Qual o nome do produto mais barato.'''
total = mil = menor = cont = 0
barato = ' '
print('='*23)
print('{:=^23}'.format(' LOJAS JEFFERSON '))
while True:
    print('='*23)
    produto = str(input('Nome do produto: '))
    valor = float(input('Qual o valor:R$ '))
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    total += valor
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    if valor > 1000:
        mil += 1
    if continuar == 'N':
        break
print('='*9,'FIM','='*9)
print(f'O total da compra foi {total:.2f} reais!')
print(f'{mil} produtos custam mais de mil reais!')
print(f'O produto mais barato foi {barato}!')