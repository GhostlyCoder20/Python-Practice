"""Operadores aritméticos

Se utilizan para realizar operaciones matemáticas en variables o valores numéricos.

  + -> para sumar
  - -> para restar
  * -> para multiplicar
  / -> para dividir
  // -> para division entera
  % -> para el residuo de una division
  ** -> para elevar a una potencia

"""

if __name__ == '__main__':

    num1 = 10
    num2 = 2

    # Sumar
    sum = num1 + num2
    rest = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    idiv = num1 // num2
    resd = num1 % num2
    pow = num2**num1

    print("Suma:", sum)
    print("Resta:", rest)
    print("Multiplicación:", mult)
    print("Division: ", div)
    print("Division entera: ", idiv)
    print("Residuo:", resd)
    print("Elevado a la potencia de", num1, ":", pow)






