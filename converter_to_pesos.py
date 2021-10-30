dolares = input("Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_dolar = 3766
pesos = dolares * valor_dolar
pesos = round(pesos, 0)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")