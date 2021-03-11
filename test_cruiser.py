import unittest
import utils
from unittest.mock import patch
from cruiser import Cruiser
from ship import Ship
from configparser import ConfigParser


class TestCruiser(unittest.TestCase):
    mocked_primary_board = [
        [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
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
    mocked_primary_board_computer = [
        [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def test_validate_cruiser_points(self):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False

        # call method of object Cruiser
        observed_result = self.cruiser.validate_cruiser_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_cruiser_player_one(self):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # when
        initial_result = [
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

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty.ini')

        # call method of class Cruiser
        observed_result = self.cruiser.place_cruiser_player_one(config)

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('player.Player.get_hit_counter_player', return_value=[2, 4, 3, 0, 0])
    def test_ship_sunk_cruiser_player(self, get_hit_counter_player):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Cruiser
        observed_result = self.cruiser.ship_sunk_cruiser_player()

        self.assertEqual(expected_result, observed_result)

    @patch('player.Player.get_primary_board_player_one', return_value=mocked_primary_board)
    def test_validate_cruiser_overlap(self, get_primary_board_player_one):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_ship_overlap.ini')

        # when
        expected_result = False

        # call method of object Cruiser
        observed_result = self.cruiser.validate_cruiser_overlap(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_cruiser_computer_points(self):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False

        # call method of object Cruiser
        observed_result = self.cruiser.validate_cruiser_computer_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_cruiser_computer(self):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # when
        initial_result = [
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

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty.ini')

        # call method of class Cruiser
        observed_result = self.cruiser.place_cruiser_computer(config)

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('computer.Computer.get_hit_counter_computer', return_value=[2, 4, 2, 0, 0])
    def test_ship_sunk_cruiser_computer(self, get_hit_counter_computer):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Cruiser
        observed_result = self.cruiser.ship_sunk_cruiser_computer()

        self.assertEqual(expected_result, observed_result)

    @patch('computer.Computer.get_primary_board_computer', return_value=mocked_primary_board_computer)
    def test_validate_cruiser_computer_overlap(self, get_primary_board_player_one):
        # create an object of class Cruiser
        self.cruiser = Cruiser()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_ship_overlap.ini')

        # when
        expected_result = False

        # call method of object Cruiser
        observed_result = self.cruiser.validate_cruiser_computer_overlap(config)

        # assert
        self.assertEqual(expected_result, observed_result)
