from utils import Constants
from ship import Ship
from player import Player
from computer import Computer
from configparser import ConfigParser


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.constants = Constants()
        self.validation_flag_destroyer_player = self.constants.get_constant_values('validation_flag_destroyer_player')
        self.validation_flag_destroyer_computer = self.constants.get_constant_values('validation_flag_destroyer_computer')
        self.validation_flag_ship_sunk_destroyer_player = self.constants.get_constant_values('validation_flag_ship_sunk_destroyer_player')
        self.validation_flag_ship_sunk_destroyer_computer = self.constants.get_constant_values('validation_flag_ship_sunk_destroyer_computer')
        self.validation_flag_destroyer_overlap_player = self.constants.get_constant_values('validation_flag_destroyer_overlap_player')
        self.validation_flag_destroyer_overlap_computer = self.constants.get_constant_values('validation_flag_destroyer_overlap_computer')
        self.player = Player()
        self.computer = Computer()

    def validate_destroyer_points(self, battleship_config):
        destroyer_values_player_one = battleship_config.get('main', 'destroyer_player')
        destroyer_axis_player_one = int(destroyer_values_player_one.split(',')[0].strip())
        destroyer_row_player_one = int(destroyer_values_player_one.split(',')[1].strip())
        destroyer_column_player_one = int(destroyer_values_player_one.split(',')[2].strip())

        # check axis
        if destroyer_axis_player_one != self.constants.get_constant_values('horizontal_axis') and destroyer_axis_player_one != self.constants.get_constant_values('vertical_axis'):
            print("The destroyer axis value is invalid.")
            self.validation_flag_destroyer_player = False

        # check row
        if destroyer_axis_player_one == self.constants.get_constant_values('vertical_axis'):
            if destroyer_row_player_one > 8 or destroyer_row_player_one <= 0 or destroyer_row_player_one % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.validation_flag_destroyer_player = False
        else:
            if destroyer_row_player_one > 10 or destroyer_row_player_one <= 0 or destroyer_row_player_one % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.validation_flag_destroyer_player = False

        # check column
        if destroyer_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if destroyer_column_player_one > 8 or destroyer_column_player_one <= 0 or destroyer_column_player_one % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.validation_flag_destroyer_player = False
        else:
            if destroyer_column_player_one > 10 or destroyer_column_player_one <= 0 or destroyer_column_player_one % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.validation_flag_destroyer_player = False
        return self.validation_flag_destroyer_player

    def place_destroyer_player_one(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        destroyer_values_player_one = battleship_config.get('main', 'destroyer_player')
        destroyer_axis_player_one = int(destroyer_values_player_one.split(',')[0].strip())
        destroyer_row_player_one = int(destroyer_values_player_one.split(',')[1].strip())
        destroyer_column_player_one = int(destroyer_values_player_one.split(',')[2].strip())
        if destroyer_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one - 1] = self.constants.get_constant_values('destroyer')
            primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one] = self.constants.get_constant_values('destroyer')
            primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one + 1] = self.constants.get_constant_values('destroyer')
        else:
            primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one - 1] = self.constants.get_constant_values('destroyer')
            primary_board_player_one[destroyer_row_player_one][destroyer_column_player_one - 1] = self.constants.get_constant_values('destroyer')
            primary_board_player_one[destroyer_row_player_one + 1][destroyer_column_player_one - 1] = self.constants.get_constant_values('destroyer')

    def ship_sunk_destroyer_player(self):
        hit_counter_player = self.player.get_hit_counter_player()
        if hit_counter_player[2] == 3:
            self.validation_flag_ship_sunk_destroyer_player = True
            print("computer sunk player's destroyer")
        return self.validation_flag_ship_sunk_destroyer_player

    def validate_destroyer_overlap(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        destroyer_values_player_one = battleship_config.get('main', 'destroyer_player')
        destroyer_axis_player_one = int(destroyer_values_player_one.split(',')[0].strip())
        destroyer_row_player_one = int(destroyer_values_player_one.split(',')[1].strip())
        destroyer_column_player_one = int(destroyer_values_player_one.split(',')[2].strip())

        # check if ship does not overlap
        if destroyer_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one - 1] != 0 or \
                    primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one] != 0 or \
                    primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one + 1] != 0:
                print('\nThe destroyer overlaps with another ship.\n\n')
                self.validation_flag_destroyer_overlap_player = False
        else:
            if primary_board_player_one[destroyer_row_player_one - 1][destroyer_column_player_one - 1] != 0 or \
                    primary_board_player_one[destroyer_row_player_one][destroyer_column_player_one - 1] != 0 or \
                    primary_board_player_one[destroyer_row_player_one + 1][destroyer_column_player_one - 1] != 0:
                print('\nThe destroyer overlaps with another ship.\n\n')
                self.validation_flag_destroyer_overlap_player = False
        return self.validation_flag_destroyer_overlap_player

    def validate_destroyer_computer_points(self, battleship_config):
        destroyer_values_computer = battleship_config.get('main', 'destroyer_computer')
        destroyer_axis_computer = int(destroyer_values_computer.split(',')[0].strip())
        destroyer_row_computer = int(destroyer_values_computer.split(',')[1].strip())
        destroyer_column_computer = int(destroyer_values_computer.split(',')[2].strip())

        # check axis
        if destroyer_axis_computer != self.constants.get_constant_values('horizontal_axis') and destroyer_axis_computer != self.constants.get_constant_values('vertical_axis'):
            print("The destroyer axis value is invalid.")
            self.validation_flag_destroyer_computer = False

        # check row
        if destroyer_axis_computer == self.constants.get_constant_values('vertical_axis'):
            if destroyer_row_computer > 8 or destroyer_row_computer <= 0 or destroyer_row_computer % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.validation_flag_destroyer_computer = False
        else:
            if destroyer_row_computer > 10 or destroyer_row_computer <= 0 or destroyer_row_computer % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.validation_flag_destroyer_computer = False

        # check column
        if destroyer_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if destroyer_column_computer > 8 or destroyer_column_computer <= 0 or destroyer_column_computer % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.validation_flag_destroyer_computer = False
        else:
            if destroyer_column_computer > 10 or destroyer_column_computer <= 0 or destroyer_column_computer % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.validation_flag_destroyer_computer = False
        return self.validation_flag_destroyer_computer

    def place_destroyer_computer(self, battleship_config):
        primary_board_computer = self.computer.get_primary_board_computer()
        destroyer_values_computer = battleship_config.get('main', 'destroyer_computer')
        destroyer_axis_computer = int(destroyer_values_computer.split(',')[0].strip())
        destroyer_row_computer = int(destroyer_values_computer.split(',')[1].strip())
        destroyer_column_computer = int(destroyer_values_computer.split(',')[2].strip())
        if destroyer_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] = self.constants.get_constant_values('destroyer')
            primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer] = self.constants.get_constant_values('destroyer')
            primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer + 1] = self.constants.get_constant_values('destroyer')
        else:
            primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] = self.constants.get_constant_values('destroyer')
            primary_board_computer[destroyer_row_computer][destroyer_column_computer - 1] = self.constants.get_constant_values('destroyer')
            primary_board_computer[destroyer_row_computer + 1][destroyer_column_computer - 1] = self.constants.get_constant_values('destroyer')

    def ship_sunk_destroyer_computer(self):
        hit_counter_computer = self.computer.get_hit_counter_computer()
        if hit_counter_computer[2] == 3:
            self.validation_flag_ship_sunk_destroyer_computer = True
            print("player sunk computer's destroyer")
        return self.validation_flag_ship_sunk_destroyer_computer

    def validate_destroyer_computer_overlap(self, battleship_config):
        primary_board_computer = self.computer.get_primary_board_computer()
        destroyer_values_computer = battleship_config.get('main', 'destroyer_computer')
        destroyer_axis_computer = int(destroyer_values_computer.split(',')[0].strip())
        destroyer_row_computer = int(destroyer_values_computer.split(',')[1].strip())
        destroyer_column_computer = int(destroyer_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if destroyer_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] != 0 or \
                    primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer] != 0 or \
                    primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer + 1] != 0:
                print('\nThe destroyer overlaps with another ship.\n\n')
                self.validation_flag_destroyer_overlap_computer = False
        else:
            if primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] != 0 or \
                    primary_board_computer[destroyer_row_computer][destroyer_column_computer - 1] != 0 or \
                    primary_board_computer[destroyer_row_computer + 1][destroyer_column_computer - 1] != 0:
                print('\nThe destroyer overlaps with another ship.\n\n')
                self.validation_flag_destroyer_overlap_computer = False
        return self.validation_flag_destroyer_overlap_computer
