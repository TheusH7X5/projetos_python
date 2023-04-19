preço = float(input('Qual é o preço do produto? R$'))
preço_desconto = preço - (preço * 5 / 100)

print(f'O produto que custava R${preço}, na promoção de 5% de desconto vai custar R${preço_desconto}')
