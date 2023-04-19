idade_dias = int(input())

anos = idade_dias // 365
idade_dias = idade_dias % 365

meses = idade_dias // 30
idade_dias = idade_dias % 30

dias = idade_dias

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
