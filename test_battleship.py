from unittest import TestCase
import unittest
from battleship import BattleShip
from configparser import ConfigParser

class TestInit(unittest.TestCase):
    def test_player_board_1(self):
        # given
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        # when
        self.battleship = BattleShip()

        # assert
        self.assertEqual(self.battleship.primary_board_player_one, expected)

    def test_read_computer_gamemode_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_opponent_type = 1
        # call an object of class BattleShip
        observed_opponent_type = self.battleship.pick_gamemode()

        # assert
        self.assertEqual(observed_opponent_type, expected_opponent_type)

    def test_read_game_difficulty_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_game_difficulty = 1
        # call object of class BattleShip
        observed_game_difficulty = self.battleship.pick_game_difficulty()

        # assert
        self.assertEqual(observed_game_difficulty, expected_game_difficulty)


# class TestBattleShip(unittest.TestCase):
    # def setUp(self):
    #     self.battleship = BattleShip()  # creating an object
        # class contains methods/functions and fields/attributes
        # method is a function in a class
        # watch introductory python vid abt classes and methods
        # figure out what python self is from yt

