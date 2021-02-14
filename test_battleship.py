from unittest import TestCase
import unittest
import utils
from BattleShip import BattleShip
from unittest.mock import patch
from configparser import ConfigParser


class TestBattleShip(unittest.TestCase):

    def test_player_board_one(self):
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
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')

        # assert
        self.assertEqual(expected_player_board_player_one, self.battleship.ship.primary_board_player_one)

    def test_read_computer_opponent_type_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
        self.constants = utils.Constants()

        # when
        expected_opponent_type = self.constants.COMPUTER_OPPONENT
        # call method of object BattleShip
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(expected_opponent_type, observed_opponent_type)

    def test_read_game_difficulty_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
        self.constants = utils.Constants()

        # when
        expected_game_difficulty = self.constants.EASY_DIFFICULTY
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

    def test_read_value_without_config_file(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()
        self.constants = utils.Constants()

        # when
        expected_game_difficulty = self.constants.EASY_DIFFICULTY
        expected_opponent_type = self.constants.COMPUTER_OPPONENT
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.get_game_difficulty()
        observed_opponent_type = self.battleship.get_opponent_type()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)
        self.assertEqual(expected_opponent_type, observed_opponent_type)

# validate

    def test_validate_game_difficulty(self):
        # create an object of class BattleShip
        self.battleship = BattleShip(config_name='config_easy_difficulty_with_errors.ini')

        # when
        expected_game_difficulty = False
        # call method of object BattleShip
        observed_game_difficulty = self.battleship.validate_game_difficulty()

        # assert
        self.assertEqual(expected_game_difficulty, observed_game_difficulty)

# offense
    def test_picking_point_player(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        lowest_valid_value = 0
        highest_valid_value = 10

        # call method of class BattleShip
        observed_point = self.battleship.player.pick_point_player_one()

        # assert
        self.assertTrue(lowest_valid_value < observed_point[0] <= highest_valid_value and
                        lowest_valid_value < observed_point[1] <= highest_valid_value)

    def test_picking_point_computer(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        lowest_valid_value = 0
        highest_valid_value = 10

        # call method of class BattleShip
        observed_point = self.battleship.computer.pick_point_computer()

        # assert
        self.assertTrue(lowest_valid_value < observed_point[0] <= highest_valid_value and
                        lowest_valid_value < observed_point[1] <= highest_valid_value)

    def test_place_point_primary_player(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_primary_board = [
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

        # call method of class BattleShip
        observed_primary_board = self.battleship.place_point_on_primary_player()

        self.assertNotEqual(expected_primary_board, observed_primary_board)

    def test_place_point_secondary_player(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_secondary_board = [
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

        # call method of class BattleShip
        observed_secondary_board = self.battleship.place_point_on_secondary_player()

        self.assertNotEqual(expected_secondary_board, observed_secondary_board)

    def test_place_point_primary_computer(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_primary_board = [
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

        # call method of class BattleShip
        observed_primary_board = self.battleship.place_point_on_primary_computer()

        self.assertNotEqual(expected_primary_board, observed_primary_board)

    def test_place_point_secondary_computer(self):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_secondary_board = [
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

        # call method of class BattleShip
        observed_secondary_board = self.battleship.place_point_on_secondary_computer()

        self.assertNotEqual(expected_secondary_board, observed_secondary_board)

    @patch('ship.Ship.get_primary_board_computer', return_value=[
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
    @patch('player.Player.pick_point_player_one', return_value=(1, 1))
    def test_hit_or_miss_player(self, get_primary_board_player_one, pick_point_player_one):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_result = True

        # call method of class BattleShip
        observed_result = self.battleship.hit_or_miss_player()

        self.assertEqual(expected_result, observed_result)

    @patch('ship.Ship.get_primary_board_player_one', return_value=[
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
    @patch('computer.Computer.pick_point_computer', return_value=(1, 4))
    def test_hit_or_miss_computer(self, get_primary_board_player_one, pick_point_computer):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_result = True

        # call method of class BattleShip
        observed_result = self.battleship.hit_or_miss_computer()

        self.assertEqual(expected_result, observed_result)

    @patch('ship.Ship.get_primary_board_computer', return_value=[
        [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    @patch('player.Player.pick_point_player_one', return_value=(5, 1))
    def test_hit_counter_player(self, get_primary_board_computer, pick_point_player_one):
        # create an object of class BattleShip
        self.battleship = BattleShip()

        # when
        expected_result = True

        # call method of class BattleShip
        observed_result = self.battleship.computer.track_hit_counter_computer()

        self.assertEqual(expected_result, observed_result)

#     @patch('BattleShip.BattleShip.get_primary_board_player_one', return_value=[
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
#         [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
#     ])
#     @patch('BattleShip.BattleShip.pick_point_computer', return_value=(2, 1))
#     def test_hit_counter_computer(self, get_primary_board_player_one, pick_point_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.hit_counter_player()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_player', return_value=[2, 4, 2, 0, 0])
#     def test_ship_sunk_battleship_player(self, get_hit_counter_player):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.ship_sunk_battleship_player()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_computer', return_value=[5, 1, 2, 0, 0])
#     def test_ship_sunk_carrier_computer(self, get_hit_counter_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.ship_sunk_carrier_computer()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_computer', return_value=[2, 4, 2, 0, 0])
#     def test_ship_sunk_battleship_computer(self, get_hit_counter_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.ship_sunk_battleship_computer()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_computer', return_value=[2, 3, 3, 0, 0])
#     def test_ship_sunk_destroyer_computer(self, get_hit_counter_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.ship_sunk_destroyer_computer()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_computer', return_value=[2, 3, 1, 2, 0])
#     def test_ship_sunk_patrol_boat_computer(self, get_hit_counter_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.ship_sunk_patrol_boat_computer()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_computer', return_value=[2, 3, 1, 1, 3])
#     def test_ship_sunk_submarine_computer(self, get_hit_counter_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.ship_sunk_submarine_computer()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_player', return_value=[5, 4, 3, 2, 3])
#     def test_game_over_player(self, get_hit_counter_player):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.game_over_player()
#
#         self.assertEqual(expected_result, observed_result)
#
#     @patch('BattleShip.BattleShip.get_hit_counter_computer', return_value=[5, 4, 3, 2, 3])
#     def test_game_over_computer(self, get_hit_counter_computer):
#         # create an object of class BattleShip
#         self.battleship = BattleShip()
#
#         # when
#         expected_result = True
#
#         # call method of class BattleShip
#         observed_result = self.battleship.game_over_computer()
#
#         self.assertEqual(expected_result, observed_result)
#
# start game
#
#     def test_start_game(self):
#         # given
#         # create an object of class BattleShip
#         self.battleship = BattleShip(config_name='config_easy_difficulty.ini')
#
#         # when
#         expected_primary_board_player_one = [
#             [0, 0, 0, 0, 0, 0, 0, 3, 3, 3],
#             [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
#             [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [4, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#             [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         ]
#
#         expected_primary_board_computer = [
#             [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
#             [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],
#             [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
#             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         ]
#         # call method of object BattleShip
#         self.battleship.start_game()
#         observed_primary_board_player_one = self.battleship.ship.get_primary_board_player_one()
#         observed_primary_board_computer = self.battleship.ship.get_primary_board_computer()
#
#         # assert
#         self.assertEqual(expected_primary_board_player_one, observed_primary_board_player_one)
#         self.assertEqual(expected_primary_board_computer, observed_primary_board_computer)
