#Ex 04 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n = float(input('Diga um valor: '))
if n < 0:
    print(f'O número {n} é negativo.')
if n > 0:
    print(f'O número {n} é positivo.')