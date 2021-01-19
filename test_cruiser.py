import unittest
import utils
from unittest.mock import patch
from cruiser import Cruiser
from ship import Ship
from configparser import ConfigParser


class TestCruiser(unittest.TestCase):
    def test_validate_cruiser_points(self):
        # create an object of class BattleShip
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

