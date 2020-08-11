import pytest

from tamagotchi.classes.game_board import GameBoard
from tamagotchi.abstract.actor import Actor


class TestGameBoard:

    def test_create_game_board(self):
        game_board = GameBoard(0, 0)

        assert isinstance(game_board, GameBoard)

    def test_game_board_get_actor(self):
        game_board = GameBoard(0, 0)

        assert isinstance(game_board.get_actor(), Actor) 
    
    def test_game_board_get_board_size(self):
        game_board = GameBoard(10, 20)

        assert game_board.get_board_size() == (10, 20)

    def test_game_board_get_game_state(self):
        game_board = GameBoard(10, 20)

        assert game_board.get_game_over() == False
    
    def test_game_board_get_game_state_is_over(self):
        game_board = GameBoard(10, 20)

        game_board.game_over = True

        assert game_board.get_game_over() == True
