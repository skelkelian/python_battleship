import unittest
import utils
from player import Player
from unittest.mock import patch
from configparser import ConfigParser


class TestPlayer(unittest.TestCase):
    def test_primary_board_player_one(self):
        # given
        expected_primary_board_player_one = [
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
        self.assertEqual(expected_primary_board_player_one, self.player.primary_board_player_one)

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

    @patch('player.Player.get_primary_board_player_one', return_value=[
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
    @patch('player.Player.pick_point', return_value=(1, 1))
    def test_hit_or_miss_player(self, get_primary_board_player_one, pick_point):
        # create object of class Player
        self.player = Player()

        # when
        expected_result = True

        # call method of class Player
        observed_result = self.player.hit_or_miss_player()

        self.assertEqual(expected_result, observed_result)

    def test_picking_point_player(self):
        # create object of class Player
        self.player = Player()

        # when
        lowest_valid_value = 0
        highest_valid_value = 10

        # call method of class BattleShip
        observed_point = self.player.pick_point()

        # assert
        self.assertTrue(lowest_valid_value < observed_point[0] <= highest_valid_value and
                        lowest_valid_value < observed_point[1] <= highest_valid_value)

    @patch('player.Player.get_hit_counter_player', return_value=[5, 4, 3, 2, 3])
    def test_game_over_player(self, get_hit_counter_player):
        # create an object of class Player
        self.player = Player()

        # when
        expected_result = True

        # call method of class Player
        observed_result = self.player.game_over_player()

        self.assertEqual(expected_result, observed_result)
