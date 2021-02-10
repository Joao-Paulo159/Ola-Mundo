#05 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Qual é o seu sexo? [M/F]')).upper().strip()
if sexo == 'F':
    print('Sexo Feminino.')
if sexo == 'M':
    print('Sexo Masculino.')
if sexo not in 'MF':
    print('Sexo invalido!')

