print('-=' * 20)
print(f'{"CALCULO DE TEMPO DE DOWNLOAD":^40}')
print('-=' * 20)
tamanhoprogam = float(input('Qual é o tamanho do programa em MB:'))
velocidade =  int(input('Quantos megas de internet? '))
calculo = tamanhoprogam / velocidade
print(f'{calculo:.1f} Min')