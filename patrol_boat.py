from utils import Constants


class Patrol_Boat:
    def __init__(self):
        self.constants = Constants()

    def validate_patrol_boat_points(self, battleship_config):
        patrol_boat_values_player_one = battleship_config.get('main', 'patrol_boat_player')
        patrol_boat_axis_player_one = int(patrol_boat_values_player_one.split(',')[0].strip())
        patrol_boat_row_player_one = int(patrol_boat_values_player_one.split(',')[1].strip())
        patrol_boat_column_player_one = int(patrol_boat_values_player_one.split(',')[2].strip())

        # check axis
        if patrol_boat_axis_player_one != self.constants.HORIZONTAL_AXIS and patrol_boat_axis_player_one != self.constants.VERTICAL_AXIS:
            print("The patrol boat axis value is invalid.")
            self.constants.validation_flag_patrol_boat_player = False

        # check row
        if patrol_boat_axis_player_one == self.constants.VERTICAL_AXIS:
            if patrol_boat_row_player_one > 9 or patrol_boat_row_player_one <= 0 or patrol_boat_row_player_one % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_player = False
        else:
            if patrol_boat_row_player_one > 10 or patrol_boat_row_player_one <= 0 or patrol_boat_row_player_one % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_player = False

        # check column
        if patrol_boat_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if patrol_boat_column_player_one > 9 or patrol_boat_column_player_one <= 0 or patrol_boat_column_player_one % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_player = False
        else:
            if patrol_boat_column_player_one > 10 or patrol_boat_column_player_one <= 0 or patrol_boat_column_player_one % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_player = False
        return self.constants.validation_flag_patrol_boat_player
