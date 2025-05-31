def ifelseelif():
    # Variables numéricas
    numero1 = 20
    numero2 = 20

    # Variable booleana: ¿son iguales?
    iguales = (numero1 == numero2)

    # Lógica con if, elif y else
    if numero1 < numero2:
        resultado = "{} es menor que {}".format(numero1, numero2)
    elif iguales:
        resultado = "{} es igual a {}".format(numero1, numero2)
    else:
        resultado = "{} es mayor que {}".format(numero1, numero2)

    return dict(numero1=numero1, numero2=numero2, iguales=iguales, resultado=resultado)
