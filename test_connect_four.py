"""
Tests for connect4 game
"""

import pytest
from connect_four import Connect4Board


def test_gameover():
    game = Connect4Board()
    game.board_state = [
        ["_", "_", "X", "O", "O", "O", "X"],
        ["_", "_", "X", "X", "X", "X", "O"],
        ["_", "_", "_", "O", "O", "_", "_"],
        ["_", "_", "_", "X", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
    ]
    winner = game.check_game_over(1, 1, 2)
    assert winner == 1

    game = Connect4Board()
    game.board_state = [
        ["_", "_", "X", "O", "O", "O", "X"],
        ["_", "_", "O", "X", "X", "X", "O"],
        ["_", "_", "_", "O", "O", "_", "_"],
        ["_", "_", "_", "X", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_"],
    ]
    winner = game.check_game_over(1, 1, 2)
    assert winner == False


def test_overflow():
    game = Connect4Board()
    game.board_state = [
        ["_", "_", "X", "O", "O", "O", "X"],
        ["_", "_", "O", "X", "X", "X", "O"],
        ["_", "_", "_", "O", "O", "_", "_"],
        ["_", "_", "_", "X", "_", "_", "_"],
        ["_", "_", "_", "O", "_", "_", "_"],
        ["_", "_", "_", "X", "_", "_", "_"],
    ]
    assert game.valid_move(6, 3) == False
    assert game.valid_move(3, 4) == True
    assert game.valid_move(6, 4) == False
    assert game.valid_move(4, 7) == False
