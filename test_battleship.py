from unittest import TestCase
import unittest
import utils
from BattleShip import BattleShip
from unittest.mock import patch
from configparser import ConfigParser


class TestBattleShip(unittest.TestCase):

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

        # assert
        self.assertEqual(expected_player_board_player_one, self.battleship.player.primary_board_player_one)

    def test_read_computer_opponent_type_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
        self.constants = utils.Constants()

        # when
        expected_opponent_type = 1
        # call method of object BattleShip
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(expected_opponent_type, observed_opponent_type)

    def test_read_game_difficulty_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
        self.constants = utils.Constants()

        # when
        expected_game_difficulty = 1
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

    def test_read_value_without_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()
        self.constants = utils.Constants()

        # when
        expected_game_difficulty = 1
        expected_opponent_type = 1
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)
        self.assertEqual(expected_opponent_type, observed_opponent_type)

# validate

    def test_validate_game_difficulty(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_game_difficulty = False
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.validate_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

# start game

    def test_start_game(self):
        # given
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_primary_board_player_one = [
            [0, 0, 0, 0, 0, 0, 0, 3, 3, 3],
            [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        expected_primary_board_computer = [
            [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
            [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        # call method of object BattleShip
        self.battleship.start_game()
        observed_primary_board_player_one = self.battleship.player.get_primary_board_player_one()
        observed_primary_board_computer = self.battleship.computer.get_primary_board_computer()

        # assert
        self.assertEqual(expected_primary_board_player_one, observed_primary_board_player_one)
        self.assertEqual(expected_primary_board_computer, observed_primary_board_computer)

    def test_end_game(self):
        # given
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        observed_result = self.battleship.play_game()

        expected_result = True

        # assert
        self.assertEqual(observed_result, expected_result)
