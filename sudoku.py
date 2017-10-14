# ---------------------------------------------------------------------------------------------------------
sudoku = [[7, 9, 0, 0, 0, 0, 3, 0, 0],
          [0, 0, 0, 0, 0, 6, 9, 0, 0],
          [8, 0, 0, 0, 3, 0, 0, 7, 6],
          [0, 0, 0, 0, 0, 5, 0, 0, 2],
          [0, 0, 5, 4, 1, 8, 7, 0, 0],
          [4, 0, 0, 7, 0, 0, 0, 0, 0],
          [6, 1, 0, 0, 9, 0, 0, 0, 8],
          [0, 0, 2, 3, 0, 0, 0, 0, 0],
          [0, 0, 9, 0, 0, 0, 0, 5, 4],
          ]


# ---------------------------------------------------------------------------------------------------------
def check_value(x, i, j):
    if sudoku[i][j] == x:
        return True
    if sudoku[i][j] != 0:
        return False
    # check horizontal
    for k in range(9):
        if sudoku[k][j] == x:
            return False
            # check vertical
    for k in range(9):
        if sudoku[i][k] == x:
            return False
            # check 3x3 surroundings
    start_i = i // 3
    start_j = j // 3
    for k in range(3):
        for l in range(3):
            if sudoku[start_i * 3 + k][start_j * 3 + l] == x:
                return False
    return True


# ---------------------------------------------------------------------------------------------------------
def solve_sudoku(i, j):
    old_value = sudoku[i][j]
    for x in range(1, 9):
        if not check_value(x, i, j):
            break
        sudoku[i][j] = x
        # increment field position
        next_i = i + 1
        next_j = j
        if next_i > 8:
            next_j = j + 1
            next_i = 0
        if next_j > 8:
            return True  # if end of sudoku reached ---> sudoku solved
        if solve_sudoku(next_i, next_j):
            return True
        sudoku[i][j] = old_value

    return False


# ---------------------------------------------------------------------------------------------------------
def print_sudoku():
    print("|---+---+---|")
    for i in range(9):
        for j in range(9):
            if j%3 == 0:
                print ("|",end='')
            print(sudoku[i][j], end='')
        print("|")
        print("|---+---+---|")


# ---------------------------------------------------------------------------------------------------------
def main():
    print_sudoku()
    if solve_sudoku(0, 0):
        print("Sudoku gelöst!")
        print_sudoku()
    else:
        print("Sudoku nicht gelöst")


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
