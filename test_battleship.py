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

    def test_validate_game_difficulty(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_game_difficulty = self.battleship.EASY_DIFFICULTY
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

    def test_validate_carrier_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_success

        # assert
        self.assertEqual(expected_result, observed_result)

    # def test_ship_sunk(self):
    #     pass

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

# SOMETHING UNUSUAL HAPPENED
# I TOOK THE SHIP POINTS OUT OF THE SECOND CONFIG FILE (CONFIG FILE W ERRORS) AND IT STILL WORKED
# THIS IS NORMAL AND LOGICAL AND WHAT I THINK SHOULD HAPPEN HOWEVER, WHEN I WAS WORKING ON THE FIRST
# SHIP PLACEMENTS (CARRIER), I NEEDED TO PUT THE VALUES IN BOTH CONFIG FILES. NOW FOR SOME ODD REASON,
# I DON'T NEED TO AND ALL THE TESTS STILL PASS IF I TAKE OUT CARRIER & BATTLESHIP FROM SECOND CONFIG FILE
