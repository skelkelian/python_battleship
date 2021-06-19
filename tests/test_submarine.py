import unittest
import utils
from unittest.mock import patch
from src.submarine import Submarine


class TestSubmarine(unittest.TestCase):
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

    def test_validate_submarine_points(self):
        # create an object of class Submarine
        self.submarine = Submarine('../config/config_easy_difficulty_with_errors.ini')
        self.constants = utils.Constants()

        # when
        expected_result = False
        # call method of object Submarine
        observed_result = self.submarine.validate_submarine_points()

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_submarine_player_one(self):
        # create an object of class Submarine
        self.submarine = Submarine('../config/config_easy_difficulty.ini')
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

        # call method of class Submarine
        observed_result = self.submarine.place_submarine_player_one()

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('src.player.Player.get_hit_counter_player', return_value=[2, 3, 1, 1, 3])
    def test_ship_sunk_submarine_player(self, get_hit_counter_player):
        # create an object of class Submarine
        self.submarine = Submarine()
        self.constants = utils.Constants()

        # when
        expected_result = True
        # call method of class Submarine
        observed_result = self.submarine.ship_sunk_submarine_player()

        self.assertEqual(expected_result, observed_result)

    @patch('src.player.Player.get_primary_board_player_one', return_value=mocked_primary_board)
    def test_validate_submarine_overlap(self, get_primary_board_player_one):
        # create an object of class Submarine
        self.submarine = Submarine('../config/config_easy_ship_overlap.ini')
        self.constants = utils.Constants()

        # when
        expected_result = False
        # call method of object Submarine
        observed_result = self.submarine.validate_submarine_overlap()

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_validate_submarine_computer_points(self):
        # create an object of class Submarine
        self.submarine = Submarine('../config/config_easy_difficulty_with_errors.ini')
        self.constants = utils.Constants()

        # when
        expected_result = False
        # call method of object Submarine
        observed_result = self.submarine.validate_submarine_computer_points()

        # assert
        self.assertEqual(expected_result, observed_result)

    def test_place_submarine_computer(self):
        # create an object of class Submarine
        self.submarine = Submarine('../config/config_easy_difficulty.ini')
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

        # call method of class Submarine
        observed_result = self.submarine.place_submarine_computer()

        # assert
        self.assertNotEqual(initial_result, observed_result)

    @patch('src.computer.Computer.get_hit_counter_computer', return_value=[2, 3, 1, 1, 3])
    def test_ship_sunk_submarine_computer(self, get_hit_counter_computer):
        # create an object of class Submarine
        self.submarine = Submarine()
        self.constants = utils.Constants()

        # when
        expected_result = True
        # call method of class Submarine
        observed_result = self.submarine.ship_sunk_submarine_computer()

        self.assertEqual(expected_result, observed_result)

    @patch('src.computer.Computer.get_primary_board_computer', return_value=mocked_primary_board_computer)
    def test_validate_submarine_computer_overlap(self, get_primary_board_computer):
        # create an object of class Submarine
        self.submarine = Submarine('../config/config_easy_ship_overlap.ini')
        self.constants = utils.Constants()

        # when
        expected_result = False
        # call method of object Submarine
        observed_result = self.submarine.validate_submarine_computer_overlap()

        # assert
        self.assertEqual(expected_result, observed_result)
