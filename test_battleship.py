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
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
        # does the line above matter because we are not extracting a value from config file in this function?

        # assert
        self.assertEqual(self.battleship.primary_board_player_one, expected)

    def test_read_computer_opponent_type_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_opponent_type = 1
        # call an object of class BattleShip
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(observed_opponent_type, expected_opponent_type)

    def test_read_game_difficulty_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_game_difficulty = 1
        # call object of class BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(observed_game_difficulty, expected_game_difficulty)

    def test_read_value_without_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_game_difficulty = 1
        expected_opponent_type = 1
        # call object of class BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(observed_game_difficulty, expected_game_difficulty)
        self.assertEqual(observed_opponent_type, expected_opponent_type)

    def test_simulate_game(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        self.battleship.print_directions()



        # assert
        self.assertEqual(1,1)


# class TestBattleShip(unittest.TestCase):
    # def setUp(self):
    #     self.battleship = BattleShip()  # creating an object
        # class contains methods/functions and fields/attributes
        # method is a function in a class
        # watch introductory python vid abt classes and methods
        # figure out what python self is from yt

