'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final mostre:
Quantas pessoas tem mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres tem mais de 20 anos.'''

pessoa = homen = mulher = 0
sexo = continuar = ''
while True:
    print('='*30)
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: [M/F]')).upper().strip()
    while not sexo in 'M/F':
        str(input('Qual o sexo: [M/F]')).upper().strip()
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    while not continuar in 'S/N':
        str(input('Quer continuar? [S/N]')).upper().strip()
    if sexo == 'F':
        sexo = 'FEMININO'
    elif sexo == 'M':
        sexo = 'MASCULINO'
    if idade > 18:
        pessoa += 1
    if sexo == 'MASCULINO':
        homen += 1
    if sexo == 'FEMININO' and idade > 20:
        mulher += 1
    if continuar == 'N':
       break
print('='*10, 'FIM', '='*10)
print(f'AO TODO TIVEMOS {pessoa} PESSOAS MAIORES DE 18 ANOS!')
print(f'AO TODO TIVEMOS {homen} HOMENS CADASTRADOS!')
print(f'AO TODO TIVEMOS {mulher} MULHERES ACIMA DE 20 ANOS!')
