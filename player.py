from random import randint
import utils
from participant import Participant


class Player(Participant):
    def __init__(self, config_name=None):
        super().__init__()
        self.constants = utils.Constants()
        self.validation_flag_hit_or_miss_player = self.constants.get_constant_values('validation_flag_hit_or_miss_player')
        self.validation_flag_game_over_player = self.constants.get_constant_values('validation_flag_game_over_player')
        self.validation_flag_hit_counter_computer = self.constants.get_constant_values('validation_flag_hit_counter_computer')
        self.hit_counter_player_one = self.constants.get_constant_values('hit_counter_player_one')
        self.primary_board_player_one = [
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
        self.secondary_board_player_one = [
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

    def get_hit_counter_player(self):
        return self.hit_counter_player_one

    def get_primary_board_player_one(self):
        return self.primary_board_player_one

    def update_primary_board_player_one(self, boat_type, boat_values):
        values_player_one = boat_values
        axis_player_one = int(values_player_one.split(',')[0].strip())
        row_player_one = int(values_player_one.split(',')[1].strip())
        column_player_one = int(values_player_one.split(',')[2].strip())
        if boat_type == "carrier":
            if axis_player_one == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_player_one[row_player_one - 1][column_player_one - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one - 1][column_player_one] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one - 1][column_player_one + 1] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one - 1][column_player_one + 2] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one - 1][column_player_one + 3] = self.constants.get_constant_values('carrier')
            else:
                self.primary_board_player_one[row_player_one - 1][column_player_one - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one][column_player_one - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one + 1][column_player_one - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one + 2][column_player_one - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_player_one[row_player_one + 3][column_player_one - 1] = self.constants.get_constant_values('carrier')

        elif boat_type == "destroyer":
            if axis_player_one == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_player_one[row_player_one - 1][column_player_one - 1] = self.constants.get_constant_values('destroyer')
                self.primary_board_player_one[row_player_one - 1][column_player_one] = self.constants.get_constant_values('destroyer')
                self.primary_board_player_one[row_player_one - 1][column_player_one + 1] = self.constants.get_constant_values('destroyer')
            else:
                self.primary_board_player_one[row_player_one - 1][column_player_one - 1] = self.constants.get_constant_values('destroyer')
                self.primary_board_player_one[row_player_one][column_player_one - 1] = self.constants.get_constant_values('destroyer')
                self.primary_board_player_one[row_player_one + 1][column_player_one - 1] = self.constants.get_constant_values('destroyer')

        elif boat_type == "patrol_boat":
            if axis_player_one == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_player_one[row_player_one - 1][
                    column_player_one - 1] = self.constants.get_constant_values('patrol_boat')
                self.primary_board_player_one[row_player_one - 1][
                    column_player_one] = self.constants.get_constant_values('patrol_boat')
            else:
                self.primary_board_player_one[row_player_one - 1][
                    column_player_one - 1] = self.constants.get_constant_values('patrol_boat')
                self.primary_board_player_one[row_player_one][
                    column_player_one - 1] = self.constants.get_constant_values('patrol_boat')

        else:
            print("boat type is undefined")

    def track_hit_counter_player(self):  # this tracks the computer's hits on the player's ships
        row_selected, column_selected = self.pick_point()
        primary_board_player = self.get_primary_board_player_one()
        if primary_board_player[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('carrier'):
            self.hit_counter_player_one[0] = self.hit_counter_player_one[0] + 1
            print("hit carrier")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('cruiser'):
            self.hit_counter_player_one[1] = self.hit_counter_player_one[1] + 1
            print("hit cruiser")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('destroyer'):
            self.hit_counter_player_one[2] = self.hit_counter_player_one[2] + 1
            print("hit destroyer")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('patrol_boat'):
            self.hit_counter_player_one[3] = self.hit_counter_player_one[3] + 1
            print("hit patrol boat")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('submarine'):
            self.hit_counter_player_one[4] = self.hit_counter_player_one[4] + 1
            print("hit submarine")
        else:
            self.validation_flag_hit_counter_computer = False
            print("missed ships")
        return self.validation_flag_hit_counter_computer

    def hit_or_miss_player(self):  # player attacking computer's ships
        row_selected, column_selected = self.pick_point()
        primary_board_player_one = self.get_primary_board_player_one()
        if primary_board_player_one[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('submarine') and \
                primary_board_player_one[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('patrol_boat') and \
                primary_board_player_one[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('destroyer') and \
                primary_board_player_one[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('cruiser') and \
                primary_board_player_one[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('carrier'):
            self.validation_flag_hit_or_miss_player = False
            self.secondary_board_player_one[row_selected - 1][column_selected - 1] = -1
        else:
            self.primary_board_player_one[row_selected - 1][column_selected - 1] = 9
            self.secondary_board_player_one[row_selected - 1][column_selected - 1] = 1
        return self.validation_flag_hit_or_miss_player

    def game_over_player(self):  # if this triggers, the player lost
        hit_counter_player = self.get_hit_counter_player()
        if hit_counter_player[0] + hit_counter_player[1] + hit_counter_player[2] + \
                hit_counter_player[3] + hit_counter_player[4] == 17:
            self.validation_flag_game_over_player = True
        return self.validation_flag_game_over_player
