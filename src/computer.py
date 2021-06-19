from random import randint
import utils
from src.participant import Participant


class Computer(Participant):
    def __init__(self):
        super().__init__()
        self.constants = utils.Constants()
        self.validation_flag_hit_counter_player = self.constants.get_constant_values('validation_flag_hit_counter_player')
        self.validation_flag_hit_or_miss_computer = self.constants.get_constant_values('validation_flag_hit_or_miss_computer')
        self.validation_flag_game_over_computer = self.constants.get_constant_values('validation_flag_game_over_computer')
        self.hit_counter_computer = self.constants.get_constant_values('hit_counter_computer')
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

    def update_primary_board_computer(self, boat_type, boat_values):
        values_computer = boat_values
        axis_computer = int(values_computer.split(',')[0].strip())
        row_computer = int(values_computer.split(',')[1].strip())
        column_computer = int(values_computer.split(',')[2].strip())
        if boat_type == "carrier":
            if axis_computer == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer - 1][column_computer] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer - 1][column_computer + 1] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer - 1][column_computer + 2] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer - 1][column_computer + 3] = self.constants.get_constant_values('carrier')
            else:
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer][column_computer - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer + 1][column_computer - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer + 2][column_computer - 1] = self.constants.get_constant_values('carrier')
                self.primary_board_computer[row_computer + 3][column_computer - 1] = self.constants.get_constant_values('carrier')

        elif boat_type == "cruiser":
            if axis_computer == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('cruiser')
                self.primary_board_computer[row_computer - 1][column_computer] = self.constants.get_constant_values('cruiser')
                self.primary_board_computer[row_computer - 1][column_computer + 1] = self.constants.get_constant_values('cruiser')
                self.primary_board_computer[row_computer - 1][column_computer + 2] = self.constants.get_constant_values('cruiser')
            else:
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('cruiser')
                self.primary_board_computer[row_computer][column_computer - 1] = self.constants.get_constant_values('cruiser')
                self.primary_board_computer[row_computer + 1][column_computer - 1] = self.constants.get_constant_values('cruiser')
                self.primary_board_computer[row_computer + 2][column_computer - 1] = self.constants.get_constant_values('cruiser')

        elif boat_type == "destroyer":
            if axis_computer == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('destroyer')
                self.primary_board_computer[row_computer - 1][column_computer] = self.constants.get_constant_values('destroyer')
                self.primary_board_computer[row_computer - 1][column_computer + 1] = self.constants.get_constant_values('destroyer')
            else:
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('destroyer')
                self.primary_board_computer[row_computer][column_computer - 1] = self.constants.get_constant_values('destroyer')
                self.primary_board_computer[row_computer + 1][column_computer - 1] = self.constants.get_constant_values('destroyer')

        elif boat_type == "patrol_boat":
            if axis_computer == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('patrol_boat')
                self.primary_board_computer[row_computer - 1][column_computer] = self.constants.get_constant_values('patrol_boat')
            else:
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('patrol_boat')
                self.primary_board_computer[row_computer][column_computer - 1] = self.constants.get_constant_values('patrol_boat')

        elif boat_type == "submarine":
            if axis_computer == self.constants.get_constant_values('horizontal_axis'):
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('submarine')
                self.primary_board_computer[row_computer - 1][column_computer] = self.constants.get_constant_values('submarine')
                self.primary_board_computer[row_computer - 1][column_computer + 1] = self.constants.get_constant_values('submarine')
            else:
                self.primary_board_computer[row_computer - 1][column_computer - 1] = self.constants.get_constant_values('submarine')
                self.primary_board_computer[row_computer][column_computer - 1] = self.constants.get_constant_values('submarine')
                self.primary_board_computer[row_computer + 1][column_computer - 1] = self.constants.get_constant_values('submarine')

        else:
            print("boat type is undefined")

    def track_hit_counter_computer(self):  # this tracks the player's hits on the computer's ships
        row_selected, column_selected = self.pick_point()
        primary_board_computer = self.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('carrier'):
            self.hit_counter_computer[0] = self.hit_counter_computer[0] + 1
            print("hit carrier")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('cruiser'):
            self.hit_counter_computer[1] = self.hit_counter_computer[1] + 1
            print("hit battleship")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('destroyer'):
            self.hit_counter_computer[2] = self.hit_counter_computer[2] + 1
            print("hit destroyer")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('patrol_boat'):
            self.hit_counter_computer[3] = self.hit_counter_computer[3] + 1
            print("hit patrol boat")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.get_constant_values('submarine'):
            self.hit_counter_computer[4] = self.hit_counter_computer[4] + 1
            print("hit submarine")
        else:
            self.validation_flag_hit_counter_player = False
            print("missed ships")
        return self.validation_flag_hit_counter_player

    def hit_or_miss_computer(self):  # computer attacking player's ships
        row_selected, column_selected = self.pick_point()
        primary_board_computer = self.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('submarine') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('patrol_boat') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('destroyer') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('cruiser') and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.get_constant_values('carrier'):
            self.validation_flag_hit_or_miss_computer = False
            self.secondary_board_computer[row_selected - 1][column_selected - 1] = -1
        else:
            self.primary_board_computer[row_selected - 1][column_selected - 1] = 9
            self.secondary_board_computer[row_selected - 1][column_selected - 1] = 1
        return self.validation_flag_hit_or_miss_computer

    def update_hit_counter_computer(self):
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[0] == 5:
            self.validation_flag_ship_sunk_carrier_computer = True
            print("player sunk computer's carrier")
        elif hit_counter_computer[1] == 4:
            self.validation_flag_ship_sunk_cruiser_computer = True
            print("player sunk computer's cruiser")
        elif hit_counter_computer[2] == 3:
            self.validation_flag_ship_sunk_destroyer_computer = True
            print("player sunk computer's destroyer")
        elif hit_counter_computer[3] == 2:
            self.validation_flag_ship_sunk_patrol_boat_computer = True
            print("player sunk computer's patrol boat")
        elif hit_counter_computer[4] == 3:
            self.validation_flag_ship_sunk_submarine_computer = True
            print("player sunk computer's submarine")
        else:
            print("No ships were sunk")

    def game_over_computer(self):  # if this triggers, the computer lost
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[0] + hit_counter_computer[1] + hit_counter_computer[2] + \
                hit_counter_computer[3] + hit_counter_computer[4] == 17:
            self.validation_flag_game_over_computer = True
            print('Computer lost, Player wins!')
        return self.validation_flag_game_over_computer
