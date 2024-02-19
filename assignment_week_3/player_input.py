def get_player_names():
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    return player1_name, player2_name

def get_player_symbols(player1_name, player2_name):
    player1_symbol = input(f"{player1_name}, choose your symbol: ")
    player2_symbol = input(f"{player2_name}, choose your symbol: ")
    return player1_symbol, player2_symbol