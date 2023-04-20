dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'Total a pagar é R${pago:.2f}')
