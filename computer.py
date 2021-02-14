from random import randint
from player import Player
from utils import Constants
from ship import Ship


class Computer:
    def __init__(self, config_name=None):
        self.player = Player()
        self.constants = Constants()
        self.ship = Ship()
        self.hit_counter_computer = [0, 0, 0, 0, 0]  # when player hits a ship adjust this hit counter
        self.primary_board_computer = [
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

    def get_hit_counter_computer(self):
        return self.hit_counter_computer

    def track_hit_counter_computer(self):  # this tracks the player's hits on the computer's ships
        row_selected, column_selected = self.player.pick_point_player_one()
        primary_board_computer = self.ship.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.CARRIER:
            self.constants.HIT_COUNTER_COMPUTER[0] = self.constants.HIT_COUNTER_COMPUTER[0] + 1
            print("hit carrier")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.BATTLESHIP:
            self.constants.HIT_COUNTER_COMPUTER[1] = self.constants.HIT_COUNTER_COMPUTER[1] + 1
            print("hit battleship")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.DESTROYER:
            self.constants.HIT_COUNTER_COMPUTER[2] = self.constants.HIT_COUNTER_COMPUTER[2] + 1
            print("hit destroyer")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.PATROL_BOAT:
            self.constants.HIT_COUNTER_COMPUTER[3] = self.constants.HIT_COUNTER_COMPUTER[3] + 1
            print("hit patrol boat")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.SUBMARINE:
            self.constants.HIT_COUNTER_COMPUTER[4] = self.constants.HIT_COUNTER_COMPUTER[4] + 1
            print("hit submarine")
        else:
            self.constants.validation_flag_hit_counter_player = False
            print("missed ships")
        return self.constants.validation_flag_hit_counter_player

    def get_primary_board_computer(self):
        return self.primary_board_computer

    def pick_point_computer(self):
        row_picked_by_computer = randint(1, 10)
        column_picked_by_computer = randint(1, 10)
        return row_picked_by_computer, column_picked_by_computer
