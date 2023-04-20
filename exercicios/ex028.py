from random import randint
from time import sleep
computer = randint(0, 5)  # make the computer "Think"
player = int(input("What number i thought? "))
print('Processando...')
sleep(3)
if player == computer:
    print(
        f'Parabéns você conseguiu me vencer! eu pensei no {computer} e você no {player}')
else:
    print(f'GANHEI! Eu pensei no número {player} e não no {computer}')
