import unittest
import utils
from unittest.mock import patch
from patrol_boat import Patrol_Boat
from configparser import ConfigParser


class TestPatrol_Boat(unittest.TestCase):
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

    def test_validate_patrol_boat_points(self):
        # create an object of class Patrol_Boat
        self.patrol_boat = Patrol_Boat()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object Patrol_Boat
        observed_result = self.patrol_boat.validate_patrol_boat_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_patrol_boat_player_one(self):
        # create an object of class Patrol Boat
        self.patrol_boat = Patrol_Boat()
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

        # call method of class Patrol Boat
        observed_result = self.patrol_boat.place_patrol_boat_player_one(config)

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('ship.Ship.get_hit_counter_player', return_value=[2, 3, 1, 2, 0])
    def test_ship_sunk_patrol_boat_player(self, get_hit_counter_player):
        # create an object of class Patrol_Boat
        self.patrol_boat = Patrol_Boat()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Patrol Boat
        observed_result = self.patrol_boat.ship_sunk_patrol_boat_player()

        self.assertEqual(expected_result, observed_result)

    @patch('ship.Ship.get_primary_board_player_one', return_value=mocked_primary_board)
    def test_validate_patrol_boat_overlap(self, get_primary_board_player_one):
        # create an object of class Patrol Boat
        self.patrol_boat = Patrol_Boat()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_ship_overlap.ini')

        # when
        expected_result = False
        # call method of object Patrol Boat
        observed_result = self.patrol_boat.validate_patrol_boat_overlap(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_patrol_boat_computer_points(self):
        # create an object of class Patrol_Boat
        self.patrol_boat = Patrol_Boat()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object Patrol_Boat
        observed_result = self.patrol_boat.validate_patrol_boat_computer_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_patrol_boat_computer(self):
        # create an object of class Patrol Boat
        self.patrol_boat = Patrol_Boat()
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

        # call method of class Patrol Boat
        observed_result = self.patrol_boat.place_patrol_boat_computer(config)

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('ship.Ship.get_hit_counter_computer', return_value=[2, 3, 1, 2, 0])
    def test_ship_sunk_patrol_boat_computer(self, get_hit_counter_computer):
        # create an object of class Patrol_Boat
        self.patrol_boat = Patrol_Boat()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Patrol Boat
        observed_result = self.patrol_boat.ship_sunk_patrol_boat_computer()

        self.assertEqual(expected_result, observed_result)

    @patch('ship.Ship.get_primary_board_computer', return_value=mocked_primary_board_computer)
    def test_validate_patrol_boat_computer_overlap(self, get_primary_board_player_one):
        # create an object of class Patrol Boat
        self.patrol_boat = Patrol_Boat()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_ship_overlap.ini')

        # when
        expected_result = False
        # call method of object Patrol Boat
        observed_result = self.patrol_boat.validate_patrol_boat_computer_overlap(config)

        # assert
        self.assertEqual(expected_result, observed_result)
