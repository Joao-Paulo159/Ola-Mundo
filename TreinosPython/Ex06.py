# 06 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogal = ['A','E','I','O','U']
consoante = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'I', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'X', 'Y', 'Z']
letra = str(input('Digite um Letra: ')).strip().upper()
if letra in vogal:
    print('A letra que você digitou é uma Vogal.')
if letra in consoante:
    print('A letra que você digitou é uma Consoante.')

    