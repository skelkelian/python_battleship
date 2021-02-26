import unittest
import utils
from computer import Computer
from unittest.mock import patch
from configparser import ConfigParser


class TestComputer(unittest.TestCase):
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

