from math import sin, radians, cos, tan
ângulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o seno de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o tangente de {tangente:.2f}')