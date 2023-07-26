"""
Hay una forma de reasignar variables en python que es diferente de la usual
que se muestra de la siguiente forma

Es muy util para los arreglos, recuérdalo
"""


if __name__ == '__main__':

    num1 = 8
    num2 = 9

    print("Antes: ")
    print(num1)
    print(num2)

    # De esta forma lo que hay en num1 tendrá el valor de num2 y num2 tendrá el valor de num1
    num1, num2 = num2, num1

    print("Después: ")
    print(num1)
    print(num2)
