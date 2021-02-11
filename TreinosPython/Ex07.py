'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
   * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
   * A mensagem "Reprovado", se a média for menor do que sete;
   * A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
import math
print('-=' * 20)
print('CALCULO DE MÉDIA'.center(40))
print('-=' * 20)
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi {media}')
if media >= 7:
    print('\033[32mAPROVADO\033[m')
if media < 7:
    print('\033[31mREPROVADO\033[m')
if media == 10:
    print('\033[33mAPROVADO COM DISTINÇÃO\033[m')
