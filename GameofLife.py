"""
Program which will allow you to play the Game of Life via the command line.
"""

import numpy as np
from tabulate import tabulate
from time import sleep


class LifeBoard:
    def __init__(self, rows=25, cols=25):
        # Init game board
        self.rows = rows
        self.cols = cols
        self.empty_marker = "_"
        self.current_board_state = np.full((rows, cols), self.empty_marker, dtype="<U9")
        self.new_board_state = np.full((rows, cols), self.empty_marker, dtype="<U9")
        self.life_states = {
            "1": "X",
            "2": "O",
        }
        # Randomly initialize life
        initial_states = np.random.rand(rows, cols)
        initial_states[initial_states < 0.5] = 1
        initial_states[initial_states != 1] = 0

        # Now apply to board_state
        for row in range(rows):
            for col in range(cols):
                if initial_states[row, col] == 1:
                    self.current_board_state[row, col] = "O"
                    self.new_board_state[row, col] = "O"

                else:
                    self.current_board_state[row, col] = "_"
                    self.new_board_state[row, col] = "_"

    def find_neighbors(self, row, col):
        neighbor_coordinates = []
        for n_row in range(row - 1, row + 2):
            for n_col in range(col - 1, col + 2):
                if n_row == row and n_col == col:
                    continue
                elif n_row < 0 or n_col < 0:
                    continue
                elif n_row > self.rows - 1 or n_col > self.cols - 1:
                    continue

                neighbor_coordinates.append([n_row, n_col])
        life_states = [
            self.current_board_state[rr, cc] for (rr, cc) in neighbor_coordinates
        ]
        life_counts = (life_states.count("O"), life_states.count("_"))

        return life_counts

    def apply_rules(self, center_state, life_counts):
        # Rule 1
        if center_state == "O" and life_counts[0] < 2:
            center_state = "_"
        # Rule 2
        if center_state == "O" and 3 >= life_counts[0] >= 2:
            center_state = "O"
        # Rule 3
        if center_state == "O" and life_counts[0] > 3:
            center_state = "_"
        # Rule 4
        if center_state == "_" and life_counts[0] == 3:
            center_state = "O"

        return center_state

    def mutate(self):
        # Implementating one life mutation
        for row in range(self.rows):
            for col in range(self.cols):
                # Apply rules to current index
                # only apply output mutation to New board state

                self.new_board_state[row, col] = self.apply_rules(
                    self.current_board_state[row, col], self.find_neighbors(row, col)
                )

        self.current_board_state = self.new_board_state.copy()

    def show(self):
        # Show current board state
        print(tabulate(np.flip(self.new_board_state, 0), tablefmt="simple_grid"))


def play_game_of_life():
    # Init empty board
    game = LifeBoard()

    mutations = 0
    while mutations <= 500:  # Game of Life is lifing
        game.mutate()

        mutations += 1
        game.show()
        sleep(0.1)


if __name__ == "__main__":
    play_game_of_life()
