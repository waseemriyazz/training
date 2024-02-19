def display_board(board):
    for row in board:
        print("|".join(row))
    print()


def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == ' '


def make_move(board, row, col, symbol):
    board[row][col] = symbol


def check_win(board, symbol):
    size = len(board)
    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == symbol for j in range(size)) or all(board[j][i] == symbol for j in range(size)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(size)) or all(board[i][size - 1 - i] == symbol for i in range(size)):
        return True
    return False


def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)