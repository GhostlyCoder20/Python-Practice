"""
Concatenación de variables

Para concatenar en python existen 4 formas de concatenar

* concatenar con el símbolo +
* concatenar con el método .format()
* concatenar con fstring
* concatenar con comas(solo funciona en el método print)

"""
if __name__ == '__main__':

    firstName = "Francisco"
    lastName = "Molina"
    age = 20

    # concatenar con el símbolo mas
    full_name = firstName + " " + lastName
    print(full_name)

    # concatenar con el método .format()
    greeting1 = "Hola, soy {} y tengo {} años".format(firstName, age)
    print(greeting1)

    # concatenar con fstring
    greeting2 = f"Hola mi nombre es {firstName} {lastName}"
    print(greeting2)

    # concatenar con comas(solo funciona en el método print)
    print("Hola, soy", firstName, lastName, "y tengo", age, "años")





