menu = """
Bienvenido al conversor de monedas
1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos
Elige una Opción
"""
opcion = int(input(menu))      #ingresamos el valor en texto

if opcion == 1:
    pesos = input("Cuántos $$ pesos Colombianos tienes: ")
    pesos = float(pesos)
    valor_dolar = 3489
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $$"+ " " + dolares + " " + "Dólares")
elif opcion == 2:
    pesos = input("Cuántos $$ pesos Argentinos tienes: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $$"+ " " + dolares + " " + "Dólares")
elif opcion == 3:
    pesos = input("Cuántos $$ pesos Mexicanos tienes: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $$"+ " " + dolares + " " + "Dólares")
else:
    print("Ingresa una opción correcta por favor")