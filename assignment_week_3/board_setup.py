def get_board_size():
    size = int(input("Enter the size of the game board (e.g., 3 for 3x3, 4 for 4x4): "))
    return size

def initialize_board(size):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board