import unittest
import utils
from player import Player
from unittest.mock import patch
from configparser import ConfigParser


class TestPlayer(unittest.TestCase):
    def test_player_board_player_one(self):
        # given
        expected_player_board_player_one = [
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
        self.player = Player(config_name='config_easy_difficulty.ini')

        # assert
        self.assertEqual(expected_player_board_player_one, self.player.primary_board_player_one)

    @patch('player.Player.get_primary_board_player_one', return_value=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
        [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
    ])
    @patch('player.Player.pick_point', return_value=(2, 1))
    def test_hit_counter_player(self, get_primary_board_player_one, pick_point):
        # create object of class Player
        self.player = Player()

        # when
        expected_result = True

        # call method of class Player
        observed_result = self.player.track_hit_counter_player()

        self.assertEqual(expected_result, observed_result)
