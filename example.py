"""
    This is my attempt at the Tamagotchi challenge
    Author: Tristan Andersen
"""

import pygame

from tamagotchi.classes import GameBoard


if __name__ == "__main__":
    game_screen_size = (600, 400)

    game_board = GameBoard(game_screen_size[0], game_screen_size[1])

    game_board.run_game()  # Game loop runs in here, will exit upon closing
