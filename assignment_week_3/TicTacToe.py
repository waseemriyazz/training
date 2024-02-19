from player_input import get_player_names, get_player_symbols
from board_setup import get_board_size, initialize_board
from game_logic import display_board, is_valid_move, make_move, check_win, check_draw
from game_statistics import display_statistics

def play_tic_tac_toe():
    player1_name, player2_name = get_player_names()
    player1_symbol, player2_symbol = get_player_symbols(player1_name, player2_name)
    size = get_board_size()
    board = initialize_board(size)
    # Initialize game statistics variables
    player1_wins = player2_wins = draws = total_games = 0

    while True:
        display_board(board)

        # Alternate turns between players
        if total_games % 2 == 0:
            current_player, symbol = player1_name, player1_symbol
        else:
            current_player, symbol = player2_name, player2_symbol

        print(f"{current_player}'s turn ({symbol})")

        # Get player move
        while True:
            try:
                row = int(input("Enter row (0-based): "))
                col = int(input("Enter column (0-based): "))
                if is_valid_move(board, row, col):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter integers for row and column.")

        make_move(board, row, col, symbol)

        # Check for win or draw
        if check_win(board, symbol):
            display_board(board)
            print(f"{current_player} wins!")
            if current_player == player1_name:
                player1_wins += 1
            else:
                player2_wins += 1
            total_games += 1
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            draws += 1
            total_games += 1
            break

        total_games += 1

    display_statistics(player1_name, player2_name, player1_wins, player2_wins, draws, total_games)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == 'yes'


if __name__ == "__main__":
    while play_tic_tac_toe():
        pass