"""
Program which will allow you to play connect four via the command line.
"""

# My version of connect four
import numpy as np
from tabulate import tabulate

tabulate.PRESERVE_WHITESPACE = True


class Connect4Board:
    def __init__(self, rows=6, cols=7):
        # Init Connect4 game board
        self.rows = rows
        self.cols = cols
        self.empty_marker = "_"
        self.board_state = np.full((6, 7), self.empty_marker, dtype="<U9")
        self.no_winner = True
        self.player_tokens = {
            "1": "X",
            "2": "O",
        }

    def show(self):
        # Show current board state
        print(tabulate(np.flip(self.board_state, 0), tablefmt="simple_grid"))

    def valid_move(self, row, col):
        valid = True
        # Check whether move is valid
        if not 0 <= col <= self.cols - 1:
            valid = False
            print(f"Col index {col + 1} is not within range {1} - {self.cols}")
            return False

        if not 0 <= row <= self.rows - 1:
            valid = False
            print(f"Column is full")

        return valid

    def get_rows(self, col):
        # Check which rows are available for column
        if not 0 <= col <= self.cols - 1:
            return -1
        for r in range(self.rows):
            if self.board_state[r][col] == self.empty_marker:
                return r

    def play_piece(self, player, col):
        # Player plays a piece
        col = col - 1
        row = self.get_rows(col)

        if self.valid_move(row, col):
            self.valid_input = True
            self.board_state[row, col] = self.player_tokens[
                str(player)
            ]  # player makes move
        else:
            return

        # Check if that move won the game
        winner = self.check_game_over(player, row, col)

        if winner:
            print(f"Game over, player {player} wins!")
            self.no_winner = False

    def check_game_almost_over(self, player, row, col):
        # Check board state to see if game is almost over
        # (for computer use)

        # Check horizontal, check if row has 3 in a row
        for cc in range(self.cols - 2):
            if (0 <= cc <= self.cols - 1) and (0 <= cc + 2 <= self.cols - 1):
                if (
                    self.board_state[row][cc] == self.player_tokens[str(player)]
                    and self.board_state[row][cc + 1] == self.player_tokens[str(player)]
                    and self.board_state[row][cc + 2] == self.player_tokens[str(player)]
                ):
                    return True

        # Check vertical, check if col has 3 in a row
        for rr in range(self.rows - 2):
            if (0 <= rr <= self.rows - 1) and (0 <= rr + 2 <= self.rows - 1):
                if (
                    self.board_state[rr][col] == self.player_tokens[str(player)]
                    and self.board_state[rr + 1][col] == self.player_tokens[str(player)]
                    and self.board_state[rr + 2][col] == self.player_tokens[str(player)]
                ):
                    return True

        # Check right diagonal, check if diag has 4 in a row
        # TODO: Add conditions so that the checks don't go off the board.
        for offset in range(0, 3):
            if (
                (0 <= row - offset <= self.rows - 1)
                and (0 <= row - offset + 2 <= self.rows - 1)
                and (0 <= col - offset <= self.cols - 1)
                and (0 <= col - offset + 2 <= self.cols - 1)
            ):
                if (
                    self.board_state[row - offset][col - offset]
                    == self.player_tokens[str(player)]
                    and self.board_state[row - offset + 1][col - offset + 1]
                    == self.player_tokens[str(player)]
                    and self.board_state[row - offset + 2][col - offset + 2]
                    == self.player_tokens[str(player)]
                ):
                    return True

        # Check left diagonal, check if left diag has 3 in a row
        for offset in range(0, 3):
            if (
                (0 <= row + offset <= self.rows - 1)
                and (0 <= row + offset - 2 <= self.rows - 1)
                and (0 <= col - offset <= self.cols - 1)
                and (0 <= col - offset + 2 <= self.cols - 1)
            ):
                if (
                    self.board_state[row + offset][col - offset]
                    == self.player_tokens[str(player)]
                    and self.board_state[row + offset - 1][col - offset + 1]
                    == self.player_tokens[str(player)]
                    and self.board_state[row + offset - 2][col - offset + 2]
                    == self.player_tokens[str(player)]
                ):
                    return True
        return False

    def check_game_over(self, player, row, col):
        # Check board state to see if game is over

        # Check horizontal, check if row has 4 in a row
        for cc in range(self.cols - 3):
            if (0 <= cc <= self.cols - 1) and (0 <= cc + 3 <= self.cols - 1):
                if (
                    self.board_state[row][cc] == self.player_tokens[str(player)]
                    and self.board_state[row][cc + 1] == self.player_tokens[str(player)]
                    and self.board_state[row][cc + 2] == self.player_tokens[str(player)]
                    and self.board_state[row][cc + 3] == self.player_tokens[str(player)]
                ):
                    return True

        # Check vertical, check if col has 4 in a row
        for rr in range(self.rows - 3):
            if (0 <= rr <= self.rows - 1) and (0 <= rr + 3 <= self.rows - 1):
                if (
                    self.board_state[rr][col] == self.player_tokens[str(player)]
                    and self.board_state[rr + 1][col] == self.player_tokens[str(player)]
                    and self.board_state[rr + 2][col] == self.player_tokens[str(player)]
                    and self.board_state[rr + 3][col] == self.player_tokens[str(player)]
                ):
                    return True

        # Check right diagonal, check if diag has 4 in a row
        # TODO: Add conditions so that the checks don't go off the board.
        for offset in range(0, 4):
            if (
                (0 <= row - offset <= self.rows - 1)
                and (0 <= row - offset + 3 <= self.rows - 1)
                and (0 <= col - offset <= self.cols - 1)
                and (0 <= col - offset + 3 <= self.cols - 1)
            ):
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
                (0 <= row + offset <= self.rows - 1)
                and (0 <= row + offset - 3 <= self.rows - 1)
                and (0 <= col - offset <= self.cols - 1)
                and (0 <= col - offset + 3 <= self.cols - 1)
            ):
                if (
                    self.board_state[row + offset][col - offset]
                    == self.player_tokens[str(player)]
                    and self.board_state[row + offset - 1][col - offset + 1]
                    == self.player_tokens[str(player)]
                    and self.board_state[row + offset - 2][col - offset + 2]
                    == self.player_tokens[str(player)]
                    and self.board_state[row + offset - 3][col - offset + 3]
                    == self.player_tokens[str(player)]
                ):
                    return True
        return False


