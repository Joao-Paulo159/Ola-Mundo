#maior >
# menor < 
#08 - Faça um Programa que leia três números e mostre o maior e o menor deles .
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número: '))
maior = n1
menor = n1
if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3
if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3
print(f'O maior entre eles é {maior} e o menor é {menor}')
