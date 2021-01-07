import unittest
import utils
from unittest.mock import patch
from submarine import Submarine
from configparser import ConfigParser


class TestSubmarine(unittest.TestCase):
    def test_validate_submarine_points(self):
        # create an object of class Carrier
        self.submarine = Submarine()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object Submarine
        observed_result = self.submarine.validate_submarine_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)
