from utils import Constants
from ship import Ship
from configparser import ConfigParser


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.constants = Constants()

    def validate_destroyer_points(self, battleship_config):
        destroyer_values_player_one = battleship_config.get('main', 'destroyer_player')
        destroyer_axis_player_one = int(destroyer_values_player_one.split(',')[0].strip())
        destroyer_row_player_one = int(destroyer_values_player_one.split(',')[1].strip())
        destroyer_column_player_one = int(destroyer_values_player_one.split(',')[2].strip())

        # check axis
        if destroyer_axis_player_one != self.constants.HORIZONTAL_AXIS and destroyer_axis_player_one != self.constants.VERTICAL_AXIS:
            print("The destroyer axis value is invalid.")
            self.constants.validation_flag_destroyer_player = False

        # check row
        if destroyer_axis_player_one == self.constants.VERTICAL_AXIS:
            if destroyer_row_player_one > 8 or destroyer_row_player_one <= 0 or destroyer_row_player_one % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.constants.validation_flag_destroyer_player = False
        else:
            if destroyer_row_player_one > 10 or destroyer_row_player_one <= 0 or destroyer_row_player_one % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.constants.validation_flag_destroyer_player = False

        # check column
        if destroyer_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if destroyer_column_player_one > 8 or destroyer_column_player_one <= 0 or destroyer_column_player_one % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.constants.validation_flag_destroyer_player = False
        else:
            if destroyer_column_player_one > 10 or destroyer_column_player_one <= 0 or destroyer_column_player_one % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.constants.validation_flag_destroyer_player = False
        return self.constants.validation_flag_destroyer_player

    def ship_sunk_destroyer_player(self):
        hit_counter_player = self.get_hit_counter_player()
        if hit_counter_player[2] == 3:
            self.constants.validation_flag_ship_sunk_destroyer_player = True
            print("computer sunk player's destroyer")
        return self.constants.validation_flag_ship_sunk_destroyer_player
