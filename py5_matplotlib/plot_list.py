lista =[]
numero = int(input('ingrese el numero a evaluar :'))
lista.append(numero)


while numero != 1:
    c = numero % 2
    if c == 0:
        numero=numero/2
        lista.append(numero)
    else:
        numero= numero *3 +1
        lista.append(numero)

print(f"la lista es: { lista }")
