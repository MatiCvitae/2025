def ifelseelif():
    numero1 = 20
    numero2 = 20
    iguales = (numero1 == numero2)
    if numero1 < numero2:
        resultado = "{} es menor que {}".format(numero1, numero2)
    elif iguales:
        resultado = "{} es igual a {}".format(numero1, numero2)
    else:
        resultado = "{} es mayor que {}".format(numero1, numero2)

    return dict(numero1=numero1, numero2=numero2, iguales=iguales, resultado=resultado)
