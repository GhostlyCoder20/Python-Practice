"""
Los operadores a nivel de bit o bitwise operators son operadores que
actúan sobre números enteros pero usando su representación binaria.

bin(): sirve para convertir un número decimal a binario
y viceversa
"""

if __name__ == '__main__':


    """
    
    Operador &
    
    Es realizar operaciones lógicas AND a nivel de bits entre números enteros. 
    Cada bit en el resultado se calcula comparando los bits correspondientes en 
    los operandos y colocando un 1 en el resultado solo si ambos bits son 1. Esto 
    se utiliza para manipular y analizar representaciones binarias de números.
    
    """
    # Se realiza una operación por detrás que el resultado
    # (que al principio es binario pero luego convertido en número) es la suma de los dos números convertidos en binario
    a = 47
    b = 75
    c = a & b
    print(a, "es en binario: ", bin(a))
    print(b, "es en binario: ", bin(b))
    print(c, "es en binario: ", bin(c)) # 11 supuestamente

    print("\n")

    """
    
    Operador | 
    
    El operador "|" realiza la operación lógica OR (o inclusivo) entre los bits de los operandos. 
    Cada bit en el resultado se calcula comparando los bits correspondientes en los operandos y 
    colocando un 1 en el resultado si al menos uno de los bits es 1.
    
    
    """

    d = 60
    e = 90
    f = d | e
    print(d, "es en binario: ", bin(d))
    print(e, "es en binario: ", bin(e))
    print(f, "es en binario: ", bin(f))

    print("\n")

    """
    Operador ^
    
    La operación XOR es verdadera si los bits comparados son diferentes 
    y es falsa si los bits son iguales. En otras palabras, devuelve 1 si 
    los bits son diferentes y 0 si son iguales.
    
    """

    g = 5
    h = 10
    i = g ^ h
    print(g, "es en binario: ", bin(g))
    print(h, "es en binario: ", bin(h))
    print(i, "es en binario: ", bin(i))

    print("\n")


    """
    
    El Operador ~
    
    En Python, el operador NOT se utiliza como operador a nivel de bits para realizar la operación de inversión 
    (complemento) de bits en los valores enteros.
    """

    j = 9
    k = ~j
    print(j, "en binario es: ", bin(j))
    print(k, "en binario es: ", bin(k))

    print("\n")


    """
    Operadores >> o <<
    
    Los operadores Bit Shift son operadores que mueven los bits las posiciones que le indiquemos. 
    Disponemos de dos operadores dependiendo de si queremos mover los bits a la izquierda (<<), o a la derecha (>>).
    
    """

    l = 100
    m = l >> 2
    n = l << 2

    print(l, "en binario es: ", bin(l))
    print(m, "en binario es: ", bin(m))
    print(n, "en binario es: ", bin(n))




