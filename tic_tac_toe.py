class TicTacToe:
    """Main game class that handles the game operations for Tic Tac Toe"""

    def __init__(self):
        """Initializes the required variables to play the game"""

        self.n = 3
        self.board = [[" "] * self.n for _ in range(self.n)]
        self.current_player = 1
        self.player_map = {1: "X", 2: "O"}
        self.is_on = True
        self.rounds = 0

    def print_board(self):
        """Prints the current game board like an actual game"""

        print(end="\n")
        for i in range(self.n):
            for j in range(self.n):
                print(f" {self.board[i][j]} ", end="")
                if j < self.n - 1:
                    print("|", end="")
            print()
            if i < self.n - 1:
                print("-" * (3 * self.n + (self.n - 1)))
        print(end="\n")

    def play_turn(self):
        """Takes player's input for the position to place their marks"""

        return int(
            input(
                f"Player {self.current_player} ({self.player_map[self.current_player]}), enter your move (1-9): "
            )
        )

    def update_board(self, pos):
        """Updates the game board after a player's turn"""

        mark = self.player_map[self.current_player]

        for i in range(self.n):
            for j in range(self.n):
                if pos == 1:
                    if self.board[i][j] == " ":
                        self.board[i][j] = mark
                        return True
                    else:
                        return False
                pos -= 1
        return False

    def check_winner(self):
        """Checks row-wise, column-wise, and both diagonal-wise, if any player has won"""

        # row check
        for row in self.board:
            if len(set(row)) == 1 and row[0] != " ":
                return 1 if row[0] == "X" else 2

        # column check
        col_board = [[" "] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                col_board[j][i] = self.board[i][j]

        for row in col_board:
            if len(set(row)) == 1 and row[0] != " ":
                return 1 if row[0] == "X" else 2

        # top-left to bottom-right diagonal check
        diag1 = [self.board[i][i] for i in range(self.n)]
        if len(set(diag1)) == 1 and " " not in diag1:
            return 1 if diag1[0] == "X" else 2

        # top-right to bottom-left diagonal check
        diag2 = [self.board[i][self.n - i - 1] for i in range(self.n)]
        if len(set(diag2)) == 1 and " " not in diag2:
            return 1 if diag2[0] == "X" else 2

        # no one is winner yet
        return 0
