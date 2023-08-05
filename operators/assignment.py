
"""Operadores de Asignación

Los operadores de asignación en Python se utilizan para asignar valores a variables.
Son operadores que permiten guardar un valor en una variable específica.

Python también ofrece operadores de asignación compuesta, que combinan una operación
con la asignación en una sola expresión. Estos operadores son útiles para realizar
operaciones y actualizar el valor de una variable al mismo tiempo.

+= -> Suma y asignación
-= -> Resta y asignación
*= -> Multiplicación y asignación
/= -> División y asignación
**= -> Exponente y asignación
%= -> Modulo y asignación

"""

if __name__ == '__main__':

    number = 1

    number += 2
    print('Suma y asignación:', number)

    number -= 1
    print('Resta y asignación:', number)

    number *= 3
    print('Multiplicación y asignación:', number)

    number /= 3  # También existe para la division entera que es //=
    print('División y asignación:', number)

    number **= 2
    print('Exponente y asignación:', number)

    number %= 2
    print('Modulo y asignación:', number)




