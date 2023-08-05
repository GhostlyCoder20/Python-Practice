"""Operadores Relacionales

Un operador relacional se emplea para comparar y establecer la relación entre ellos.
Devuelve un valor booleano (true o false) basado en la condición.

> ->	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha
< ->	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda
== ->	Devuelve True si ambos operandos son iguales
>= ->	Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
<= ->	Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda.
!= ->	Devuelve True si ambos operandos no son iguales

"""


if __name__ == '__main__':

    bigger = 2 > 3
    print("2 es mayor a 3 ?:", bigger)

    smaller = 4 < 2
    print("4 es menor a 2 ?:", smaller)

    equals = 3 == 3
    print("3 es igual a 3 ?:", equals)

    bigEqual = 5 >= 2
    print("5 es mayor o igual 2 ?:", bigEqual)

    smallEqual = 4 <= 4.1
    print("4 es menor o igual 4.1 ?:", smallEqual)

    distinct = 2 != 2
    print("2 es distinto de 2 ?:", distinct)


