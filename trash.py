from random import randint
from utils import Constants


class Participant:
    def __init__(self):
        self.board = [0]

    def track_hit_counter_player(self):  # this tracks the computer's hits on the player's ships
        row_selected, column_selected = self.pick_point()
        primary_board_player = self.get_primary_board_player_one()
        if primary_board_player[row_selected - 1][column_selected - 1] == self.constants.CARRIER:
            self.constants.HIT_COUNTER_PLAYER_ONE[0] = self.constants.HIT_COUNTER_PLAYER_ONE[0] + 1
            print("hit carrier")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.BATTLESHIP:
            self.constants.HIT_COUNTER_PLAYER_ONE[1] = self.constants.HIT_COUNTER_PLAYER_ONE[1] + 1
            print("hit battleship")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.DESTROYER:
            self.constants.HIT_COUNTER_PLAYER_ONE[2] = self.constants.HIT_COUNTER_PLAYER_ONE[2] + 1
            print("hit destroyer")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.PATROL_BOAT:
            self.constants.HIT_COUNTER_PLAYER_ONE[3] = self.constants.HIT_COUNTER_PLAYER_ONE[3] + 1
            print("hit patrol boat")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.SUBMARINE:
            self.constants.HIT_COUNTER_PLAYER_ONE[4] = self.constants.HIT_COUNTER_PLAYER_ONE[4] + 1
            print("hit submarine")
        else:
            self.constants.validation_flag_hit_counter_computer = False
            print("missed ships")
        return self.constants.validation_flag_hit_counter_computer

    def pick_point(self):
        row_picked = randint(1, 10)
        column_picked = randint(1, 10)
        return row_picked, column_picked


import unittest
import utils
from player import Player
from computer import Computer
from ship import Ship
from participant import Participant
from unittest.mock import patch
from configparser import ConfigParser


class TestComputer(unittest.TestCase):
    @patch('ship.Ship.get_primary_board_player_one', return_value=[
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
    @patch('computer.Computer.pick_point_computer', return_value=(2, 1))
    def test_hit_counter_computer(self, get_primary_board_player_one, pick_point_computer):
        # create object of class Player
        self.computer = Computer()

        # when
        expected_result = True

        # call method of class BattleShip
        observed_result = self.computer.track_hit_counter_player()

        self.assertEqual(expected_result, observed_result)