# Esempio di sudoku

matrix = [[5, 4, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 0, 0, 0, 9, 1, 6, 0],
          [0, 0, 2, 6, 0, 0, 0, 8, 0],
          [0, 0, 8, 4, 0, 2, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 0, 7, 0, 5, 3, 0, 0],
          [0, 9, 0, 0, 0, 1, 7, 0, 0],
          [0, 3, 7, 2, 0, 0, 0, 0, 4],
          [0, 0, 0, 0, 0, 0, 0, 9, 8]]


def stampa(matrix):
    for x in range(9):
        s = " "
        for y in range(9):
            if matrix[x][y] != 0:
                if y == 2 or y == 5:
                    s += str(matrix[x][y]) + " | "
                else:
                    s += str(matrix[x][y]) + " "
            else:
                if y == 2 or y == 5:
                    s += "- | "
                else:
                    s += "- "
        print(s)
        if x == 2 or x == 5:
            print(" ------+-------+------ ")


def check_riga(mat, y, n):
    for i in range(9):
        if mat[y][i] == n:
            return False
    return True


def check_colonna(mat, x, n):
    for i in range(9):
        if mat[i][x] == n:
            return False
    return True


def check_quadrato(mat, x, y, n):
    col = (y // 3)
    riga = (x // 3)
    for i in range(3):
        for j in range(3):
            if mat[i + col * 3][j + riga * 3] == n:
                return False
    return True


def legale(mat, x, y, n):
    return check_riga(mat, x, n) and check_colonna(mat, y, n) and check_quadrato(mat, y, x, n)


def solve(matrix):
    for x in range(9):
        for y in range(9):
            if matrix[x][y] == 0:
                for n in range(1, 10):
                    if legale(matrix, x, y, n):
                        matrix[x][y] = n
                        solve(matrix)
                        matrix[x][y] = 0
                return
    stampa(matrix)


if __name__ == "__main__":
    print("\n\nSudoku iniziale: \n")
    stampa(matrix)

    print("\n\nSudoku completato:\n")
    solve(matrix)
