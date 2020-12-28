from unittest import TestCase
import unittest
import utils
from unittest.mock import patch
from carrier import Carrier
from configparser import ConfigParser


class TestCarrier(unittest.TestCase):
    def test_validate_carrier_points(self):
        # create an object of class Carrier
        self.carrier = Carrier()
        self.constants = utils.Constants()

        # creates an object of ConfigParser
        config = ConfigParser()

        # read config file
        config.read('config_easy_difficulty_with_errors.ini')

        # when
        expected_result = False
        # call method of object Carrier
        observed_result = self.carrier.validate_carrier_points(config)

        # assert
        self.assertEqual(expected_result, observed_result)
