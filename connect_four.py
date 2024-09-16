"""
Program which will allow you to play connect four via the command line.
"""

# My version of connect four
import numpy as np
from tabulate import tabulate
from colorama import Fore, Style


class Connect4Board:
    def __init__(self, rows=6, cols=7):
        # Init Connect4 game board
        self.rows = rows
        self.cols = cols
        self.board_state = np.full((6, 7), ".", dtype="<U9")
        self.no_winner = True
        # red_token = Fore.RED + "O" + Style.RESET_ALL
        # blue_token = Fore.BLUE + "O" + Style.RESET_ALL
        self.player_tokens = {}
        # self.player_tokens = {
        #     "1": red_token,
        #     "2": blue_token,
        # }
        self.player_tokens = {
            "1": "X",
            "2": "O",
        }

    def show(self):
        # Show current board state
        print(tabulate(np.flip(self.board_state, 0), tablefmt="grid"))

        # print(tabulate(self.board_state, tablefmt="grid"))

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
            if self.board_state[r][col] == ".":
                return r

    def play_piece(self, player, col):
        # Player plays a piece
        row = self.get_rows(col)

        if self.valid_move(row, col):
            self.board_state[row, col] = self.player_tokens[
                str(player)
            ]  # player makes move

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
                self.board_state[row][cc] == self.player_tokens[str(player)]
                and self.board_state[row][cc + 1] == self.player_tokens[str(player)]
                and self.board_state[row][cc + 2] == self.player_tokens[str(player)]
                and self.board_state[row][cc + 3] == self.player_tokens[str(player)]
            ):
                return True

        # Check vertical, check if col has 4 in a row
        for rr in range(self.rows - 3):
            if (
                self.board_state[rr][col] == self.player_tokens[str(player)]
                and self.board_state[rr + 1][col] == self.player_tokens[str(player)]
                and self.board_state[rr + 2][col] == self.player_tokens[str(player)]
                and self.board_state[rr + 3][col] == self.player_tokens[str(player)]
            ):
                return True

        # Check right diagonal, check if diag has 4 in a row
        for offset in range(0, 4):
            if (
                self.board_state[row - offset][col - offset]
                == self.player_tokens[str(player)]
                and self.board_state[row - offset + 1][col - offset + 1]
                == self.player_tokens[str(player)]
                and self.board_state[row - offset + 2][col - offset + 2]
                == self.player_tokens[str(player)]
                and self.board_state[row - offset + 3][col - offset + 3]
                == self.player_tokens[str(player)]
            ):
                return True

        # Check left diagonal, check if left diag has 4 in a row
        for offset in range(0, 4):
            if (
                self.board_state[row - offset][col - offset]
                == self.player_tokens[str(player)]
                and self.board_state[row - offset - 1][col - offset + 1]
                == self.player_tokens[str(player)]
                and self.board_state[row - offset - 2][col - offset + 2]
                == self.player_tokens[str(player)]
                and self.board_state[row - offset - 3][col - offset + 3]
                == self.player_tokens[str(player)]
            ):
                return True
        return False


def play_connect4():
    # Init empty board
    game = Connect4Board()
    while game.no_winner:  # no one has won yet
        for player in [1, 2]:
            if not game.no_winner:
                break

            # Play a turn
            col = int(input(f"Player {player} Select a Column (0-6):"))

            game.play_piece(player, col)  # play piece for player 1

            game.show()
            # print(game.board_state)


if __name__ == "__main__":
    play_connect4()
