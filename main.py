from tic_tac_toe import TicTacToe

print("""
Welcome to Tic Tac Toe!
Player 1 is X.
Player 2 is O.

Rules:

1. The game is played on a grid that's 3 squares by 3 squares.
2. Players take turns putting their marks (X/O) in empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

Constraints:

1. Players can only place their mark on an empty square.
2. Players can only choose grid numbers (1-9).

Example numbers:

 1 | 2 | 3
----------- 
 4 | 5 | 6 
-----------
 7 | 8 | 9
""")

game = TicTacToe()

while game.is_on:
    print("Current Board:")
    game.print_board()

    position = game.play_turn()

    while position < 1 or position > 9:
        print("Wrong position! Try again.")
        position = game.play_turn()

    while not game.update_board(position):
        print("Position is alread taken! Try again.")
        position = game.play_turn()

    result = game.check_winner()
    if result == 1 or result == 2:
        game.print_board()
        print(f"Player {result} wins! 🎉")
        game.is_on = False
    else:
        game.rounds += 1
        if game.rounds == 9:
            print("It's a tie! 🤝")
            game.is_on = False

    game.current_player = 2 if game.current_player == 1 else 1
