from unittest import TestCase
import unittest
import utils
from unittest.mock import patch
from destroyer import Destroyer
from ship import Ship
from configparser import ConfigParser


class TestDestroyer(unittest.TestCase):
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

    def test_validate_destroyer_points(self):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object Destroyer
        observed_result = self.destroyer.validate_destroyer_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_destroyer_player_one(self):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
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

        # call method of class Destroyer
        observed_result = self.destroyer.place_destroyer_player_one(config)

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('player.Player.get_hit_counter_player', return_value=[2, 3, 3, 0, 0])
    def test_ship_sunk_destroyer_player(self, get_hit_counter_player):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Destroyer
        observed_result = self.destroyer.ship_sunk_destroyer_player()

        self.assertEqual(expected_result, observed_result)

    @patch('player.Player.get_primary_board_player_one', return_value=mocked_primary_board)
    def test_validate_destroyer_overlap(self, get_primary_board_player_one):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_ship_overlap.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.destroyer.validate_destroyer_overlap(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_destroyer_computer_points(self):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object Destroyer
        observed_result = self.destroyer.validate_destroyer_computer_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_destroyer_computer(self):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
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

        # call method of class Destroyer
        observed_result = self.destroyer.place_destroyer_computer(config)

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('ship.Ship.get_hit_counter_computer', return_value=[2, 3, 3, 0, 0])
    def test_ship_sunk_destroyer_computer(self, get_hit_counter_computer):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Destroyer
        observed_result = self.destroyer.ship_sunk_destroyer_computer()

        self.assertEqual(expected_result, observed_result)

    @patch('ship.Ship.get_primary_board_computer', return_value=mocked_primary_board_computer)
    def test_validate_destroyer_computer_overlap(self, get_primary_board_computer):
        # create an object of class Destroyer
        self.destroyer = Destroyer()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_ship_overlap.ini')

        # when
        expected_result = False
        # call method of object BattleShip
        observed_result = self.destroyer.validate_destroyer_computer_overlap(config)

        # assert
        self.assertEqual(expected_result, observed_result)
