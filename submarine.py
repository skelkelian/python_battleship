from utils import Constants
from ship import Ship
from player import Player
from computer import Computer


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.constants = Constants()
        self.validation_flag_submarine_player = self.constants.get_constant_values('validation_flag_submarine_player')
        self.validation_flag_submarine_computer = self.constants.get_constant_values('validation_flag_submarine_computer')
        self.validation_flag_ship_sunk_submarine_player = self.constants.get_constant_values('validation_flag_ship_sunk_submarine_player')
        self.validation_flag_submarine_overlap_player = self.constants.get_constant_values('validation_flag_submarine_overlap_player')
        self.validation_flag_submarine_overlap_computer = self.constants.get_constant_values('validation_flag_submarine_overlap_computer')
        self.player = Player()
        self.computer = Computer()

    def validate_submarine_points(self, battleship_config):
        submarine_values_player_one = battleship_config.get('main', 'submarine_player')
        submarine_axis_player_one = int(submarine_values_player_one.split(',')[0].strip())
        submarine_row_player_one = int(submarine_values_player_one.split(',')[1].strip())
        submarine_column_player_one = int(submarine_values_player_one.split(',')[2].strip())

        # check axis
        if submarine_axis_player_one != self.constants.get_constant_values('horizontal_axis') and submarine_axis_player_one != self.constants.get_constant_values('vertical_axis'):
            print("The submarine axis value is invalid.")
            self.validation_flag_submarine_player = False

        # check row
        if submarine_axis_player_one == self.constants.get_constant_values('vertical_axis'):
            if submarine_row_player_one > 8 or submarine_row_player_one <= 0 or submarine_row_player_one % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.validation_flag_submarine_player = False
        else:
            if submarine_row_player_one > 10 or submarine_row_player_one <= 0 or submarine_row_player_one % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.validation_flag_submarine_player = False

        # check column
        if submarine_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if submarine_column_player_one > 8 or submarine_column_player_one <= 0 or submarine_column_player_one % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.validation_flag_submarine_player = False
        else:
            if submarine_column_player_one > 10 or submarine_column_player_one <= 0 or submarine_column_player_one % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.validation_flag_submarine_player = False
        return self.validation_flag_submarine_player

    def place_submarine_player_one(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        submarine_values_player_one = battleship_config.get('main', 'submarine_player')
        submarine_axis_player_one = int(submarine_values_player_one.split(',')[0].strip())
        submarine_row_player_one = int(submarine_values_player_one.split(',')[1].strip())
        submarine_column_player_one = int(submarine_values_player_one.split(',')[2].strip())
        if submarine_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one - 1] = self.constants.get_constant_values('submarine')
            primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one] = self.constants.get_constant_values('submarine')
            primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one + 1] = self.constants.get_constant_values('submarine')
        else:
            primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one - 1] = self.constants.get_constant_values('submarine')
            primary_board_player_one[submarine_row_player_one][submarine_column_player_one - 1] = self.constants.get_constant_values('submarine')
            primary_board_player_one[submarine_row_player_one + 1][submarine_column_player_one - 1] = self.constants.get_constant_values('submarine')

    def ship_sunk_submarine_player(self):
        hit_counter_player = self.player.get_hit_counter_player()
        if hit_counter_player[4] == 3:
            self.validation_flag_ship_sunk_submarine_player = True
            print("computer sunk player's submarine")
        return self.validation_flag_ship_sunk_submarine_player

    def validate_submarine_overlap(self, battleship_config):
        primary_board_player_one = self.player.get_primary_board_player_one()
        submarine_values_player_one = battleship_config.get('main', 'submarine_player')
        submarine_axis_player_one = int(submarine_values_player_one.split(',')[0].strip())
        submarine_row_player_one = int(submarine_values_player_one.split(',')[1].strip())
        submarine_column_player_one = int(submarine_values_player_one.split(',')[2].strip())

        # check if ship does not overlap
        if submarine_axis_player_one == self.constants.get_constant_values('horizontal_axis'):
            if primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one - 1] != 0 or \
                    primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one] != 0 or \
                    primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one + 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.validation_flag_submarine_overlap_player = False
        else:
            if primary_board_player_one[submarine_row_player_one - 1][submarine_column_player_one - 1] != 0 or \
                    primary_board_player_one[submarine_row_player_one][submarine_column_player_one - 1] != 0 or \
                    primary_board_player_one[submarine_row_player_one + 1][submarine_column_player_one - 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.validation_flag_submarine_overlap_player = False
        return self.validation_flag_submarine_overlap_player

    def validate_submarine_computer_points(self, battleship_config):
        submarine_values_computer = battleship_config.get('main', 'submarine_computer')
        submarine_axis_computer = int(submarine_values_computer.split(',')[0].strip())
        submarine_row_computer = int(submarine_values_computer.split(',')[1].strip())
        submarine_column_computer = int(submarine_values_computer.split(',')[2].strip())

        # check axis
        if submarine_axis_computer != self.constants.get_constant_values('horizontal_axis') and submarine_axis_computer != self.constants.get_constant_values('vertical_axis'):
            print("The submarine axis value is invalid.")
            self.validation_flag_submarine_computer = False

        # check row
        if submarine_axis_computer == self.constants.get_constant_values('vertical_axis'):
            if submarine_row_computer > 8 or submarine_row_computer <= 0 or submarine_row_computer % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.validation_flag_submarine_computer = False
        else:
            if submarine_row_computer > 10 or submarine_row_computer <= 0 or submarine_row_computer % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.validation_flag_submarine_computer = False

        # check column
        if submarine_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if submarine_column_computer > 8 or submarine_column_computer <= 0 or submarine_column_computer % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.validation_flag_submarine_computer = False
        else:
            if submarine_column_computer > 10 or submarine_column_computer <= 0 or submarine_column_computer % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.validation_flag_submarine_computer = False
        return self.validation_flag_submarine_computer

    def place_submarine_computer(self, battleship_config):
        primary_board_computer = self.computer.get_primary_board_computer()
        submarine_values_computer = battleship_config.get('main', 'submarine_computer')
        submarine_axis_computer = int(submarine_values_computer.split(',')[0].strip())
        submarine_row_computer = int(submarine_values_computer.split(',')[1].strip())
        submarine_column_computer = int(submarine_values_computer.split(',')[2].strip())
        if submarine_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] = self.constants.get_constant_values('submarine')
            primary_board_computer[submarine_row_computer - 1][submarine_column_computer] = self.constants.get_constant_values('submarine')
            primary_board_computer[submarine_row_computer - 1][submarine_column_computer + 1] = self.constants.get_constant_values('submarine')
        else:
            primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] = self.constants.get_constant_values('submarine')
            primary_board_computer[submarine_row_computer][submarine_column_computer - 1] = self.constants.get_constant_values('submarine')
            primary_board_computer[submarine_row_computer + 1][submarine_column_computer - 1] = self.constants.get_constant_values('submarine')

    def ship_sunk_submarine_computer(self):
        hit_counter_computer = self.computer.get_hit_counter_computer()
        if hit_counter_computer[4] == 3:
            self.constants.validation_flag_ship_sunk_submarine_computer = True
            print("player sunk computer's submarine")
        return self.constants.validation_flag_ship_sunk_submarine_computer

    def validate_submarine_computer_overlap(self, battleship_config):
        primary_board_computer = self.computer.get_primary_board_computer()
        submarine_values_computer = battleship_config.get('main', 'submarine_computer')
        submarine_axis_computer = int(submarine_values_computer.split(',')[0].strip())
        submarine_row_computer = int(submarine_values_computer.split(',')[1].strip())
        submarine_column_computer = int(submarine_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if submarine_axis_computer == self.constants.get_constant_values('horizontal_axis'):
            if primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] != 0 or \
                    primary_board_computer[submarine_row_computer - 1][submarine_column_computer] != 0 or \
                    primary_board_computer[submarine_row_computer - 1][submarine_column_computer + 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.validation_flag_submarine_overlap_computer = False
        else:
            if primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] != 0 or \
                    primary_board_computer[submarine_row_computer][submarine_column_computer - 1] != 0 or \
                    primary_board_computer[submarine_row_computer + 1][submarine_column_computer - 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.validation_flag_submarine_overlap_computer = False
        return self.validation_flag_submarine_overlap_computer
