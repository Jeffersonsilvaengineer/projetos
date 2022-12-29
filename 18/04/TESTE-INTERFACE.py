'''Crie um programa onde o usúario possa digitar 7 valores númericos e cadastreos em um única lista
que mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente!'''

list_total = [[], []]
for c in range(7):
    valores = int(input(f'Digite o {c+1} número: '))
    if valores % 2 == 0:
        list_total[0].append(valores)
    else:
        list_total[1].append(valores)
    list_total[0].sort()
    list_total[1].sort()
print('=-='*20)
print(f'Os valores pares foram {list_total[0]}')
print(f'Os valores impares foram {list_total[1]}')

