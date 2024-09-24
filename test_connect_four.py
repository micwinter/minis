"""
Tests for connect4 game
"""

import pytest
from connect_four import Connect4Board

# Init empty board
game = Connect4Board()


def test_basics():

    game.board_state = []
    assert game.no_winner == "False"
