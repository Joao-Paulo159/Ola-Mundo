# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
for c in range(0,3):
    nomep = str(input(f'Produto 0{c+1}: '))
    preço = float(input(f'Preço R$'))
    menor = preço
if (preço < menor):
    menor = preço
if (preço < menor):
    menor = preço
print(f'Você deve comprar o  produto que custa R${menor:.2f} pois é o mais barato'.replace('.',','))
