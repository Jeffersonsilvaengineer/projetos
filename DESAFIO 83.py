list_1 = []
list_total = []
while True:
    list_1.append(str(input('Digite um nome: ')))
    list_1.append(int(input('Digite um peso: ')))
    list_total.append(list_1[:])
    list_1.clear()
    cont = input('Quer continuar [S/N]: ').upper()
    while cont not in 'SN':
        cont = input('RESPOSTA INVÁLIDA! Quer continuar [S/N]: ').upper()
    if cont == 'S':
        continue
    else:
        break
print(list_total)


