#Ex 03 - Faça um Programa que peça dois números e imprima o maior deles.
while True:
    n1 = float(input('Primeiro Número: '))
    n2 = float(input('Segundo Número: '))
    maior = 0
    if n1 > n2:
        maior = n1
        print(f'O maior número entre {n1} e {n2} é {maior}')
    if n2 > n1:
        maior = n2
        print(f'O maior entre {n1} e {n2} é {maior}')
    else:
        print('Os dois valores são iguais.')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

