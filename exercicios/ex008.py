medida = float(input('Digite a medida: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(
    f'A media de {medida}m corresponde a {km}km, {hm}hm, {dam}dam, {dm:.1f}dm, {cm:.1f}cm, {mm:.1f}mm e ')
