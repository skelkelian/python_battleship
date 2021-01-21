from utils import Constants
from ship import Ship
from player import Player
from configparser import ConfigParser


class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self.constants = Constants()
        self.player = Player()

    def validate_cruiser_points(self, battleship_config):
        cruiser_values_player_one = battleship_config.get('main', 'cruiser_player')
        cruiser_axis_player_one = int(cruiser_values_player_one.split(',')[0].strip())
        cruiser_row_player_one = int(cruiser_values_player_one.split(',')[1].strip())
        cruiser_column_player_one = int(cruiser_values_player_one.split(',')[2].strip())

        # check axis
        if cruiser_axis_player_one != self.constants.HORIZONTAL_AXIS and cruiser_axis_player_one != self.constants.VERTICAL_AXIS:
            print("The cruiser axis value is invalid.")
            self.constants.validation_flag_cruiser_player = False

        # check row
        if cruiser_axis_player_one == self.constants.VERTICAL_AXIS:
            if cruiser_row_player_one > 7 or cruiser_row_player_one <= 0 or cruiser_row_player_one % 1 != 0:
                print('\nThe cruiser row value is invalid.\n\n')
                self.constants.validation_flag_cruiser_player = False
        else:
            if cruiser_row_player_one > 10 or cruiser_row_player_one <= 0 or cruiser_row_player_one % 1 != 0:
                print('\nThe cruiser row value is invalid.\n\n')
                self.constants.validation_flag_cruiser_player = False

        # check column
        if cruiser_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if cruiser_column_player_one > 7 or cruiser_column_player_one <= 0 or cruiser_column_player_one % 1 != 0:
                print('\nThe cruiser column value is invalid.\n\n')
                self.constants.validation_flag_cruiser_player = False
        else:
            if cruiser_column_player_one > 10 or cruiser_column_player_one <= 0 or cruiser_column_player_one % 1 != 0:
                print('\nThe cruiser column value is invalid.\n\n')
                self.constants.validation_flag_cruiser_player = False
        return self.constants.validation_flag_cruiser_player

    def place_cruiser_player_one(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        cruiser_values_player_one = battleship_config.get('main', 'cruiser_player')
        cruiser_axis_player_one = int(cruiser_values_player_one.split(',')[0].strip())
        cruiser_row_player_one = int(cruiser_values_player_one.split(',')[1].strip())
        cruiser_column_player_one = int(cruiser_values_player_one.split(',')[2].strip())
        if cruiser_axis_player_one == self.constants.HORIZONTAL_AXIS:
            primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one - 1] = self.constants.BATTLESHIP
            primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one] = self.constants.BATTLESHIP
            primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one + 1] = self.constants.BATTLESHIP
            primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one + 2] = self.constants.BATTLESHIP
        else:
            primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one - 1] = self.constants.BATTLESHIP
            primary_board_player_one[cruiser_row_player_one][cruiser_column_player_one - 1] = self.constants.BATTLESHIP
            primary_board_player_one[cruiser_row_player_one + 1][cruiser_column_player_one - 1] = self.constants.BATTLESHIP
            primary_board_player_one[cruiser_row_player_one + 2][cruiser_column_player_one - 1] = self.constants.BATTLESHIP

    def ship_sunk_cruiser_player(self):
        hit_counter_player = self.get_hit_counter_player()
        if hit_counter_player[1] == 4:
            self.constants.validation_flag_ship_sunk_cruiser_player = True
            print("computer sunk player's cruiser")
        return self.constants.validation_flag_ship_sunk_cruiser_player

    def validate_cruiser_overlap(self, battleship_config):
        primary_board_player_one = self.get_primary_board_player_one()
        cruiser_values_player_one = battleship_config.get('main', 'cruiser_player')
        cruiser_axis_player_one = int(cruiser_values_player_one.split(',')[0].strip())
        cruiser_row_player_one = int(cruiser_values_player_one.split(',')[1].strip())
        cruiser_column_player_one = int(cruiser_values_player_one.split(',')[2].strip())

        # check if ship does not overlap
        if cruiser_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one - 1] != 0 or \
                    primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one] != 0 or \
                    primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one + 1] != 0 or \
                    primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one + 2] != 0:
                print('\nThe cruiser overlaps with another ship.\n\n')
                self.constants.validation_flag_cruiser_overlap_player = False
        else:
            if primary_board_player_one[cruiser_row_player_one - 1][cruiser_column_player_one - 1] != 0 or \
                    primary_board_player_one[cruiser_row_player_one][cruiser_column_player_one - 1] != 0 or \
                    primary_board_player_one[cruiser_row_player_one + 1][cruiser_column_player_one - 1] != 0 or \
                    primary_board_player_one[cruiser_row_player_one + 2][cruiser_column_player_one - 1] != 0:
                print('\nThe cruiser overlaps with another ship.\n\n')
                self.constants.validation_flag_cruiser_overlap_player = False
        return self.constants.validation_flag_cruiser_overlap_player