from unittest import TestCase
import unittest
from battleship import BattleShip

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

# class TestBattleShip(unittest.TestCase):
    # def setUp(self):
    #     self.battleship = BattleShip()  # creating an object
        # class contains methods/functions and fields/attributes
        # method is a function in a class
        # watch introductory python vid abt classes and methods
        # figure out what python self is from yt

