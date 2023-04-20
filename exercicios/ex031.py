distância = float(input('Qual é a distância de sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}km.')
# if distância <= 200:
#     preço = distância * 0.50
# else:
#     preço = distância * 0.45

preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')
