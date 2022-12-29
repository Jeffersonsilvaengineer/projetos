'''Faça um programa que leia o salário bruto de uma pessoa em um determinado mês.
Calcule e mostre o seu salário líquido no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato. A saída do programa deve escrever o seguinte texto:'''

'''(+) Salário Bruto: R$ valor
(-) IR (11%): R$ valor
(-) INSS (8%): R$ valor
(-) Sindicato ( 5%): R$ valor
(-) Total Desconto : R$ valor
(=) Salário Liquido: R$ valor'''

sal = float(input('Digite seu salário bruto: '))
renda = (sal * (11/100))
inss = (sal * (8/100))
sind = (sal * (5/100))
total = renda + inss + sind
liq = sal - total
print(f'(+) Salário Bruto: R$ {sal}')
print(f'(-) IR (11%): R$ {renda}')
print(f'(-) INSS (8%): R$ {inss}')
print(f'(-) Sindicato ( 5%): R$ {sind}')
print(f'(-) Total Desconto : R$ {total}')
print(f'(=) Salário Liquido: R$ {liq}')
