def solve(col, n, board, leftRow, upperDiagonal, lowerDiagonal):
    if col == n:
        for row in range(n):
            print(board[row])
        print()
        return

    for row in range(n):
        if (leftRow[row] == 0 and upperDiagonal[n - 1 + col - row] == 0
                and lowerDiagonal[row + col] == 0):
            board[row][col] = 1
            leftRow[row] = 1
            lowerDiagonal[row + col] = 1
            upperDiagonal[n - 1 + col - row] = 1
            solve(col + 1, n, board, leftRow, upperDiagonal, lowerDiagonal)
            board[row][col] = 0
            leftRow[row] = 0
            lowerDiagonal[row + col] = 0
            upperDiagonal[n - 1 + col - row] = 0


def initialise():
    n = int(input("Enter the dimension: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    leftRow = [0] * n
    upperDiagonal = [0] * (2 * n - 1)
    lowerDiagonal = [0] * (2 * n - 1)
    solve(0, n, board, leftRow, upperDiagonal, lowerDiagonal)


initialise()
