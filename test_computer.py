import unittest
import utils
from computer import Computer
from unittest.mock import patch
from configparser import ConfigParser


class TestComputer(unittest.TestCase):
    def test_primary_board_computer(self):
        # given
        expected_primary_board_computer = [
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
        self.computer = Computer(config_name='config_easy_difficulty.ini')

        # assert
        self.assertEqual(expected_primary_board_computer, self.computer.primary_board_computer)

    @patch('computer.Computer.get_primary_board_computer', return_value=[
        [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
        [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    @patch('computer.Computer.pick_point', return_value=(5, 1))
    def test_hit_counter_computer(self, get_primary_board_computer, pick_point):
        # create object of class Computer
        self.computer = Computer()

        # when
        expected_result = True

        # call method of class Computer
        observed_result = self.computer.track_hit_counter_computer()

        self.assertEqual(expected_result, observed_result)

    @patch('computer.Computer.get_primary_board_computer', return_value=[
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    @patch('computer.Computer.pick_point', return_value=(1, 1))
    def test_hit_or_miss_computer(self, get_primary_board_computer, pick_point):
        # create an object of class Computer
        self.computer = Computer()

        # when
        expected_result = True

        # call method of class BattleShip
        observed_result = self.computer.hit_or_miss_computer()

        self.assertEqual(expected_result, observed_result)

    def test_picking_point_computer(self):
        # create an object of class Computer
        self.computer = Computer()

        # when
        lowest_valid_value = 0
        highest_valid_value = 10

        # call method of class BattleShip
        observed_point = self.computer.pick_point()

        # assert
        self.assertTrue(lowest_valid_value < observed_point[0] <= highest_valid_value and
                        lowest_valid_value < observed_point[1] <= highest_valid_value)

    @patch('computer.Computer.get_hit_counter_computer', return_value=[5, 4, 3, 2, 3])
    def test_game_over_computer(self, get_hit_counter_computer):
        # create an object of class Computer
        self.computer = Computer()

        # when
        expected_result = True

        # call method of class Computer
        observed_result = self.computer.game_over_computer()

        self.assertEqual(expected_result, observed_result)
