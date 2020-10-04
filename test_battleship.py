from unittest import TestCase
import unittest
from BattleShip import BattleShip
from unittest.mock import patch
from configparser import ConfigParser


class TestInit(unittest.TestCase):

# read

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
        self.assertEqual(expected_player_board_player_one, self.battleship.primary_board_player_one)

    def test_read_computer_opponent_type_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_opponent_type = self.battleship.COMPUTER_OPPONENT
        # call method of object BattleShip
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(expected_opponent_type, observed_opponent_type)

    def test_read_game_difficulty_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # when
        expected_game_difficulty = self.battleship.EASY_DIFFICULTY
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

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
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)
        self.assertEqual(expected_opponent_type, observed_opponent_type)

# validate

    @patch('BattleShip.BattleShip.validate_carrier_points', return_value=True)
    def test_validate_game_difficulty(self, validate_carrier_points):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_game_difficulty = False
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.validate_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

    @patch('BattleShip.BattleShip.validate_game_difficulty', return_value=True)
    def test_validate_carrier_points(self, validate_game_difficulty):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_carrier

        # assert
        self.assertEqual(expected_result, observed_result)

    @patch('BattleShip.BattleShip.validate_game_difficulty', return_value=True)
    def test_validate_carrier_computer_points(self, validate_game_difficulty):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_carrier_computer

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_battleship_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_battleship

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_battleship_computer_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_battleship_computer

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_destroyer_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_destroyer

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_destroyer_computer_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_destroyer_computer

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_patrol_boat_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_patrol_boat

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_patrol_boat_computer_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_patrol_boat_computer

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_submarine_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_submarine

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_submarine_computer_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_submarine_computer

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_battleship_overlap(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_ship_overlap.ini')

        # run start_game function to place all the points
        self.battleship.start_game()

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_battleship_overlap

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_destroyer_overlap(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_ship_overlap.ini')

        # run start_game function to place all the points
        self.battleship.start_game()

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_destroyer_overlap

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_patrol_boat_overlap(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_ship_overlap.ini')

        # run start_game function to place all the points
        self.battleship.start_game()

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_patrol_boat_overlap

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_submarine_overlap(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_ship_overlap.ini')

        # run start_game function to place all the points
        self.battleship.start_game()

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_submarine_overlap

        # assert
        self.assertEqual(expected_result, observed_result)

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
        # call method of object BattleShip
        self.battleship.start_game()
        observed_primary_board_player_one = self.battleship.get_primary_board_player_one()

        # assert
        self.assertEqual(expected_primary_board_player_one, observed_primary_board_player_one)