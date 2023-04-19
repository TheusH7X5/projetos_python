while True:
    valor = input().strip().lower()

    if valor[0] == "-":
        break

    if valor[:2] == "0x":
        valor_decimal = int(valor, 16)
        print(valor_decimal)
    else:
        valor_decimal = int(valor)
        valor_hexadecimal = hex(valor_decimal)
        print("0x" + valor_hexadecimal[2:].upper())
