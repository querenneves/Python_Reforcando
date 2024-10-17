x = int(input('Digite um inteiro: '))
if x == 0:
    paridade = 'neutro'
else:
    paridade = 'par' if x % 2 == 0 else 'ímpar'
print(f'O valor de {x} é {paridade}')
