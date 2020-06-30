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

    def test_read_computer_config_file(self):
        # given
        config = ConfigParser()
        config.read('config.ini')

        # when
        expected_opponent_type = 1
        observed_opponent_type = int(config.get('main', 'opponent_type'))

        # assert
        self.assertEqual(observed_opponent_type, expected_opponent_type)



# class TestBattleShip(unittest.TestCase):
    # def setUp(self):
    #     self.battleship = BattleShip()  # creating an object
        # class contains methods/functions and fields/attributes
        # method is a function in a class
        # watch introductory python vid abt classes and methods
        # figure out what python self is from yt

