import unittest
import utils
from unittest.mock import patch
from patrol_boat import Patrol_Boat
from configparser import ConfigParser


class TestPatrol_Boat(unittest.TestCase):
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
