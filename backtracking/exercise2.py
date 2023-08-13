"""
Ejercicio de sudoku con backtracking
"""

def print_sudoku(sudoku):
    for i in range(9):

        if i == 3 or i == 6:
            print("|-------+-------+-------|")
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            if sudoku[i][j]:
                print(str(sudoku[i][j]) + " ", end="")
            else:
                print(". ", end="")
        print("|")

def validate(sudoku, n, i, j):
    row = sudoku[i]
    column = [row[j] for row in sudoku]
    block = [sudoku[a][b]
             for a in range(9)
             for b in range(9)
             if i // 3 == a // 3
             and j // 3 == b // 3]
    return n not in row and n not in column and n not in block


def solve_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    if validate(sudoku, n, i, j):
                        sudoku[i][j] = n
                        if solve_sudoku(sudoku):
                            return True
                        else:
                            sudoku[i][j] = 0
                return False
    return True



if __name__ == '__main__':

    SUDOKU = [
        [0, 0, 0, 0, 0, 0, 0, 5, 7],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [1, 0, 0, 7, 0, 0, 0, 9, 6],
        [6, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 4, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 1, 0, 0, 0, 9],
        [0, 9, 0, 2, 0, 7, 8, 0, 0],
        [0, 0, 5, 0, 8, 4, 0, 7, 0]
    ]

    solve_sudoku(SUDOKU)
    print_sudoku(SUDOKU)

