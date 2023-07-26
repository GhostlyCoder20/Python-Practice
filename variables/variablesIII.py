
"""
Conversion de variables

Las conversiones permiten convertir un tipo de variable a otro, siempre que la conversión sea válida.
En total existes 6 conversores de variables, en esta parte solo mostraremos 4 conversores

"""
if __name__ == '__main__':

    iNumber = 9
    fNumber = 9.6
    sNumber = 10.45
    bNumber = 0

    # float() convierte la variable a tipo float
    print(float(iNumber))

    # int() convierte la variable a tipo int
    print(int(fNumber))

    # str() convierte la variable a tipo string
    print(str(sNumber))

    # bool() convierte la variable a tipo booleano
    # si el numero es cero retorna false, si es negativo o positivo retorna true
    print(bool(bNumber))