def play_connect4():
    # Init empty board
    game = Connect4Board()
    game_mode = int(
        input(f"Would you like to play against a computer (1) or a person (2)")
    )

    if game_mode == 1:  # Playing against a computer
        move_history = []
        while game.no_winner:  # no one has won yet
            for player in [1, 2]:
                game.valid_input = False
                while not game.valid_input:
                    if not game.no_winner:
                        break

                    if player == 2:
                        # Tell computer to play a move
                        print("Computer player 2 is making a move")
                        get_player_1_row = game.get_rows(move_history[-1])
                        if game.check_game_almost_over(
                            1, get_player_1_row - 1, move_history[-1]
                        ):
                            # Have computer player block
                            print("Player 1 has 3 in a row")
                        col = np.random.randint(
                            move_history[-1] - 1, move_history[-1] + 1
                        )
                    else:
                        # Play a turn
                        col = int(input(f"Player {player} Select a Column (1-7):"))
                        move_history.append(col)

                    game.play_piece(player, col)  # play piece for player 1

                    game.show()
    elif game_mode == 2:  # Playing against a person
        while game.no_winner:  # no one has won yet
            for player in [1, 2]:
                game.valid_input = False
                while not game.valid_input:
                    if not game.no_winner:
                        break

                    # Play a turn
                    col = int(input(f"Player {player} Select a Column (1-7):"))

                    game.play_piece(player, col)  # play piece for player 1

                    game.show()
    else:
        raise ValueError(
            "Please choose either 1 for playing against computer or 2 for playing against a person!"
        )


if __name__ == "__main__":
    play_connect4()
