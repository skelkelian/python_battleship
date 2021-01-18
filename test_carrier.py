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

    def test_place_carrier_player_one(self):
        # create an object of class Carrier
        self.carrier = Carrier()
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
        
        # call method of class Carrier

        observed_result = self.carrier.place_carrier_player_one(config)
        self.assertNotEqual(initial_result, observed_result)

    @patch('ship.Ship.get_hit_counter_player', return_value=[5, 1, 2, 0, 0])
    def test_ship_sunk_carrier_player(self, get_hit_counter_player):
        # create an object of class Carrier
        self.carrier = Carrier()
        self.constants = utils.Constants()

        # when
        expected_result = True

        # call method of class Carrier

        observed_result = self.carrier.ship_sunk_carrier_player()

        self.assertEqual(expected_result, observed_result)
