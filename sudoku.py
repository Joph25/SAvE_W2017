# ---------------------------------------------------------------------------------------------------------
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


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
            triple_i = start_i * 3 + k
            triple_j = start_j * 3 + l
            if sudoku[triple_i][triple_j] == x:
                return False
    return True


# ---------------------------------------------------------------------------------------------------------
def solve_sudoku(i, j):
    # print_sudoku()
    old_value = sudoku[i][j]
    for x in range(1, 10):  # range goes from 1 to 9 (not including 10) in whole number steps
        if not check_value(x, i, j):
            continue
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
    for i in range(9):
        if i % 3 == 0:
            print("|---+---+---|")
        for j in range(9):
            if j % 3 == 0:
                print("|", end='')
            print(sudoku[i][j], end='')
        print("|")
    print("|---+---+---|")
    print()


# ---------------------------------------------------------------------------------------------------------
def main():
    print_sudoku()
    if solve_sudoku(0, 0):
        print("Sudoku gelöst!")
        print_sudoku()
    else:
        # print_sudoku()
        print("Sudoku nicht gelöst")


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
