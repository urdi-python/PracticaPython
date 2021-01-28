#RESUMEN
def run():
    def conversor(tipo_pesos, valor_euro):
        pesos = input("Cuántos Pesos tienes: ")
        pesos = float(pesos)
        euros = pesos / valor_euro
        euros = round(euros, 1)
        euros = str(euros)
        print("tienes" + " " + euros + " " + "Euros")
    

    menu = """
    Bienvenido al conversos de pesos a Euros:
    Por favor selecciona los pesos de su preferencia

    1- Peso Colombiano
    2- Pesos Argentino
    3- Pesos Mexicano
    4- Pesos Chilenos

    Gracias por preferirnos 

    """
    opcion = int(input(menu))

    if opcion == 1:
        conversor("Colombianos", 4273)
    elif opcion == 2:
        conversor("Argentinos", 103)
    elif opcion == 3:
        conversor("Mexicanos", 25)
    elif opcion == 4:
        conversor("Chilenos", 739)
    else:
        print("ingresa correctamente el numero de preferencia por favor")



if __name__ == "main":
    run()

