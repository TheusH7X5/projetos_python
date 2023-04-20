a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))
lower_value = a
if b < a and b < c:
    lower_value = b
if c < a and c < b:
    lower_value = c

upper_value = a
if b > a and b > c:
    upper_value = b
if c > a and c > b:
    upper_value = c

print(f'O menor valor digitado foi {lower_value}')
print(f'O maior valor digitado foi {upper_value}')
