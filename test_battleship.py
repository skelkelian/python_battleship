from unittest import TestCase
import unittest
from BattleShip import BattleShip
from unittest.mock import patch
from random import *
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

    def test_validate_battleship_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_battleship

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

    def test_validate_patrol_boat_points(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.battleship.validation_flag_patrol_boat

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

        # MY ISSUE WITH THIS TEST AND WHY IT IS NOT PASSING:
        # self.battleship.primary_board_player_one DOES NOT TAKE FROM THE VALUES I WANT IT TO.

        # MY ASSUMPTION:
        # I RAN self.battleship.start_game() WHICH HAS ALL THE PLACE POINTS FUNCTIONS. THESE FUNCTIONS OBTAIN THE SHIP
        # VALUE FROM WHICH CONFIG FILE WAS CHOSEN IN THE TEST. I CREATED A CONFIG FILE (config_easy_ship_overlap.ini)
        # WHICH HAD SHIP VALUES THAT WOULD OVERLAP. MY IDEA WAS THAT THIS TEST WOULD PLACE THE SHIPS ON THE BOARD THEN
        # CHECK TO SEE IF A POINT OVERLAPPED.

        # FIRST ISSUE WITH ASSUMPTION:
        # THE ISSUE WITH THIS ASSUMPTION IS THAT THE PLACE FUNCTIONS LITERALLY DO
        # NOT CARE IF THERE IS A SHIP THERE OR NOT. THIS MEANS THAT EITHER WAY, A SHIP WILL BE PLACED IN THAT LOCATION
        # AND IF A SHIP WAS THERE ALREADY, THE FUNCTION WOULD JUST REPLACE THE POINT. BECAUSE OF THIS THE SHIPS WILL
        # NEVER OVERLAP WHICH CAUSES MY TEST TO FAIL.

        # SECOND ISSUE WITH ASSUMPTION:
        # NOW, THE ISSUE WITH WHAT I SAID ABOVE IS THAT THIS IS NOT
        # HAPPENING. WHAT IS REALLY HAPPENING IS THAT WHEN I RUN self.battleship.start_game(), IT PLACES ALL THE POINTS
        # BECAUSE THAT IS WHERE ALL THE PLACE POINT FUNCTIONS ARE. MY ASSUMPTION THAT IT WOULD NOT TAKE THE VALUES FROM
        # THE OLD CONFIG FILE WAS COMPLETELY WRONG BECAUSE WHEN I DEBUGGED THIS TEST BY DOING PRINTING THE PRIMARY BOARD
        # (print(self.battleship.primary_board_player_one)) I SAW THE POINTS PLACED FOR THE OTHER CONFIG FILE WHICH WAS
        # (config_easy_difficulty.ini).

        # WHAT I'M THINKING ABOUT WHEN CONSIDERING THESE ISSUES:
        # THE SECOND ISSUE IS THE ISSUE WE ARE DEALING WITH NOW AND IT IS NOT AS MAJOR. THE FIRST ISSUE IS AN ISSUE THAT
        # WE WOULD HAVE FOUND IN THE FUTURE IF I DIDN'T LOOK AT THE PLACE FUNCTIONS CAREFULLY. THIS SECOND ISSUE HOWEVER
        # IS GOING TO NEED A LOT MORE CONSIDERATION TO SEE WHAT WE SHOULD DO ABOUT IT.

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


    # def test_player_pick_points(self):
    #     # given
    #     # create an object of class BattleShip
    #     self.battleship = BattleShip()
    #
    #     # when
    #
    #     # call method of object BattleShip
    #     self.battleship.validate_point_picked()
    #     observed_point_location = self.battleship.()
    #
    #     # assert
    #     # self.assertEqual(expected_point_location, observed_point_location)