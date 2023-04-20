name = str(input('Qual é seu nome? '))
if name == 'Matheus':
    print(f'Que nome lindo {name}')
else:
    print(f'Seu nome é tão normal {name}')
print(f'Bom dia, {name}')


n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
n3 = float(input('Terceira nota do aluno: '))

m = (n1 + n2 + n3) / 3

print(
    f'A média de nota é {m:.1f}')
# if m >= 6.0:
#     print('Sua média foi boa!')
# else:
#     print('Sua média foi ruim!')
print('Parabéns' if m >= 6.0 else 'ESTUDE MAIS')
