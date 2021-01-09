from utils import Constants
from ship import Ship
from configparser import ConfigParser


class Carrier(Ship):
    def __init__(self):
        super().__init__()
        self.constants = Constants()

    def validate_carrier_points(self, battleship_config):
        carrier_values_player_one = battleship_config.get('main', 'carrier_player')
        carrier_axis_player_one = int(carrier_values_player_one.split(',')[0].strip())
        carrier_row_player_one = int(carrier_values_player_one.split(',')[1].strip())
        carrier_column_player_one = int(carrier_values_player_one.split(',')[2].strip())

        # check axis
        if carrier_axis_player_one != self.constants.HORIZONTAL_AXIS and carrier_axis_player_one != self.constants.VERTICAL_AXIS:
            print("The carrier axis value is invalid.")
            self.constants.validation_flag_carrier_player = False

        # check row
        if carrier_axis_player_one == self.constants.VERTICAL_AXIS:
            if carrier_row_player_one > 6 or carrier_row_player_one <= 0 or carrier_row_player_one % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.constants.validation_flag_carrier_player = False
        else:
            if carrier_row_player_one > 10 or carrier_row_player_one <= 0 or carrier_row_player_one % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.constants.validation_flag_carrier_player = False

        # check column
        if carrier_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if carrier_column_player_one > 6 or carrier_column_player_one <= 0 or carrier_column_player_one % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.constants.validation_flag_carrier_player = False
        else:
            if carrier_column_player_one > 10 or carrier_column_player_one <= 0 or carrier_column_player_one % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.constants.validation_flag_carrier_player = False
        return self.constants.validation_flag_carrier_player

    def place_carrier_player_one(self, battleship_config, primary_board_player_one):
        carrier_values_player_one = battleship_config.get('main', 'carrier_player')
        carrier_axis_player_one = int(carrier_values_player_one.split(',')[0].strip())
        carrier_row_player_one = int(carrier_values_player_one.split(',')[1].strip())
        carrier_column_player_one = int(carrier_values_player_one.split(',')[2].strip())
        if carrier_axis_player_one == self.constants.HORIZONTAL_AXIS:
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one - 1] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one + 1] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one + 2] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one + 3] = self.constants.CARRIER
        else:
            primary_board_player_one[carrier_row_player_one - 1][carrier_column_player_one - 1] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one][carrier_column_player_one - 1] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one + 1][carrier_column_player_one - 1] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one + 2][carrier_column_player_one - 1] = self.constants.CARRIER
            primary_board_player_one[carrier_row_player_one + 3][carrier_column_player_one - 1] = self.constants.CARRIER

    def ship_sunk_carrier_player(self):
        hit_counter_player = self.get_hit_counter_player()
        if hit_counter_player[0] == 5:
            self.constants.validation_flag_ship_sunk_carrier_player = True
            print("computer sunk player's carrier")
        return self.constants.validation_flag_ship_sunk_carrier_player
