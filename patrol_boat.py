from utils import Constants
from ship import Ship
from player import Player
from computer import Computer
from configparser import ConfigParser


class Patrol_Boat(Ship):
    def __init__(self):
        super().__init__()
        self.constants = Constants()
        self.validation_flag_patrol_boat_player = self.constants.get_constant_values('validation_flag_patrol_boat_player')
        self.validation_flag_patrol_boat_computer = self.constants.get_constant_values('validation_flag_patrol_boat_computer')
        self.validation_flag_ship_sunk_patrol_boat_player = self.constants.get_constant_values('validation_flag_ship_sunk_patrol_boat_player')
        self.validation_flag_patrol_boat_overlap_player = self.constants.get_constant_values('validation_flag_patrol_boat_overlap_player')
        self.player = Player()
        self.computer = Computer()

    def validate_patrol_boat_points(self, battleship_config):
        patrol_boat_values_player_one = battleship_config.get('main', 'patrol_boat_player')
        patrol_boat_axis_player_one = int(patrol_boat_values_player_one.split(',')[0].strip())
        patrol_boat_row_player_one = int(patrol_boat_values_player_one.split(',')[1].strip())
        patrol_boat_column_player_one = int(patrol_boat_values_player_one.split(',')[2].strip())

        # check axis
        if patrol_boat_axis_player_one != self.constants.get_constant_values('horizontal_axis') and patrol_boat_axis_player_one != self.constants.get_constant_values('vertical_axis'):
            print("The patrol boat axis value is invalid.")
            self.validation_flag_patrol_boat_player = False

        # check row
        if patrol_boat_axis_player_one == self.constants.get_constant_values('vertical_axis'):
            if patrol_boat_row_player_one > 9 or patrol_boat_row_player_one <= 0 or patrol_boat_row_player_one % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.validation_flag_patrol_boat_player = False
        else:
            if patrol_boat_row_player_one > 10 or patrol_boat_row_player_one <= 0 or patrol_boat_row_player_one % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.validation_flag_patrol_boat_player = False

        # check column
        if patrol_boat_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if patrol_boat_column_player_one > 9 or patrol_boat_column_player_one <= 0 or patrol_boat_column_player_one % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.validation_flag_patrol_boat_player = False
        else:
            if patrol_boat_column_player_one > 10 or patrol_boat_column_player_one <= 0 or patrol_boat_column_player_one % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.validation_flag_patrol_boat_player = False
        return self.validation_flag_patrol_boat_player

    def place_patrol_boat_player_one(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        patrol_boat_values_player_one = battleship_config.get('main', 'patrol_boat_player')
        patrol_boat_axis_player_one = int(patrol_boat_values_player_one.split(',')[0].strip())
        patrol_boat_row_player_one = int(patrol_boat_values_player_one.split(',')[1].strip())
        patrol_boat_column_player_one = int(patrol_boat_values_player_one.split(',')[2].strip())
        if patrol_boat_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            primary_board_player_one[patrol_boat_row_player_one - 1][patrol_boat_column_player_one - 1] = self.constants.get_constant_values('patrol_boat')
            primary_board_player_one[patrol_boat_row_player_one - 1][patrol_boat_column_player_one] = self.constants.get_constant_values('patrol_boat')
        else:
            primary_board_player_one[patrol_boat_row_player_one - 1][patrol_boat_column_player_one - 1] = self.constants.get_constant_values('patrol_boat')
            primary_board_player_one[patrol_boat_row_player_one][patrol_boat_column_player_one - 1] = self.constants.get_constant_values('patrol_boat')

    def ship_sunk_patrol_boat_player(self):
        hit_counter_player = self.player.get_hit_counter_player()
        if hit_counter_player[3] == 2:
            self.validation_flag_ship_sunk_patrol_boat_player = True
            print("computer sunk player's patrol boat")
        return self.validation_flag_ship_sunk_patrol_boat_player

    def validate_patrol_boat_overlap(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        patrol_boat_values_player_one = battleship_config.get('main', 'patrol_boat_player')
        patrol_boat_axis_player_one = int(patrol_boat_values_player_one.split(',')[0].strip())
        patrol_boat_row_player_one = int(patrol_boat_values_player_one.split(',')[1].strip())
        patrol_boat_column_player_one = int(patrol_boat_values_player_one.split(',')[2].strip())

        # check if ship does not overlap
        if patrol_boat_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if primary_board_player_one[patrol_boat_row_player_one - 1][patrol_boat_column_player_one - 1] != 0 or \
                    primary_board_player_one[patrol_boat_row_player_one - 1][patrol_boat_column_player_one] != 0:
                print('\nThe patrol boat overlaps with another ship.\n\n')
                self.validation_flag_patrol_boat_overlap_player = False
        else:
            if primary_board_player_one[patrol_boat_row_player_one - 1][patrol_boat_column_player_one - 1] != 0 or \
                    primary_board_player_one[patrol_boat_row_player_one][patrol_boat_column_player_one - 1] != 0:
                print('\nThe patrol boat overlaps with another ship.\n\n')
                self.validation_flag_patrol_boat_overlap_player = False
        return self.validation_flag_patrol_boat_overlap_player

    def validate_patrol_boat_computer_points(self, battleship_config):
        patrol_boat_values_computer = battleship_config.get('main', 'patrol_boat_computer')
        patrol_boat_axis_computer = int(patrol_boat_values_computer.split(',')[0].strip())
        patrol_boat_row_computer = int(patrol_boat_values_computer.split(',')[1].strip())
        patrol_boat_column_computer = int(patrol_boat_values_computer.split(',')[2].strip())

        # check axis
        if patrol_boat_axis_computer != self.constants.get_constant_values('horizontal_axis') and patrol_boat_axis_computer != self.constants.get_constant_values('vertical_axis'):
            print("The patrol boat axis value is invalid.")
            self.validation_flag_patrol_boat_computer = False

        # check row
        if patrol_boat_axis_computer == self.constants.get_constant_values('vertical_axis'):
            if patrol_boat_row_computer > 9 or patrol_boat_row_computer <= 0 or patrol_boat_row_computer % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.validation_flag_patrol_boat_computer = False
        else:
            if patrol_boat_row_computer > 10 or patrol_boat_row_computer <= 0 or patrol_boat_row_computer % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.validation_flag_patrol_boat_computer = False

        # check column
        if patrol_boat_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if patrol_boat_column_computer > 9 or patrol_boat_column_computer <= 0 or patrol_boat_column_computer % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.validation_flag_patrol_boat_computer = False
        else:
            if patrol_boat_column_computer > 10 or patrol_boat_column_computer <= 0 or patrol_boat_column_computer % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.validation_flag_patrol_boat_computer = False
        return self.validation_flag_patrol_boat_computer

    def place_patrol_boat_computer(self, battleship_config):
        primary_board_computer = self.computer.get_primary_board_computer()
        patrol_boat_values_computer = battleship_config.get('main', 'patrol_boat_computer')
        patrol_boat_axis_computer = int(patrol_boat_values_computer.split(',')[0].strip())
        patrol_boat_row_computer = int(patrol_boat_values_computer.split(',')[1].strip())
        patrol_boat_column_computer = int(patrol_boat_values_computer.split(',')[2].strip())
        if patrol_boat_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] = self.constants.get_constant_values('patrol_boat')
            primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer] = self.constants.get_constant_values('patrol_boat')
        else:
            primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] = self.constants.get_constant_values('patrol_boat')
            primary_board_computer[patrol_boat_row_computer][patrol_boat_column_computer - 1] = self.constants.get_constant_values('patrol_boat')

    def ship_sunk_patrol_boat_computer(self):
        hit_counter_computer = self.computer.get_hit_counter_computer()
        if hit_counter_computer[3] == 2:
            self.constants.validation_flag_ship_sunk_patrol_boat_computer = True
            print("player sunk computer's patrol boat")
        return self.constants.validation_flag_ship_sunk_patrol_boat_computer

    def validate_patrol_boat_computer_overlap(self, battleship_config):
        primary_board_computer = self.computer.get_primary_board_computer()
        patrol_boat_values_computer = battleship_config.get('main', 'patrol_boat_computer')
        patrol_boat_axis_computer = int(patrol_boat_values_computer.split(',')[0].strip())
        patrol_boat_row_computer = int(patrol_boat_values_computer.split(',')[1].strip())
        patrol_boat_column_computer = int(patrol_boat_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if patrol_boat_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] != 0 or \
                    primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer] != 0:
                print('\nThe patrol boat overlaps with another ship.\n\n')
                self.constants.validation_flag_patrol_boat_overlap_computer = False
        else:
            if primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] != 0 or \
                    primary_board_computer[patrol_boat_row_computer][patrol_boat_column_computer - 1] != 0:
                print('\nThe patrol boat overlaps with another ship.\n\n')
                self.constants.validation_flag_patrol_boat_overlap_computer = False
        return self.constants.validation_flag_patrol_boat_overlap_computer
