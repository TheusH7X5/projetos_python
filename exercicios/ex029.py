speed = float(input('Qual é a velocidade atual do carro? '))
if speed > 80:
    print('MULTADO!, Você excedeu o limite permitido que é de 80km/h')
    multa = (speed-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
