from utils import Constants


class Submarine:
    def __init__(self):
        self.constants = Constants()

    def validate_submarine_points(self, battleship_config):
        submarine_values_player_one = battleship_config.get('main', 'submarine_player')
        submarine_axis_player_one = int(submarine_values_player_one.split(',')[0].strip())
        submarine_row_player_one = int(submarine_values_player_one.split(',')[1].strip())
        submarine_column_player_one = int(submarine_values_player_one.split(',')[2].strip())

        # check axis
        if submarine_axis_player_one != self.constants.HORIZONTAL_AXIS and submarine_axis_player_one != self.constants.VERTICAL_AXIS:
            print("The submarine axis value is invalid.")
            self.constants.validation_flag_submarine_player = False

        # check row
        if submarine_axis_player_one == self.constants.VERTICAL_AXIS:
            if submarine_row_player_one > 8 or submarine_row_player_one <= 0 or submarine_row_player_one % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.constants.validation_flag_submarine_player = False
        else:
            if submarine_row_player_one > 10 or submarine_row_player_one <= 0 or submarine_row_player_one % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.constants.validation_flag_submarine_player = False

        # check column
        if submarine_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if submarine_column_player_one > 8 or submarine_column_player_one <= 0 or submarine_column_player_one % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.constants.validation_flag_submarine_player = False
        else:
            if submarine_column_player_one > 10 or submarine_column_player_one <= 0 or submarine_column_player_one % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.constants.validation_flag_submarine_player = False
        return self.constants.validation_flag_submarine_player
