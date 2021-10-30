menu = """
Bienvenido al conversor de monedas.

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
  pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
  valor_dolar = 3766
  dolares = round(pesos / valor_dolar, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares + " dólares")
elif opcion == 2:
  pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
  valor_dolar = 65
  dolares = round(pesos / valor_dolar, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares + " dólares")
elif opcion == 3:
  pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
  valor_dolar = 24
  dolares = round(pesos / valor_dolar, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares + " dólares")
else:
  print("Opción inválida")




