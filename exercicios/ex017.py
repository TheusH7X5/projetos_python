from math import hypot

co = float(input('Comporimento de cateto oposto: '))
ca = float(input('Comporimento de cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 0.5
hi_import = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
print(f'A hipotenusa vai medir {hi_import:.2f} importando biblioteca')
