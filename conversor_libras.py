def run():
    def conversor(tipo_pesos, valor_libra):
        pesos = input("Cuantos pesos tienes: ")
        pesos = float(pesos)
        libras = pesos / valor_libra
        libras = round(libras, 2)
        libras = str(libras)
        print("Tienes" + " " + libras + " " +  "libras Esterlinas")


    menu = """

    Bienvenido a nuestro conversor,
    Que moneda tienes:

    1) Pesos Colombianos
    2) Pesos Mexicanos
    3) Pesos Argentinos
    4) Pesos Chilenos

    Selecciona la Opción adecuada: """

    opcion = int(input(menu))

    if opcion == 1:
        conversor("Colombianos", 4925)
    elif opcion == 2:
        conversor("Mexicanos", 27)
    elif opcion == 3:
        conversor("Argentinos", 118)
    elif opcion == 4:
        conversor("Chilenos", 1009)
    else:
        print("Ingrese la opción correcta")
        

if __name__ == "__main__":
    run()