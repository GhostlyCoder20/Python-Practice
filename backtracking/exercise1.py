""" Backtracking

Backtracking es una estrategia algorítmica que busca todas las posibles soluciones
dado un conjunto de variables inicial para encontrar el resultado definido por el problema

La idea principal detrás del backtracking es explorar todas las posibilidades en una estructura de árbol de decisiones,
retrocediendo (de ahí el término "backtracking") cuando se llega a una solución inválida o cuando ya no es posible
encontrar una solución. Es decir, cuando se encuentra una solución inválida, se deshace la elección
previa y se explora otra opción.

el backtracking se implementa típicamente mediante funciones recursivas.


"""
# nums es el arreglo de números
# target es el número que como resultado debe ser al combinar los diferentes números en el arreglo nums
def find_combinations(nums, target):

    # start es la posición inicial desde donde vamos a explorar las combinaciones en arreglo
    # path es el arreglo donde se guardaran las combinaciones en forma de arreglo
    def backtrack(start, target, path):
        if target == 0:  # si target es igual a 0
            result.append(path)  # se guarda lo que hay en path en result
            return
        for i in range(start, len(nums)): # recorre los elementos del arreglo nums desde posicion de start hasta la longitud del arreglo para evitar duplicados
            if nums[i] > target: # si el elemento del arreglo nums es mayor a target
                continue  # salta a la siguiente iteración
            # Si el elemento es menor llamamos recursivamente la función backtrack con los nuevos valores.
            # i se usa como el nuevo índice de inicio para evitar duplicados.
            # target - nums[i] es el nuevo valor de target.
            # path + [nums[i]] es la nueva combinación actual.
            backtrack(i, target - nums[i], path + [nums[i]])

    # primero si inicializa el arreglo result donde se guardaran todas las combinaciones
    result = []
    nums.sort() # ordena el arreglo nums
    backtrack(0, target, []) # pasa argumentos al método backtrack
    return result # al final después de que el método backtrack haya buscado y agregado todas las combinaciones a result lo retorna


if __name__ == '__main__':
    nums = [2, 3, 6, 7]
    target = 7
    print(find_combinations(nums, target))
