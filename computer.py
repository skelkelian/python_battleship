from random import randint
from participant import Participant


class Computer(Participant):
    def __init__(self, config_name=None):
        super().__init__()
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
        self.secondary_board_computer = [
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

    def get_primary_board_computer(self):
        return self.primary_board_computer

    def track_hit_counter_computer(self):  # this tracks the player's hits on the computer's ships
        row_selected, column_selected = self.pick_point()
        primary_board_computer = self.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('carrier'):
            self.constants.HIT_COUNTER_COMPUTER[0] = self.constants.HIT_COUNTER_COMPUTER[0] + 1
            print("hit carrier")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('cruiser'):
            self.constants.HIT_COUNTER_COMPUTER[1] = self.constants.HIT_COUNTER_COMPUTER[1] + 1
            print("hit battleship")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('destroyer'):
            self.constants.HIT_COUNTER_COMPUTER[2] = self.constants.HIT_COUNTER_COMPUTER[2] + 1
            print("hit destroyer")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('patrol_boat'):
            self.constants.HIT_COUNTER_COMPUTER[3] = self.constants.HIT_COUNTER_COMPUTER[3] + 1
            print("hit patrol boat")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('submarine'):
            self.constants.HIT_COUNTER_COMPUTER[4] = self.constants.HIT_COUNTER_COMPUTER[4] + 1
            print("hit submarine")
        else:
            self.constants.validation_flag_hit_counter_player = False
            print("missed ships")
        return self.constants.validation_flag_hit_counter_player

    def hit_or_miss_computer(self):  # computer attacking player's ships
        row_selected, column_selected = self.pick_point()
        primary_board_computer = self.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('submarine') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('patrol_boat') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('destroyer') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('cruiser') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('carrier'):
            self.constants.validation_flag_hit_or_miss_computer = False
            self.secondary_board_computer[row_selected - 1][column_selected - 1] = -1
        else:
            self.primary_board_computer[row_selected - 1][column_selected - 1] = 9
            self.secondary_board_computer[row_selected - 1][column_selected - 1] = 1
        return self.constants.validation_flag_hit_or_miss_computer

    def game_over_computer(self):  # if this triggers, the computer lost
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[0] + hit_counter_computer[1] + hit_counter_computer[2] + \
                hit_counter_computer[3] + hit_counter_computer[4] == 17:
            self.constants.validation_flag_game_over_computer = True
        return self.constants.validation_flag_game_over_computer
