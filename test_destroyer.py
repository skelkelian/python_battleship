from unittest import TestCase
import unittest
import utils
from unittest.mock import patch
from destroyer import Destroyer
from configparser import ConfigParser


class TestDestroyer(unittest.TestCase):
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