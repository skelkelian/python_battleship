from unittest import TestCase
import unittest
from battleship import BattleShip
from configparser import ConfigParser


class TestInit(unittest.TestCase):
    def test_player_board_one(self):
        # given
        expected_player_board_player_one = [
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
        self.assertEqual(self.battleship.primary_board_player_one, expected_player_board_player_one)

    def test_read_computer_opponent_type_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_opponent_type = self.battleship.COMPUTER_OPPONENT
        # call method of object BattleShip
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(observed_opponent_type, expected_opponent_type)

    def test_read_game_difficulty_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_game_difficulty = self.battleship.EASY_DIFFICULTY
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(observed_game_difficulty, expected_game_difficulty)

    def test_read_value_without_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_game_difficulty = self.battleship.EASY_DIFFICULTY
        expected_opponent_type = self.battleship.COMPUTER_OPPONENT
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(observed_game_difficulty, expected_game_difficulty)
        self.assertEqual(observed_opponent_type, expected_opponent_type)

    def test_validate_game_difficulty(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_game_difficulty = self.battleship.EASY_DIFFICULTY
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(observed_game_difficulty, expected_game_difficulty)

    def test_start_game(self):
        # given
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_primary_board_player_one = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        # call method of object BattleShip
        self.battleship.start_game()
        observed_primary_board_player_one = self.battleship.get_primary_board_player_one()

        # assert
        self.assertEqual(observed_primary_board_player_one, expected_primary_board_player_one)



    # def test_simulate_game(self):
    #     # create an object of class BattleShip
    #     self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
    #
    #     self.battleship.print_directions()
    #
    #
    #
    #     # assert
    #     self.assertEqual(1,1)


# class TestBattleShip(unittest.TestCase):
    # def setUp(self):
    #     self.battleship = BattleShip()  # creating an object
        # class contains methods/functions and fields/attributes
        # method is a function in a class
        # watch introductory python vid abt classes and methods
        # figure out what python self is from yt

