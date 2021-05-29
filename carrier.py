from utils import Constants
from ship import Ship
from player import Player
from computer import Computer
from configparser import ConfigParser


class Carrier(Ship):
    def __init__(self, config_name=None):
        super().__init__()
        self.constants = Constants()
        self.validation_flag_carrier_player = self.constants.get_constant_values('validation_flag_carrier_player')
        self.validation_flag_carrier_computer = self.constants.get_constant_values('validation_flag_carrier_computer')
        self.validation_flag_ship_sunk_carrier_player = self.constants.get_constant_values('validation_flag_ship_sunk_carrier_player')
        self.validation_flag_ship_sunk_carrier_computer = self.constants.get_constant_values('validation_flag_ship_sunk_carrier_computer')
        self.player = Player()
        self.computer = Computer()

        # if there is a config file, take values from there
        # if not, set the values to default
        if config_name is not None:
            # creates an object of ConfigParser
            config_parser = ConfigParser()

            # read config file
            config_parser.read(config_name)

            self.battleship_config = config_parser

    def get_carrier_values_player_one(self):
        carrier_values_player_one = self.battleship_config.get('main', 'carrier_player')
        return carrier_values_player_one

    def validate_carrier_points(self):
        carrier_values_player_one = self.battleship_config.get('main', 'carrier_player')
        carrier_axis_player_one = int(carrier_values_player_one.split(',')[0].strip())
        carrier_row_player_one = int(carrier_values_player_one.split(',')[1].strip())
        carrier_column_player_one = int(carrier_values_player_one.split(',')[2].strip())

        # check axis
        if carrier_axis_player_one != self.constants.get_constant_values('horizontal_axis') and carrier_axis_player_one != self.constants.get_constant_values('vertical_axis'):
            print("The carrier axis value is invalid.")
            self.validation_flag_carrier_player = False

        # check row
        if carrier_axis_player_one == self.constants.get_constant_values('vertical_axis'):
            if carrier_row_player_one > 6 or carrier_row_player_one <= 0 or carrier_row_player_one % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.validation_flag_carrier_player = False
        else:
            if carrier_row_player_one > 10 or carrier_row_player_one <= 0 or carrier_row_player_one % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.validation_flag_carrier_player = False

        # check column
        if carrier_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if carrier_column_player_one > 6 or carrier_column_player_one <= 0 or carrier_column_player_one % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.validation_flag_carrier_player = False
        else:
            if carrier_column_player_one > 10 or carrier_column_player_one <= 0 or carrier_column_player_one % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.validation_flag_carrier_player = False
        return self.validation_flag_carrier_player

    def place_carrier_player_one(self):
        primary_board_player_one = self.player.get_primary_board_player_one()
        carrier_values_player_one = self.battleship_config.get('main', 'carrier_player')
        carrier_axis_player_one = int(carrier_values_player_one.split(',')[0].strip())
        carrier_row_player_one = int(carrier_values_player_one.split(',')[1].strip())
        carrier_column_player_one = int(carrier_values_player_one.split(',')[2].strip())
        if carrier_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one - 1] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one + 1] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one + 2] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one + 3] = self.constants.get_constant_values('carrier')
        else:
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one - 1] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one][carrier_column_player_one - 1] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one + 1][carrier_column_player_one - 1] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one + 2][carrier_column_player_one - 1] = self.constants.get_constant_values('carrier')
            primary_board_player_one[carrier_row_player_one + 3][carrier_column_player_one - 1] = self.constants.get_constant_values('carrier')
        return primary_board_player_one

    def ship_sunk_carrier_player(self):
        hit_counter_player = self.player.get_hit_counter_player()
        if hit_counter_player[0] == 5:
            self.validation_flag_ship_sunk_carrier_player = True
            print("computer sunk player's carrier")
        return self.validation_flag_ship_sunk_carrier_player

    def validate_carrier_computer_points(self):
        carrier_values_computer = self.battleship_config.get('main', 'carrier_computer')
        carrier_axis_computer = int(carrier_values_computer.split(',')[0].strip())
        carrier_row_computer = int(carrier_values_computer.split(',')[1].strip())
        carrier_column_computer = int(carrier_values_computer.split(',')[2].strip())

        # check axis
        if carrier_axis_computer != self.constants.get_constant_values('horizontal_axis') and carrier_axis_computer != self.constants.get_constant_values('vertical_axis'):
            print("The carrier axis value is invalid.")
            self.validation_flag_carrier_computer = False

        # check row
        if carrier_axis_computer == self.constants.get_constant_values('vertical_axis'):
            if carrier_row_computer > 6 or carrier_row_computer <= 0 or carrier_row_computer % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.validation_flag_carrier_computer = False
        else:
            if carrier_row_computer > 10 or carrier_row_computer <= 0 or carrier_row_computer % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.validation_flag_carrier_computer = False

        # check column
        if carrier_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if carrier_column_computer > 6 or carrier_column_computer <= 0 or carrier_column_computer % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.validation_flag_carrier_computer = False
        else:
            if carrier_column_computer > 10 or carrier_column_computer <= 0 or carrier_column_computer % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.validation_flag_carrier_computer = False
        return self.validation_flag_carrier_computer

    def place_carrier_computer(self):
        primary_board_computer = self.computer.get_primary_board_computer()
        carrier_values_computer = self.battleship_config.get('main', 'carrier_computer')
        carrier_axis_computer = int(carrier_values_computer.split(',')[0].strip())
        carrier_row_computer = int(carrier_values_computer.split(',')[1].strip())
        carrier_column_computer = int(carrier_values_computer.split(',')[2].strip())
        if carrier_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            primary_board_computer[carrier_row_computer - 1][carrier_column_computer - 1] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer - 1][carrier_column_computer] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer - 1][carrier_column_computer + 1] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer - 1][carrier_column_computer + 2] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer - 1][carrier_column_computer + 3] = self.constants.get_constant_values('carrier')
        else:
            primary_board_computer[carrier_row_computer - 1][carrier_column_computer - 1] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer][carrier_column_computer - 1] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer + 1][carrier_column_computer - 1] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer + 2][carrier_column_computer - 1] = self.constants.get_constant_values('carrier')
            primary_board_computer[carrier_row_computer + 3][carrier_column_computer - 1] = self.constants.get_constant_values('carrier')

    def ship_sunk_carrier_computer(self):
        hit_counter_computer = self.computer.get_hit_counter_computer()
        if hit_counter_computer[0] == 5:
            self.validation_flag_ship_sunk_carrier_computer = True
            print("player sunk computer's carrier")
        return self.validation_flag_ship_sunk_carrier_computer
