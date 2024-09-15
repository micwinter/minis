"""
Program which will allow you to play connect four via the command line.
"""

# My version of connect four
import numpy as np
from tabulate import tabulate


class Connect4Board:
    def __init__(self, rows=6, cols=7):
        # Init Connect4 game board
        self.rows = rows
        self.cols = cols
        self.board_state = np.zeros((rows, cols))
        self.no_winner = True

    def show(self):
        # Show current board state
        print(tabulate(np.flip(self.board_state, 0), tablefmt="grid"))

    # TODO: Add valueerror if you add submit an invalid input

    def valid_move(self, row, col):
        valid = True
        # Check whether move is valid
        # TODO: Change col to be min val < col < max val
        if not col in range(self.cols):
            valid = False

        if not row in range(self.rows):
            valid = False

        if valid == False:
            raise ValueError  # , f"{col} is not within range {0} - {self.cols - 1} or {row} is not within range {0} - {self.rows - 1}"
        else:
            return True

    def get_rows(self, col):
        # Check which rows are available for column
        for r in range(self.rows):
            if self.board_state[r][col] == 0:
                return r

    def play_piece(self, player, col):
        # Player plays a piece
        row = self.get_rows(col)
        if self.valid_move(row, col):
            self.board_state[row, col] = player  # player makes move

        # Check if that move won the game
        winner = self.check_game_over(player, row, col)

        if winner:
            print(f"Game over, player {player} wins!")
            self.no_winner = False

    def check_game_over(self, player, row, col):
        # Check board state to see if game is over

        # Check horizontal, check if row has 4 in a row
        for cc in range(self.cols - 3):
            if (
                self.board_state[row][cc] == player
                and self.board_state[row][cc + 1] == player
                and self.board_state[row][cc + 2] == player
                and self.board_state[row][cc + 3] == player
            ):
                return True

        # Check vertical, check if col has 4 in a row
        for rr in range(self.rows - 3):
            if (
                self.board_state[rr][col] == player
                and self.board_state[rr + 1][col] == player
                and self.board_state[rr + 2][col] == player
                and self.board_state[rr + 3][col] == player
            ):
                return True

        # TODO: Don't do a whole for loop, can optimize the diagonals
        # Only need one forloop over each of the offsets from -3 to 0, one forloop
        # x+n, y-n (negative)

        # Check right diagonal, check if diag has 4 in a row
        for cc in range(self.cols - 3):
            for rr in range(self.rows - 3):
                if (
                    self.board_state[rr][cc] == player
                    and self.board_state[rr + 1][cc + 1] == player
                    and self.board_state[rr + 2][cc + 2] == player
                    and self.board_state[rr + 3][cc + 3] == player
                ):
                    return True

        # Check left diagonal, check if left diag has 4 in a row
        # TODO: can do a bounds check to make sure you're not looking at the wrong offset.
        for cc in range(self.cols - 3):
            for rr in range(3, self.rows):
                if (
                    self.board_state[rr][cc] == player
                    and self.board_state[rr - 1][cc + 1] == player
                    and self.board_state[rr - 2][cc + 2] == player
                    and self.board_state[rr - 3][cc + 3] == player
                ):
                    return True
        return False


def play_connect4():
    # Init empty board
    game = Connect4Board()
    inputs = [0, 6, 1, 6, 2, 6, 3]
    while game.no_winner:  # no one has won yet
        # Play a turn
        # col = int(input("Player 1 Select a Column (0-6):"))
        for col in inputs:

            game.play_piece(1, col)  # play piece for player 1
            print(game.no_winner)
            # game.check_game_over()  # check if game is over
            game.show()

            # col = int(input("Player 2 Select a Column (0-6):"))
            game.play_piece(2, col)  # play piece for player 2
            print(game.no_winner)
            # game.check_game_over()
            game.show()  # Show board


if __name__ == "__main__":
    play_connect4()
