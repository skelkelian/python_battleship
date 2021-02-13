# battleship
# imports
from configparser import ConfigParser
from carrier import Carrier
from cruiser import Cruiser
from destroyer import Destroyer
from patrol_boat import Patrol_Boat
from submarine import Submarine
from ship import Ship
from player import Player
from computer import Computer
from random import randint
import utils

# TODO'S NOW
# todo: how to integrate repo w travis
# todo: move the commits from destroyer to patrol boat and submarine respectively

# A CLASS IS A BLUE PRINT AND AN OBJECT IS SOMETHING YOU MAKE FROM THAT BLUE PRINT
# you declare attributes outside the constructor and you define inside the constructor


class BattleShip:
    # CONSTANTS

    # OPPONENT TYPE

    # GAME DIFFICULTY

    # SHIP IDENTIFICATION

    # AXIS

    # HIT COUNTER

    # VALIDATION PLAYER

    # VALIDATION COMPUTER

    # BOARD
    PRIMARY_BOARD = [
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
    SECONDARY_BOARD = [
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

    def __init__(self, config_name=None):
        self.constants = utils.Constants()
        self.carrier = Carrier()
        self.cruiser = Cruiser()
        self.destroyer = Destroyer()
        self.patrol_boat = Patrol_Boat()
        self.submarine = Submarine()
        self.ship = Ship()
        self.player = Player()
        self.computer = Computer()

        # create primary board for player 1 and computer
        self.primary_board_player_one = [
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

        self.secondary_board_player_one = [
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

        # if there is a config file, take values from there
        # if not, set the values to default
        if config_name is not None:
            # creates an object of ConfigParser
            self.config = ConfigParser()

            # read config file
            self.config.read(config_name)

            # get values from config file
            self.game_difficulty = int(self.config.get('main', 'game_difficulty'))
            self.opponent_type = int(self.config.get('main', 'opponent_type'))
            self.validate_game_difficulty()

            # PLAYER ONE
            self.carrier.validate_carrier_points(self.config)
            self.cruiser.validate_cruiser_points(self.config)
            self.destroyer.validate_destroyer_points(self.config)
            self.patrol_boat.validate_patrol_boat_points(self.config)
            self.submarine.validate_submarine_points(self.config)

            # COMPUTER
            self.validate_carrier_computer_points()
            self.cruiser.validate_cruiser_computer_points(self.config)
            self.validate_destroyer_computer_points()
            self.validate_patrol_boat_computer_points()
            self.validate_submarine_computer_points()
        else:
            self.game_difficulty = self.constants.EASY_DIFFICULTY
            self.opponent_type = self.constants.COMPUTER_OPPONENT

    def get_opponent_type(self):
        return self.opponent_type

    def get_game_difficulty(self):
        return self.game_difficulty

    def get_primary_board_player_one(self):
        return self.primary_board_player_one

    def get_primary_board_computer(self):
        return self.primary_board_computer

    def get_secondary_board_player_one(self):
        return self.secondary_board_player_one

    def print_directions(self):
        print('You have chosen to play against: ' + str(self.get_opponent_type()) +
              '\nThe game difficulty is ' + str(self.get_game_difficulty()))

    def validate_game_difficulty(self):
        if self.game_difficulty != self.constants.EASY_DIFFICULTY and \
                self.game_difficulty != self.constants.NORMAL_DIFFICULTY and \
                self.game_difficulty != self.constants.GOD_DIFFICULTY:
            self.game_difficulty = self.constants.EASY_DIFFICULTY
            print('You have selected an invalid choice for game difficulty.' +
                  '\nThe game difficulty has defaulted to easy.' +
                  '\nNext time try to choose a value that is valid.')
            self.constants.validation_flag_game = False
        return self.constants.validation_flag_game

    def place_carrier_computer(self):
        carrier_values_computer = self.config.get('main', 'carrier_computer')
        carrier_axis_computer = int(carrier_values_computer.split(',')[0].strip())
        carrier_row_computer = int(carrier_values_computer.split(',')[1].strip())
        carrier_column_computer = int(carrier_values_computer.split(',')[2].strip())
        if carrier_axis_computer == self.constants.HORIZONTAL_AXIS:
            self.primary_board_computer[carrier_row_computer - 1][carrier_column_computer - 1] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer - 1][carrier_column_computer] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer - 1][carrier_column_computer + 1] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer - 1][carrier_column_computer + 2] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer - 1][carrier_column_computer + 3] = self.constants.CARRIER
        else:
            self.primary_board_computer[carrier_row_computer - 1][carrier_column_computer - 1] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer][carrier_column_computer - 1] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer + 1][carrier_column_computer - 1] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer + 2][carrier_column_computer - 1] = self.constants.CARRIER
            self.primary_board_computer[carrier_row_computer + 3][carrier_column_computer - 1] = self.constants.CARRIER

    def place_battleship_player_one(self):
        battleship_values_player_one = self.config.get('main', 'battleship_player')
        battleship_axis_player_one = int(battleship_values_player_one.split(',')[0].strip())
        battleship_row_player_one = int(battleship_values_player_one.split(',')[1].strip())
        battleship_column_player_one = int(battleship_values_player_one.split(',')[2].strip())
        if battleship_axis_player_one == self.constants.HORIZONTAL_AXIS:
            self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one - 1] = self.constants.BATTLESHIP
            self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one] = self.constants.BATTLESHIP
            self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one + 1] = self.constants.BATTLESHIP
            self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one + 2] = self.constants.BATTLESHIP
        else:
            self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one - 1] = self.constants.BATTLESHIP
            self.primary_board_player_one[battleship_row_player_one][battleship_column_player_one - 1] = self.constants.BATTLESHIP
            self.primary_board_player_one[battleship_row_player_one + 1][battleship_column_player_one - 1] = self.constants.BATTLESHIP
            self.primary_board_player_one[battleship_row_player_one + 2][battleship_column_player_one - 1] = self.constants.BATTLESHIP

    def place_battleship_computer(self):
        battleship_values_computer = self.config.get('main', 'battleship_computer')
        battleship_axis_computer = int(battleship_values_computer.split(',')[0].strip())
        battleship_row_computer = int(battleship_values_computer.split(',')[1].strip())
        battleship_column_computer = int(battleship_values_computer.split(',')[2].strip())
        if battleship_axis_computer == self.constants.HORIZONTAL_AXIS:
            self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer - 1] = self.constants.BATTLESHIP
            self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer] = self.constants.BATTLESHIP
            self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer + 1] = self.constants.BATTLESHIP
            self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer + 2] = self.constants.BATTLESHIP
        else:
            self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer - 1] = self.constants.BATTLESHIP
            self.primary_board_computer[battleship_row_computer][battleship_column_computer - 1] = self.constants.BATTLESHIP
            self.primary_board_computer[battleship_row_computer + 1][battleship_column_computer - 1] = self.constants.BATTLESHIP
            self.primary_board_computer[battleship_row_computer + 2][battleship_column_computer - 1] = self.constants.BATTLESHIP

    def place_destroyer_computer(self):
        destroyer_values_computer = self.config.get('main', 'destroyer_computer')
        destroyer_axis_computer = int(destroyer_values_computer.split(',')[0].strip())
        destroyer_row_computer = int(destroyer_values_computer.split(',')[1].strip())
        destroyer_column_computer = int(destroyer_values_computer.split(',')[2].strip())
        if destroyer_axis_computer == self.constants.HORIZONTAL_AXIS:
            self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] = self.constants.DESTROYER
            self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer] = self.constants.DESTROYER
            self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer + 1] = self.constants.DESTROYER
        else:
            self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] = self.constants.DESTROYER
            self.primary_board_computer[destroyer_row_computer][destroyer_column_computer - 1] = self.constants.DESTROYER
            self.primary_board_computer[destroyer_row_computer + 1][destroyer_column_computer - 1] = self.constants.DESTROYER

    def place_patrol_boat_computer(self):
        patrol_boat_values_computer = self.config.get('main', 'patrol_boat_computer')
        patrol_boat_axis_computer = int(patrol_boat_values_computer.split(',')[0].strip())
        patrol_boat_row_computer = int(patrol_boat_values_computer.split(',')[1].strip())
        patrol_boat_column_computer = int(patrol_boat_values_computer.split(',')[2].strip())
        if patrol_boat_axis_computer == self.constants.HORIZONTAL_AXIS:
            self.primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] = self.constants.PATROL_BOAT
            self.primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer] = self.constants.PATROL_BOAT
        else:
            self.primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] = self.constants.PATROL_BOAT
            self.primary_board_computer[patrol_boat_row_computer][patrol_boat_column_computer - 1] = self.constants.PATROL_BOAT

    def place_submarine_computer(self):
        submarine_values_computer = self.config.get('main', 'submarine_computer')
        submarine_axis_computer = int(submarine_values_computer.split(',')[0].strip())
        submarine_row_computer = int(submarine_values_computer.split(',')[1].strip())
        submarine_column_computer = int(submarine_values_computer.split(',')[2].strip())
        if submarine_axis_computer == self.constants.HORIZONTAL_AXIS:
            self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] = self.constants.SUBMARINE
            self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer] = self.constants.SUBMARINE
            self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer + 1] = self.constants.SUBMARINE
        else:
            self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] = self.constants.SUBMARINE
            self.primary_board_computer[submarine_row_computer][submarine_column_computer - 1] = self.constants.SUBMARINE
            self.primary_board_computer[submarine_row_computer + 1][submarine_column_computer - 1] = self.constants.SUBMARINE

    def validate_battleship_points(self):
        battleship_values_player_one = self.config.get('main', 'battleship_player')
        battleship_axis_player_one = int(battleship_values_player_one.split(',')[0].strip())
        battleship_row_player_one = int(battleship_values_player_one.split(',')[1].strip())
        battleship_column_player_one = int(battleship_values_player_one.split(',')[2].strip())

        # check axis
        if battleship_axis_player_one != self.constants.HORIZONTAL_AXIS and battleship_axis_player_one != self.constants.VERTICAL_AXIS:
            print("The battleship axis value is invalid.")
            self.constants.validation_flag_battleship_player = False

        # check row
        if battleship_axis_player_one == self.constants.VERTICAL_AXIS:
            if battleship_row_player_one > 7 or battleship_row_player_one <= 0 or battleship_row_player_one % 1 != 0:
                print('\nThe battleship row value is invalid.\n\n')
                self.constants.validation_flag_battleship_player = False
        else:
            if battleship_row_player_one > 10 or battleship_row_player_one <= 0 or battleship_row_player_one % 1 != 0:
                print('\nThe battleship row value is invalid.\n\n')
                self.constants.validation_flag_battleship_player = False

        # check column
        if battleship_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if battleship_column_player_one > 7 or battleship_column_player_one <= 0 or battleship_column_player_one % 1 != 0:
                print('\nThe battleship column value is invalid.\n\n')
                self.constants.validation_flag_battleship_player = False
        else:
            if battleship_column_player_one > 10 or battleship_column_player_one <= 0 or battleship_column_player_one % 1 != 0:
                print('\nThe battleship column value is invalid.\n\n')
                self.constants.validation_flag_battleship_player = False
        return self.constants.validation_flag_battleship_player

    def validate_battleship_overlap(self):
        # obtain and parse through values
        battleship_values_player_one = self.config.get('main', 'battleship_player')
        battleship_axis_player_one = int(battleship_values_player_one.split(',')[0].strip())
        battleship_row_player_one = int(battleship_values_player_one.split(',')[1].strip())
        battleship_column_player_one = int(battleship_values_player_one.split(',')[2].strip())

        # check if ship does not overlap
        if battleship_axis_player_one == self.constants.HORIZONTAL_AXIS:
            if self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one - 1] != 0 or \
                    self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one] != 0 or \
                    self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one + 1] != 0 or \
                    self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one + 2] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.constants.validation_flag_battleship_overlap_player = False
        else:
            if self.primary_board_player_one[battleship_row_player_one - 1][battleship_column_player_one - 1] != 0 or \
                    self.primary_board_player_one[battleship_row_player_one][battleship_column_player_one - 1] != 0 or \
                    self.primary_board_player_one[battleship_row_player_one + 1][battleship_column_player_one - 1] != 0 or \
                    self.primary_board_player_one[battleship_row_player_one + 2][battleship_column_player_one - 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.constants.validation_flag_battleship_overlap_player = False
        return self.constants.validation_flag_battleship_overlap_player

# COMPUTER
    def validate_carrier_computer_points(self):
        carrier_values_computer = self.config.get('main', 'carrier_computer')
        carrier_axis_computer = int(carrier_values_computer.split(',')[0].strip())
        carrier_row_computer = int(carrier_values_computer.split(',')[1].strip())
        carrier_column_computer = int(carrier_values_computer.split(',')[2].strip())

        # check axis
        if carrier_axis_computer != self.constants.HORIZONTAL_AXIS and carrier_axis_computer != self.constants.VERTICAL_AXIS:
            print("The carrier axis value is invalid.")
            self.constants.validation_flag_carrier_computer = False

        # check row
        if carrier_axis_computer == self.constants.VERTICAL_AXIS:
            if carrier_row_computer > 6 or carrier_row_computer <= 0 or carrier_row_computer % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.constants.validation_flag_carrier_computer = False
        else:
            if carrier_row_computer > 10 or carrier_row_computer <= 0 or carrier_row_computer % 1 != 0:
                print('\nThe carrier row value is invalid.\n\n')
                self.constants.validation_flag_carrier_computer = False

        # check column
        if carrier_axis_computer == self.constants.HORIZONTAL_AXIS:
            if carrier_column_computer > 6 or carrier_column_computer <= 0 or carrier_column_computer % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.constants.validation_flag_carrier_computer = False
        else:
            if carrier_column_computer > 10 or carrier_column_computer <= 0 or carrier_column_computer % 1 != 0:
                print('\nThe carrier column value is invalid.\n\n')
                self.constants.validation_flag_carrier_computer = False
        return self.constants.validation_flag_carrier_computer

    def validate_battleship_computer_points(self):
        battleship_values_computer = self.config.get('main', 'battleship_computer')
        battleship_axis_computer = int(battleship_values_computer.split(',')[0].strip())
        battleship_row_computer = int(battleship_values_computer.split(',')[1].strip())
        battleship_column_computer = int(battleship_values_computer.split(',')[2].strip())

        # check axis
        if battleship_axis_computer != self.constants.HORIZONTAL_AXIS and battleship_axis_computer != self.constants.VERTICAL_AXIS:
            print("The battleship axis value is invalid.")
            self.constants.validation_flag_battleship_computer = False

        # check row
        if battleship_axis_computer == self.constants.VERTICAL_AXIS:
            if battleship_row_computer > 7 or battleship_row_computer <= 0 or battleship_row_computer % 1 != 0:
                print('\nThe battleship row value is invalid.\n\n')
                self.constants.validation_flag_battleship_computer = False
        else:
            if battleship_row_computer > 10 or battleship_row_computer <= 0 or battleship_row_computer % 1 != 0:
                print('\nThe battleship row value is invalid.\n\n')
                self.constants.validation_flag_battleship_computer = False

        # check column
        if battleship_axis_computer == self.constants.HORIZONTAL_AXIS:
            if battleship_column_computer > 7 or battleship_column_computer <= 0 or battleship_column_computer % 1 != 0:
                print('\nThe battleship column value is invalid.\n\n')
                self.constants.validation_flag_battleship_computer = False
        else:
            if battleship_column_computer > 10 or battleship_column_computer <= 0 or battleship_column_computer % 1 != 0:
                print('\nThe battleship column value is invalid.\n\n')
                self.constants.validation_flag_battleship_computer = False
        return self.constants.validation_flag_battleship_computer

    def validate_battleship_computer_overlap(self):
        # obtain and parse through values
        battleship_values_computer = self.config.get('main', 'battleship_computer')
        battleship_axis_computer = int(battleship_values_computer.split(',')[0].strip())
        battleship_row_computer = int(battleship_values_computer.split(',')[1].strip())
        battleship_column_computer = int(battleship_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if battleship_axis_computer == self.constants.HORIZONTAL_AXIS:
            if self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer - 1] != 0 or \
                    self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer] != 0 or \
                    self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer + 1] != 0 or \
                    self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer + 2] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.constants.validation_flag_battleship_overlap_computer = False
        else:
            if self.primary_board_computer[battleship_row_computer - 1][battleship_column_computer - 1] != 0 or \
                    self.primary_board_computer[battleship_row_computer][battleship_column_computer - 1] != 0 or \
                    self.primary_board_computer[battleship_row_computer + 1][battleship_column_computer - 1] != 0 or \
                    self.primary_board_computer[battleship_row_computer + 2][battleship_column_computer - 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.constants.validation_flag_battleship_overlap_computer = False
        return self.constants.validation_flag_battleship_overlap_computer

    def validate_destroyer_computer_points(self):
        destroyer_values_computer = self.config.get('main', 'destroyer_computer')
        destroyer_axis_computer = int(destroyer_values_computer.split(',')[0].strip())
        destroyer_row_computer = int(destroyer_values_computer.split(',')[1].strip())
        destroyer_column_computer = int(destroyer_values_computer.split(',')[2].strip())

        # check axis
        if destroyer_axis_computer != self.constants.HORIZONTAL_AXIS and destroyer_axis_computer != self.constants.VERTICAL_AXIS:
            print("The destroyer axis value is invalid.")
            self.constants.validation_flag_destroyer_computer = False

        # check row
        if destroyer_axis_computer == self.constants.VERTICAL_AXIS:
            if destroyer_row_computer > 8 or destroyer_row_computer <= 0 or destroyer_row_computer % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.constants.validation_flag_destroyer_computer = False
        else:
            if destroyer_row_computer > 10 or destroyer_row_computer <= 0 or destroyer_row_computer % 1 != 0:
                print('\nThe destroyer row value is invalid.\n\n')
                self.constants.validation_flag_destroyer_computer = False

        # check column
        if destroyer_axis_computer == self.constants.HORIZONTAL_AXIS:
            if destroyer_column_computer > 8 or destroyer_column_computer <= 0 or destroyer_column_computer % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.constants.validation_flag_destroyer_computer = False
        else:
            if destroyer_column_computer > 10 or destroyer_column_computer <= 0 or destroyer_column_computer % 1 != 0:
                print('\nThe destroyer column value is invalid.\n\n')
                self.constants.validation_flag_destroyer_computer = False
        return self.constants.validation_flag_destroyer_computer

    def validate_destroyer_computer_overlap(self):
        destroyer_values_computer = self.config.get('main', 'destroyer_computer')
        destroyer_axis_computer = int(destroyer_values_computer.split(',')[0].strip())
        destroyer_row_computer = int(destroyer_values_computer.split(',')[1].strip())
        destroyer_column_computer = int(destroyer_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if destroyer_axis_computer == self.constants.HORIZONTAL_AXIS:
            if self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] != 0 or \
                    self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer] != 0 or \
                    self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer + 1] != 0:
                print('\nThe destroyer overlaps with another ship.\n\n')
                self.constants.validation_flag_destroyer_overlap_computer = False
        else:
            if self.primary_board_computer[destroyer_row_computer - 1][destroyer_column_computer - 1] != 0 or \
                    self.primary_board_computer[destroyer_row_computer][destroyer_column_computer - 1] != 0 or \
                    self.primary_board_computer[destroyer_row_computer + 1][destroyer_column_computer - 1] != 0:
                print('\nThe destroyer overlaps with another ship.\n\n')
                self.constants.validation_flag_destroyer_overlap_computer = False
        return self.constants.validation_flag_destroyer_overlap_computer

    def validate_patrol_boat_computer_points(self):
        patrol_boat_values_computer = self.config.get('main', 'patrol_boat_computer')
        patrol_boat_axis_computer = int(patrol_boat_values_computer.split(',')[0].strip())
        patrol_boat_row_computer = int(patrol_boat_values_computer.split(',')[1].strip())
        patrol_boat_column_computer = int(patrol_boat_values_computer.split(',')[2].strip())

        # check axis
        if patrol_boat_axis_computer != self.constants.HORIZONTAL_AXIS and patrol_boat_axis_computer != self.constants.VERTICAL_AXIS:
            print("The patrol boat axis value is invalid.")
            self.constants.validation_flag_patrol_boat_computer = False

        # check row
        if patrol_boat_axis_computer == self.constants.VERTICAL_AXIS:
            if patrol_boat_row_computer > 9 or patrol_boat_row_computer <= 0 or patrol_boat_row_computer % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_computer = False
        else:
            if patrol_boat_row_computer > 10 or patrol_boat_row_computer <= 0 or patrol_boat_row_computer % 1 != 0:
                print('\nThe patrol boat row value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_computer = False

        # check column
        if patrol_boat_axis_computer == self.constants.HORIZONTAL_AXIS:
            if patrol_boat_column_computer > 9 or patrol_boat_column_computer <= 0 or patrol_boat_column_computer % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_computer = False
        else:
            if patrol_boat_column_computer > 10 or patrol_boat_column_computer <= 0 or patrol_boat_column_computer % 1 != 0:
                print('\nThe patrol boat column value is invalid.\n\n')
                self.constants.validation_flag_patrol_boat_computer = False
        return self.constants.validation_flag_patrol_boat_computer

    def validate_patrol_boat_computer_overlap(self):
        patrol_boat_values_computer = self.config.get('main', 'patrol_boat_computer')
        patrol_boat_axis_computer = int(patrol_boat_values_computer.split(',')[0].strip())
        patrol_boat_row_computer = int(patrol_boat_values_computer.split(',')[1].strip())
        patrol_boat_column_computer = int(patrol_boat_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if patrol_boat_axis_computer == self.constants.HORIZONTAL_AXIS:
            if self.primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] != 0 or \
                    self.primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer] != 0:
                print('\nThe patrol boat overlaps with another ship.\n\n')
                self.constants.validation_flag_patrol_boat_overlap_computer = False
        else:
            if self.primary_board_computer[patrol_boat_row_computer - 1][patrol_boat_column_computer - 1] != 0 or \
                    self.primary_board_computer[patrol_boat_row_computer][patrol_boat_column_computer - 1] != 0:
                print('\nThe patrol boat overlaps with another ship.\n\n')
                self.constants.validation_flag_patrol_boat_overlap_computer = False
        return self.constants.validation_flag_patrol_boat_overlap_computer

    def validate_submarine_computer_points(self):
        submarine_values_computer = self.config.get('main', 'submarine_computer')
        submarine_axis_computer = int(submarine_values_computer.split(',')[0].strip())
        submarine_row_computer = int(submarine_values_computer.split(',')[1].strip())
        submarine_column_computer = int(submarine_values_computer.split(',')[2].strip())

        # check axis
        if submarine_axis_computer != self.constants.HORIZONTAL_AXIS and submarine_axis_computer != self.constants.VERTICAL_AXIS:
            print("The submarine axis value is invalid.")
            self.constants.validation_flag_submarine_computer = False

        # check row
        if submarine_axis_computer == self.constants.VERTICAL_AXIS:
            if submarine_row_computer > 8 or submarine_row_computer <= 0 or submarine_row_computer % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.constants.validation_flag_submarine_computer = False
        else:
            if submarine_row_computer > 10 or submarine_row_computer <= 0 or submarine_row_computer % 1 != 0:
                print('\nThe submarine row value is invalid.\n\n')
                self.constants.validation_flag_submarine_computer = False

        # check column
        if submarine_axis_computer == self.constants.HORIZONTAL_AXIS:
            if submarine_column_computer > 8 or submarine_column_computer <= 0 or submarine_column_computer % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.constants.validation_flag_submarine_computer = False
        else:
            if submarine_column_computer > 10 or submarine_column_computer <= 0 or submarine_column_computer % 1 != 0:
                print('\nThe submarine column value is invalid.\n\n')
                self.constants.validation_flag_submarine_computer = False
        return self.constants.validation_flag_submarine_computer

    def validate_submarine_computer_overlap(self):
        # obtain and parse through values
        submarine_values_computer = self.config.get('main', 'submarine_computer')
        submarine_axis_computer = int(submarine_values_computer.split(',')[0].strip())
        submarine_row_computer = int(submarine_values_computer.split(',')[1].strip())
        submarine_column_computer = int(submarine_values_computer.split(',')[2].strip())

        # check if ship does not overlap
        if submarine_axis_computer == self.constants.HORIZONTAL_AXIS:
            if self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] != 0 or \
                    self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer] != 0 or \
                    self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer + 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.constants.validation_flag_submarine_overlap_computer = False
        else:
            if self.primary_board_computer[submarine_row_computer - 1][submarine_column_computer - 1] != 0 or \
                    self.primary_board_computer[submarine_row_computer][submarine_column_computer - 1] != 0 or \
                    self.primary_board_computer[submarine_row_computer + 1][submarine_column_computer - 1] != 0:
                print('\nThe battleship overlaps with another ship.\n\n')
                self.constants.validation_flag_submarine_overlap_computer = False
        return self.constants.validation_flag_submarine_overlap_computer

    def place_point_on_primary_player(self):
        row_selected, column_selected = self.player.pick_point_player_one()
        self.primary_board_computer[row_selected - 1][column_selected - 1] = 9
        return self.primary_board_computer

    def place_point_on_secondary_player(self):
        row_selected, column_selected = self.player.pick_point_player_one()
        self.secondary_board_player_one[row_selected - 1][column_selected - 1] = 1
        return self.secondary_board_player_one

    def place_point_on_primary_computer(self):
        row_selected, column_selected = self.computer.pick_point_computer()
        self.primary_board_player_one[row_selected - 1][column_selected - 1] = 9
        return self.primary_board_player_one

    def place_point_on_secondary_computer(self):
        row_selected, column_selected = self.computer.pick_point_computer()
        self.secondary_board_computer[row_selected - 1][column_selected - 1] = 1
        return self.secondary_board_computer

    def hit_or_miss_player(self):  # player attacking computer's ships
        row_selected, column_selected = self.player.pick_point_player_one()
        primary_board_computer = self.ship.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.SUBMARINE and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.PATROL_BOAT and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.DESTROYER and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.BATTLESHIP and \
                primary_board_computer[row_selected - 1][column_selected - 1] != self.constants.CARRIER:
            self.constants.validation_flag_hit_or_miss_player = False
            self.secondary_board_player_one[row_selected - 1][column_selected - 1] = -1
        else:
            self.primary_board_computer[row_selected - 1][column_selected - 1] = 9
            self.secondary_board_player_one[row_selected - 1][column_selected - 1] = 1
        return self.constants.validation_flag_hit_or_miss_player

    def hit_or_miss_computer(self):  # computer attacking player's ships
        row_selected, column_selected = self.pick_point_computer()
        primary_board_player = self.get_primary_board_player_one()
        if primary_board_player[row_selected - 1][column_selected - 1] != self.constants.SUBMARINE and \
                primary_board_player[row_selected - 1][column_selected - 1] != self.constants.PATROL_BOAT and \
                primary_board_player[row_selected - 1][column_selected - 1] != self.constants.DESTROYER and \
                primary_board_player[row_selected - 1][column_selected - 1] != self.constants.BATTLESHIP and \
                primary_board_player[row_selected - 1][column_selected - 1] != self.constants.CARRIER:
            self.constants.validation_flag_hit_or_miss_computer = False
            self.secondary_board_computer[row_selected - 1][column_selected - 1] = -1
        else:
            self.primary_board_player_one[row_selected - 1][column_selected - 1] = 9
            self.secondary_board_computer[row_selected - 1][column_selected - 1] = 1
        return self.constants.validation_flag_hit_or_miss_computer

    def hit_counter_computer(self):  # this tracks the player's hits on the computer's ships
        row_selected, column_selected = self.pick_point_player_one()
        primary_board_computer = self.get_primary_board_computer()
        if primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.CARRIER:
            self.constants.HIT_COUNTER_COMPUTER[0] = self.constants.HIT_COUNTER_COMPUTER[0] + 1
            print("hit carrier")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.BATTLESHIP:
            self.constants.HIT_COUNTER_COMPUTER[1] = self.constants.HIT_COUNTER_COMPUTER[1] + 1
            print("hit battleship")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.DESTROYER:
            self.constants.HIT_COUNTER_COMPUTER[2] = self.constants.HIT_COUNTER_COMPUTER[2] + 1
            print("hit destroyer")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.PATROL_BOAT:
            self.constants.HIT_COUNTER_COMPUTER[3] = self.constants.HIT_COUNTER_COMPUTER[3] + 1
            print("hit patrol boat")
        elif primary_board_computer[row_selected - 1][column_selected - 1] == self.constants.SUBMARINE:
            self.constants.HIT_COUNTER_COMPUTER[4] = self.constants.HIT_COUNTER_COMPUTER[4] + 1
            print("hit submarine")
        else:
            self.constants.validation_flag_hit_counter_player = False
            print("missed ships")
        return self.constants.validation_flag_hit_counter_player

    def hit_counter_player(self):  # this tracks the computer's hits on the player's ships
        row_selected, column_selected = self.pick_point_computer()
        primary_board_player = self.get_primary_board_player_one()
        if primary_board_player[row_selected - 1][column_selected - 1] == self.constants.CARRIER:
            self.constants.HIT_COUNTER_PLAYER_ONE[0] = self.constants.HIT_COUNTER_PLAYER_ONE[0] + 1
            print("hit carrier")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.BATTLESHIP:
            self.constants.HIT_COUNTER_PLAYER_ONE[1] = self.constants.HIT_COUNTER_PLAYER_ONE[1] + 1
            print("hit battleship")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.DESTROYER:
            self.constants.HIT_COUNTER_PLAYER_ONE[2] = self.constants.HIT_COUNTER_PLAYER_ONE[2] + 1
            print("hit destroyer")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.PATROL_BOAT:
            self.constants.HIT_COUNTER_PLAYER_ONE[3] = self.constants.HIT_COUNTER_PLAYER_ONE[3] + 1
            print("hit patrol boat")
        elif primary_board_player[row_selected - 1][column_selected - 1] == self.constants.SUBMARINE:
            self.constants.HIT_COUNTER_PLAYER_ONE[4] = self.constants.HIT_COUNTER_PLAYER_ONE[4] + 1
            print("hit submarine")
        else:
            self.constants.validation_flag_hit_counter_computer = False
            print("missed ships")
        return self.constants.validation_flag_hit_counter_computer

    def get_hit_counter_player(self):
        return self.HIT_COUNTER_PLAYER_ONE

    def get_hit_counter_computer(self):
        return self.HIT_COUNTER_COMPUTER

    def ship_sunk_battleship_player(self):
        hit_counter_player = self.get_hit_counter_player()
        if hit_counter_player[1] == 4:
            self.constants.validation_flag_ship_sunk_battleship_player = True
            print("computer sunk player's battleship")
        return self.constants.validation_flag_ship_sunk_battleship_player

    def ship_sunk_carrier_computer(self):
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[0] == 5:
            self.constants.validation_flag_ship_sunk_carrier_computer = True
            print("player sunk computer's carrier")
        return self.constants.validation_flag_ship_sunk_carrier_computer

    def ship_sunk_battleship_computer(self):
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[1] == 4:
            self.validation_flag_ship_sunk_battleship_computer = True
            print("player sunk computer's battleship")
        return self.validation_flag_ship_sunk_battleship_computer

    def ship_sunk_destroyer_computer(self):
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[2] == 3:
            self.constants.validation_flag_ship_sunk_destroyer_computer = True
            print("player sunk computer's destroyer")
        return self.constants.validation_flag_ship_sunk_destroyer_computer

    def ship_sunk_patrol_boat_computer(self):
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[3] == 2:
            self.constants.validation_flag_ship_sunk_patrol_boat_computer = True
            print("player sunk computer's patrol boat")
        return self.constants.validation_flag_ship_sunk_patrol_boat_computer

    def ship_sunk_submarine_computer(self):
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[4] == 3:
            self.constants.validation_flag_ship_sunk_submarine_computer = True
            print("player sunk computer's submarine")
        return self.constants.validation_flag_ship_sunk_submarine_computer

    def game_over_player(self):  # if this triggers, the player lost
        hit_counter_player = self.get_hit_counter_player()
        if hit_counter_player[0] + hit_counter_player[1] + hit_counter_player[2] + \
                hit_counter_player[3] + hit_counter_player[4] == 17:
            self.constants.validation_flag_game_over_player = True
        return self.constants.validation_flag_game_over_player

    def game_over_computer(self):  # if this triggers, the computer lost
        hit_counter_computer = self.get_hit_counter_computer()
        if hit_counter_computer[0] + hit_counter_computer[1] + hit_counter_computer[2] + \
                hit_counter_computer[3] + hit_counter_computer[4] == 17:
            self.constants.validation_flag_game_over_computer = True
        return self.constants.validation_flag_game_over_computer

# START GAME

    def start_game(self):
        self.carrier.place_carrier_player_one(self.config)
        self.cruiser.place_cruiser_player_one(self.config)
        self.destroyer.place_destroyer_player_one(self.config)
        self.patrol_boat.place_patrol_boat_player_one(self.config)
        self.submarine.place_submarine_player_one(self.config)
        self.carrier.place_carrier_computer(self.config)
        self.cruiser.place_cruiser_computer(self.config)
        self.destroyer.place_destroyer_computer(self.config)
        self.patrol_boat.place_patrol_boat_computer(self.config)
        self.submarine.place_submarine_computer(self.config)
        self.cruiser.validate_cruiser_overlap(self.config)
        self.destroyer.validate_destroyer_overlap(self.config)
        self.patrol_boat.validate_patrol_boat_overlap(self.config)
        self.submarine.validate_submarine_overlap(self.config)
        self.cruiser.validate_cruiser_computer_overlap(self.config)
        self.destroyer.validate_destroyer_computer_overlap(self.config)
        self.patrol_boat.validate_patrol_boat_computer_overlap(self.config)
        self.submarine.validate_submarine_computer_overlap(self.config)

    def play_game(self):
        game_over = 0
        while game_over == 0:
            self.start_game()
            self.hit_or_miss_player()
            while self.constants.validation_flag_hit_or_miss_player is True:
                self.hit_counter_computer()
                self.ship_sunk_carrier_computer()
                self.ship_sunk_battleship_computer()
                self.ship_sunk_destroyer_computer()
                self.ship_sunk_patrol_boat_computer()
                self.ship_sunk_submarine_computer()
                self.game_over_computer()
            self.hit_or_miss_computer()
            while self.constants.validation_flag_hit_or_miss_computer is True:
                self.hit_counter_player()
                self.carrier.ship_sunk_carrier_player(self.get_hit_counter_player)
                self.ship_sunk_battleship_player()
                self.destroyer.ship_sunk_destroyer_player(self.get_hit_counter_player)
                self.patrol_boat.ship_sunk_patrol_boat_player(self.get_hit_counter_player)
                self.submarine.ship_sunk_submarine_player(self.get_hit_counter_player)
                self.game_over_player()

        # functions
        #   def pretty_print_list(self, matrix):
    #         for row in range(0, len(matrix)):
    #             print(matrix[row])
    #             for col in range(0, len(matrix)-1):
    #                 pass







# pick
# validate
# place
# check if hit or miss
    # go to primary board and check if there is a point in the row and column that was picked
    # if hit
        # place 1 on secondary board in that location
        # check which ship it hit
        # adjust hit counter
    # if miss
        # place 2 on secondary board in that location


        # def test_pick_target(self):
        #     row_picked = (randint(1, 10))
        #
        #     return ____



        # def start(self):
        
        # functions
        #   def pretty_print_list(self, matrix):
    #         for row in range(0, len(matrix)):
    #             print(matrix[row])
    #             for col in range(0, len(matrix)-1):
    #                 pass
    #


        # # display directions
        # print('If you want to play against a computer type 1 \nIf you want to play against a friend type 2\n')
        #
        # # have them pick gamemode
        # gameMode = int(input('Enter who you would like to play against a computer(1) or a friend(2): '))
        # while gameMode != 1 and gameMode != 2:
        #     gameMode = int(input('Please select either 1 or 2: '))
        #
        # # run code depending on which gamemode chosen
        # if int(gameMode) == 1:
        #     # display rules for computer mode
        #     print('\nYou have chose to play against a computer. \nTake turns choosing points on the computers 10x10 board \nin hopes of hitting a part of the ship. \nIf you hit every part of the ship it will be sunk and \nyou will continue picking points until you sink all ships. \nThe first player to sink all opponent ships wins. \n\nGoodluck, Have fun! \n\n')
        #
        #     # ask for difficulty
        #     gameDifficulty = int(input('Enter what level computer you would like to play against, easy(1), pro(2) or god(3): '))
        #     while gameDifficulty != 1 and gameDifficulty != 2 and gameDifficulty != 3:
        #         gameDifficulty = int(input('Please select either 1, 2 or 3: '))
        #
        #     # player 1 picking points
        #
        #     # create primary board for player 1
        #     self.primary_board_player_one = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #
        #     # carrier
        #
        #     # horizontal or vertical axis
        #     CA1 = int(input('Specify whether you would like your carrier to be horizontal(1) or vertical(2): '))  # carrier axis player one
        #     while CA1 != 1 and CA1 != 2:
        #         CA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for carrier
        #     CR1 = int(input('Specify what row you would like to place the carrier: '))  # carrier row player one
        #     while CR1 != 1 and CR1 != 2 and CR1 != 3 and CR1 != 4 and CR1 != 5 and CR1 != 6 and CR1 != 7 and CR1 != 8 and CR1 != 9 and CR1 != 10:
        #         CR1 = int(input('Please select a number between 1-10: '))
        #     CC1 = int(input('Specify what column you would like to place the carrier: '))  # carrier column player one
        #     while CC1 != 1 and CC1 != 2 and CC1 != 3 and CC1 != 4 and CC1 != 5 and CC1 != 6 and CC1 != 7 and CC1 != 8 and CC1 != 9 and CC1 != 10:
        #         CC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify that the ship will fit and place points
        #     if CA1 == 1:
        #         while CC1 > 6 or CC1 <= 0 or CC1 % 1 != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             CR1 = int(input('Try a row integer that is between 1 and 6: '))
        #             CC1 = int(input('Try a column integer that is between 1 and 6: '))
        #         self.primary_board_player_one[CR1 - 1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1 + 1] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1 + 2] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1 + 3] = 5
        #     else:
        #         while CR1 > 6 or CR1 <= 0 or CR1 % 1 != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             CR1 = int(input('Try a row integer that is between 1 and 6: '))
        #             CC1 = int(input('Try a column integer that is between 1 and 6: '))
        #         self.primary_board_player_one[CR1 - 1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 + 1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 + 2][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 + 3][CC1 - 1] = 5
        #
        #
        #     # display board
        #     # # pretty_print_list(self.primary_board_player_one)
        #     print('Your carrier has been placed \n\n')
        #
        #     # battleship
        #
        #     # horizontal or vertical axis
        #     BA1 = int(input('Specify whether you would like your battleship to be horizontal(1) or vertical(2): '))  # battleship axis player one
        #     while BA1 != 1 and BA1 != 2:
        #         BA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for battleship
        #     BR1 = int(input('Specify what row you would like to place the battleship: ')) # battleship row player one
        #     while BR1 != 1 and BR1 != 2 and BR1 != 3 and BR1 != 4 and BR1 != 5 and BR1 != 6 and BR1 != 7 and BR1 != 8 and BR1 != 9 and BR1 != 10:
        #         BR1 = int(input('Please select a number between 1-10: '))
        #     BC1 = int(input('Specify what column you would like to place the battleship: ')) # battleship column player one
        #     while BC1 != 1 and BC1 != 2 and BC1 != 3 and BC1 != 4 and BC1 != 5 and BC1 != 6 and BC1 != 7 and BC1 != 8 and BC1 != 9 and BC1 != 10:
        #         BC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if BA1 == 1:
        #         while BC1 > 7 or BC1 <= 0 or BC1 % 1 != 0 or self.primary_board_player_one[BR1 - 1][BC1 - 1] != 0 or self.primary_board_player_one[BR1 - 1][BC1] != 0 or self.primary_board_player_one[BR1 - 1][BC1 + 1] != 0 or self.primary_board_player_one[BR1 - 1][BC1 + 2] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             BR1 = int(input('Try a row integer that is between 1 and 7: '))
        #             BC1 = int(input('Try a column integer that is between 1 and 7: '))
        #         self.primary_board_player_one[BR1 - 1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1 - 1][BC1] = 4
        #         self.primary_board_player_one[BR1 - 1][BC1 + 1] = 4
        #         self.primary_board_player_one[BR1 - 1][BC1 + 2] = 4
        #     else:
        #         while BR1 > 7 or BR1 <= 0 or BR1 % 1 != 0 or self.primary_board_player_one[BR1 - 1][BC1 - 1] != 0 or self.primary_board_player_one[BR1][BC1 - 1] != 0 or self.primary_board_player_one[BR1 + 1][BC1 - 1] != 0 or self.primary_board_player_one[BR1 + 2][BC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             BR1 = int(input('Try a row integer that is between 1 and 7: '))
        #             BC1 = int(input('Try a column integer that is between 1 and 7: '))
        #         self.primary_board_player_one[BR1 - 1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1 + 1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1 + 2][BC1 - 1] = 4
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your battleship has been placed \n\n')
        #
        #     # destroyer
        #
        #     # horizontal or vertical axis
        #     DA1 = int(input('Specify whether you would like your destroyer to be horizontal(1) or vertical(2): '))  # destroyer axis player one
        #     while DA1 != 1 and DA1 != 2:
        #         DA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for destroyer
        #     DR1 = int(input('Specify what row you would like to place the destroyer: ')) # destroyer row player one
        #     while DR1 != 1 and DR1 != 2 and DR1 != 3 and DR1 != 4 and DR1 != 5 and DR1 != 6 and DR1 != 7 and DR1 != 8 and DR1 != 9 and DR1 != 10:
        #         DR1 = int(input('Please select a number between 1-10: '))
        #     DC1 = int(input('Specify what column you would like to place the destroyer: ')) # destroyer column player one
        #     while DC1 != 1 and DC1 != 2 and DC1 != 3 and DC1 != 4 and DC1 != 5 and DC1 != 6 and DC1 != 7 and DC1 != 8 and DC1 != 9 and DC1 != 10:
        #         DC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if DA1 == 1:
        #         while DC1 > 8 or DC1 < 0 or DC1 % 1 != 0 or self.primary_board_player_one[DR1 - 1][DC1 - 1] != 0 or self.primary_board_player_one[DR1 - 1][DC1] != 0 or self.primary_board_player_one[DR1 - 1][DC1 + 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             DR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             DC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[DR1 - 1][DC1 - 1] = 3
        #         self.primary_board_player_one[DR1 - 1][DC1] = 3
        #         self.primary_board_player_one[DR1 - 1][DC1 + 1] = 3
        #     else:
        #         while DR1 > 8 or DR1 < 0 or DR1 % 1 != 0 or self.primary_board_player_one[DR1 - 1][DC1 - 1] != 0 or self.primary_board_player_one[DR1][DC1 - 1] != 0 or self.primary_board_player_one[DR1 + 1][DC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             DR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             DC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[DR1 - 1][DC1 - 1] = 3
        #         self.primary_board_player_one[DR1][DC1 - 1] = 3
        #         self.primary_board_player_one[DR1 + 1][DC1 - 1] = 3
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your destroyer has been placed \n\n')
        #
        #     # submarine
        #
        #     # horizontal or vertical axis
        #     SA1 = int(input('Specify whether you would like your submarine to be horizontal(1) or vertical(2): ')) # submarine axis player one
        #     while SA1 != 1 and SA1 != 2:
        #         SA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for submarine
        #     SR1 = int(input('Specify what row you would like to place the submarine: ')) # submarine row player one
        #     while SR1 != 1 and SR1 != 2 and SR1 != 3 and SR1 != 4 and SR1 != 5 and SR1 != 6 and SR1 != 7 and SR1 != 8 and SR1 != 9 and SR1 != 10:
        #         SR1 = int(input('Please select a number between 1-10: '))
        #     SC1 = int(input('Specify what column you would like to place the submarine: ')) # submarine column player one
        #     while SC1 != 1 and SC1 != 2 and SC1 != 3 and SC1 != 4 and SC1 != 5 and SC1 != 6 and SC1 != 7 and SC1 != 8 and SC1 != 9 and SC1 != 10:
        #         SC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if SA1 == 1:
        #         while SC1 > 8 or SC1 < 0 or SC1 % 1 != 0 or self.primary_board_player_one[SR1 - 1][SC1 - 1] != 0 or self.primary_board_player_one[SR1 - 1][SC1] != 0 or self.primary_board_player_one[SR1 - 1][SC1 + 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             SR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             SC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[SR1 - 1][SC1 - 1] = 1
        #         self.primary_board_player_one[SR1 - 1][SC1] = 1
        #         self.primary_board_player_one[SR1 - 1][SC1 + 1] = 1
        #     else:
        #         while SR1 > 8 or SR1 < 0 or SR1 % 1 != 0 or self.primary_board_player_one[SR1 - 1][SC1 - 1] != 0 or self.primary_board_player_one[SR1][SC1 - 1] != 0 or self.primary_board_player_one[SR1 + 1][SC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             SR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             SC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[SR1 - 1][SC1 - 1] = 1
        #         self.primary_board_player_one[SR1][SC1 - 1] = 1
        #         self.primary_board_player_one[SR1 + 1][SC1 - 1] = 1
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your submarine has been placed \n\n')
        #
        #     # patrol boat
        #
        #     # horizontal or vertical axis
        #     PA1 = int(input('Specify whether you would like your patrol boat to be horizontal(1) or vertical(2): ')) # patrol boat axis player one
        #     while PA1 != 1 and PA1 != 2:
        #         PA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for patrol boat
        #     PR1 = int(input('Specify what row you would like to place the patrol boat: '))  # patrol boat row player one
        #     while PR1 != 1 and PR1 != 2 and PR1 != 3 and PR1 != 4 and PR1 != 5 and PR1 != 6 and PR1 != 7 and PR1 != 8 and PR1 != 9 and PR1 != 10:
        #         PR1 = int(input('Please select a number between 1-10: '))
        #     PC1 = int(input('Specify what column you would like to place the patrol boat: '))  # patrol boat column player one
        #     while PC1 != 1 and PC1 != 2 and PC1 != 3 and PC1 != 4 and PC1 != 5 and PC1 != 6 and PC1 != 7 and PC1 != 8 and PC1 != 9 and PC1 != 10:
        #         PC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if PA1 == 1:
        #         while PC1 > 9 or PC1 < 0 or PC1 % 1 != 0 or self.primary_board_player_one[PR1 - 1][PC1 - 1] != 0 or self.primary_board_player_one[PR1 - 1][PC1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             PR1 = int(input('Try a row integer that is between 1 and 9: '))
        #             PC1 = int(input('Try a column integer that is between 1 and 9: '))
        #         self.primary_board_player_one[PR1 - 1][PC1 - 1] = 2
        #         self.primary_board_player_one[PR1 - 1][PC1] = 2
        #     else:
        #         while PR1 > 9 or PR1 < 0 or PR1 % 1 != 0 or self.primary_board_player_one[PR1 - 1][PC1 - 1] != 0 or self.primary_board_player_one[PR1][PC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             PR1 = int(input('Try a row integer that is between 1 and 9: '))
        #             PC1 = int(input('Try a column integer that is between 1 and 9: '))
        #         self.primary_board_player_one[PR1 - 1][PC1 - 1] = 2
        #         self.primary_board_player_one[PR1][PC1 - 1] = 2
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your patrol boat has been placed \n\n')
        #
        #     # computer picking points
        #
        #     # create primary board for computer
        #     PB2 = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #
        #     # carrier
        #
        #     # horizontal or vertical axis
        #     CA2 = (randint(1, 2))  # carrier axis computer
        #
        #     # have computer assign location for carrier
        #     CR2 = (randint(1, 10))
        #     CC2 = (randint(1, 10))
        #
        #     # verify ship will fit
        #     if CA2 == 1:
        #         while CC2>6:
        #             CR2 = (randint(1, 6))
        #             CC2 = (randint(1, 6))
        #     else:
        #         while CR2>6:
        #             CR2 = (randint(1, 6))
        #             CC2 = (randint(1, 6))
        #
        #     # autoplace the points
        #     if CA2 == 1:
        #         PB2[CR2 - 1][CC2 - 1] = 5
        #         PB2[CR2 - 1][CC2] = 5
        #         PB2[CR2 - 1][CC2 + 1] = 5
        #         PB2[CR2 - 1][CC2 + 2] = 5
        #         PB2[CR2 - 1][CC2 + 3] = 5
        #     else:
        #         PB2[CR2 - 1][CC2 - 1] = 5
        #         PB2[CR2][CC2 - 1] = 5
        #         PB2[CR2 + 1][CC2 - 1] = 5
        #         PB2[CR2 + 2][CC2 - 1] = 5
        #         PB2[CR2 + 3][CC2 - 1] = 5
        #
        #     # battleship
        #
        #     # horizontal or vertical axis
        #     BA2 = (randint(1, 2))
        #
        #     # have computer assign location for battleship
        #     BR2 = (randint(1, 10))
        #     BC2 = (randint(1, 10))
        #
        #     # verify ship will fit and place points
        #     if BA2 == 1:
        #         while BC2 > 7 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2 - 1][BC2] != 0 or PB2[BR2 - 1][BC2 + 1] != 0 or PB2[BR2 - 1][BC2 + 2] != 0:
        #             BR2 = (randint(1, 7))
        #             BC2 = (randint(1, 7))
        #         PB2[BR2 - 1][BC2 - 1] = 4
        #         PB2[BR2 - 1][BC2] = 4
        #         PB2[BR2 - 1][BC2 + 1] = 4
        #         PB2[BR2 - 1][BC2 + 2] = 4
        #     else:
        #         while BR2 > 7 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2][BC2 - 1] != 0 or PB2[BR2 + 1][BC2 - 1] != 0 or PB2[BR2 + 2][BC2 - 1] != 0:
        #             BR2 = (randint(1, 7))
        #             BC2 = (randint(1, 7))
        #         PB2[BR2 - 1][BC2 - 1] = 4
        #         PB2[BR2][BC2 - 1] = 4
        #         PB2[BR2 + 1][BC2 - 1] = 4
        #         PB2[BR2 + 2][BC2 - 1] = 4
        #
        #     # destroyer
        #
        #     # horizontal or vertical axis
        #     DA2 = (randint(1, 2))
        #
        #     # have computer assign location for destroyer
        #     DR2 = (randint(1, 10))
        #     DC2 = (randint(1, 10))
        #
        #     # verify ship will fit and place points
        #     if DA2 == 1:
        #         while DC2 > 8 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2 - 1][DC2] != 0 or PB2[DR2 - 1][DC2 + 1] != 0:
        #             DR2 = (randint(1, 8))
        #             DC2 = (randint(1, 8))
        #         PB2[DR2 - 1][DC2 - 1] = 3
        #         PB2[DR2 - 1][DC2] = 3
        #         PB2[DR2 - 1][DC2 + 1] = 3
        #     else:
        #         while DR2>8 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2][DC2 - 1] != 0 or PB2[DR2 + 1][DC2 - 1] != 0:
        #             DR2 = (randint(1, 8))
        #             DC2 = (randint(1, 8))
        #         PB2[DR2 - 1][DC2 - 1] = 3
        #         PB2[DR2][DC2 - 1] = 3
        #         PB2[DR2 + 1][DC2 - 1] = 3
        #
        #     # submarine
        #
        #     # horizontal or vertical axis
        #     SA2 = (randint(1, 2))
        #
        #     # have computer assign location for submarine
        #     SR2 = (randint(1, 10))
        #     SC2 = (randint(1, 10))
        #
        #     # verify ship will fit and place points
        #     if SA2 == 1:
        #         while SC2 > 8 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2 - 1][SC2] != 0 or PB2[SR2 - 1][SC2 + 1] != 0:
        #             SR2 = (randint(1, 8))
        #             SC2 = (randint(1, 8))
        #         PB2[SR2 - 1][SC2 - 1] = 1
        #         PB2[SR2 - 1][SC2] = 1
        #         PB2[SR2 - 1][SC2 + 1] = 1
        #     else:
        #         while SR2 > 8 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2][SC2 - 1] != 0 or PB2[SR2 + 1][SC2 - 1] != 0:
        #             SR2 = (randint(1, 8))
        #             SC2 = (randint(1, 8))
        #         PB2[SR2 - 1][SC2 - 1] = 1
        #         PB2[SR2][SC2 - 1] = 1
        #         PB2[SR2 + 1][SC2 - 1] = 1
        #
        #     # patrol boat
        #
        #     # horizontal or vertical axis
        #     PA2 = (randint(1, 2))
        #
        #     # have computer assign location for patrol boat
        #     PR2 = (randint(1, 10))
        #     PC2 = (randint(1, 10))
        #
        #     # verify ship will fit and place points
        #     if PA2 == 1:
        #         while PC2 > 9 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2 - 1][PC2] != 0:
        #             PR2 = (randint(1, 9))
        #             PC2 = (randint(1, 9))
        #         PB2[PR2 - 1][PC2 - 1] = 2
        #         PB2[PR2 - 1][PC2] = 2
        #     else:
        #         while PR2 > 9 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2][PC2 - 1] != 0:
        #             PR2 = (randint(1, 9))
        #             PC2 = (randint(1, 9))
        #         PB2[PR2 - 1][PC2 - 1] = 2
        #         PB2[PR2][PC2 - 1] = 2
        #
        #     # create secondary board for player and computer
        #     SB1 = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #     SB2 = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #
        #     # create hit counter for each ship
        #
        #     # list of hit counters
        #     HCA1 = [0, 0, 0, 0, 0]
        #     HCA2 = [0, 0, 0, 0, 0]
        #     # 5,4,3,2,1 (5 = carrier, 4 = battleship, 3 = destroyer, 2 = patrol boat, 1 = submarine)
        #
        #     # create while loop so game continues until someone wins
        #     gameover = 0
        #     while gameover == 0:
        #
        #         # player 1 picks a point
        #         print('\nIT IS YOUR TURN PLAYER 1\n\n')
        #         P1PR = int(input('Pick a row you think one of the opponents ship is on: '))  # player one point row
        #         while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:  # make sure it is valid point
        #             P1PR = int(input('Please select an integer between 1-10: '))
        #             P1PC = int(input('Pick a column you think one of the opponents ship is on: '))  # player one point column
        #         while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:  # make sure it is valid point
        #             P1PC = int(input('Please select an integer between 1-10: '))
        #
        #         # verify that point hasn't been picked yet
        #         while SB1[P1PR - 1][P1PC - 1] != 0:  # if SB1 is not equal to 0 then point already picked
        #             print('\nYou have already picked that point\n\n')
        #             P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt user to pick again
        #             while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                 P1PR = int(input('Please select an integer between 1-10: '))
        #             P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                 P1PC = int(input('Please select an integer between 1-10: '))
        #
        #         # if player hits a ship
        #         while PB2[P1PR - 1][P1PC - 1] == 1 or PB2[P1PR - 1][P1PC - 1] == 2 or PB2[P1PR - 1][P1PC - 1] == 3 or PB2[P1PR - 1][P1PC - 1] == 4 or PB2[P1PR - 1][P1PC - 1] == 5:  # If he picks a point and ship is there
        #
        #             # check which ship it hit
        #             if PB2[P1PR - 1][P1PC - 1] == 1:  # I set the submarine points to one
        #                 HCA2[4] = HCA2[4] + 1
        #                 if HCA2[4] == 3:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe submarine has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 2:  # I set the patrol boat points to two
        #                 HCA2[3] = HCA2[3] + 1
        #                 if HCA2[3] == 2:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe patrol boat has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 3:  # I set the destroyer points to three
        #                 HCA2[2] = HCA2[2] + 1
        #                 if HCA2[2] == 3:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe destroyer has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 4:  # I set the battleship points to four
        #                 HCA2[1] = HCA2[1] + 1
        #                 if HCA2[1] == 4:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe battleship has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 5:  # I set the carrier point to five
        #                 HCA2[0] = HCA2[0] + 1
        #                 if HCA2[0] == 5:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe carrier has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #
        #             # if sum of hit counter list is 17, end the game
        #             if HCA2[0] + HCA2[1] + HCA2[2] + HCA2[3] + HCA2[4] == 17:
        #                 gameover = 1
        #                 # sound()
        #                 print('\nCongratulations player 1! YOU WON! You now have bragging rights over your opponent for the rest of your life!\n\n')
        #
        #             # if game is over, stop while loop
        #             if gameover == 1:
        #                 break
        #
        #             # prompt to keep choosing until a miss
        #             P1PR = int(input('Pick a row you think one of the opponents ship is on: '))
        #             while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                 P1PR = int(input('Please select an integer between 1-10: '))
        #             P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                 P1PC = int(input('Please select an integer between 1-10: '))
        #
        #             # check if point has already been picked
        #             while SB1[P1PR - 1][P1PC - 1] != 0:  # if secondary point not equal to 0 then point already picked
        #                 print('\nYou have already picked that point\n\n')
        #                 P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
        #                 while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                     P1PR = int(input('Please select an integer between 1-10: '))
        #                 P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #                 while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                     P1PC = int(input('Please select an integer between 1-10: '))
        #
        #         # if game is over, stop while loop
        #         if gameover == 1:
        #             break
        #
        #         # if player misses a ship
        #         if PB2[P1PR - 1][P1PC - 1] == 0:  # if he picks a point and there is no ship
        #
        #             # check if point has already been picked
        #             while SB1[P1PR - 1][P1PC - 1] != 0: # if the secondary point doesn't equal 0 then point already picked
        #                 print('\nYou have already picked that point\n\n')
        #                 P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
        #                 while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                     P1PR = int(input('Please select an integer between 1-10: '))
        #                 P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #                 while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                     P1PC = int(input('Please select an integer between 1-10: '))
        #             SB1[P1PR - 1][P1PC - 1] = -1  # set SB1 to -1 to show miss
        #             print('\nMISS!\n\n')
        #             # pretty_print_list(SB1)
        #
        #         # computer picking points
        #
        #         # computer plays based off difficulty
        #         if gameDifficulty == 1:  # easy difficulty
        #             P2PR = (randint(1, 10))
        #             P2PC = (randint(1, 10))
        #
        #             # check if point already picked
        #             while SB2[P2PR - 1][P2PC - 1] != 0:
        #                 P2PR = (randint(1, 10))
        #                 P2PC = (randint(1, 10))
        #
        #             # if computer hits ship
        #             while self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 5:
        #
        #                 # hit counter and sunk ship
        #                 if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1:
        #                     HCA1[4] = HCA1[4] + 1
        #                     if HCA1[4] == 3:  # if every point has been hit, ship is sunk
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your submarine\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2:
        #                     HCA1[3] = HCA1[3] + 1
        #                     if HCA1[3] == 2:  # if every point has been hit, ship is sunk
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your patrol boat\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3:
        #                     HCA1[2] = HCA1[2] + 1
        #                     if HCA1[2] == 3:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your destroyer\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4:
        #                     HCA1[1] = HCA1[1] + 1
        #                     if HCA1[1] == 4:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your battleship\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one(P2PR, P2PC)==5:
        #                     HCA1[0] = HCA1[0] + 1
        #                     if HCA1[0] == 5:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your carrier\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #
        #                 # if sum of hit counter list is 17, end the game
        #                 if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
        #                     gameover = 1
        #                     print('\nComputer wins! Better luck next time!\n\n')
        #
        #                 # if game is over, stop while loop
        #                 if gameover == 1:
        #                     break
        #
        #                 # prompt to choose until a miss
        #                 P2PR = (randint(1, 10))
        #                 P2PC = (randint(1, 10))
        #
        #                 # check if point has already been picked
        #                 while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point doesn't equal 0 then computer already picked that point
        #                     P2PR = (randint(1, 10)) # prompt computer to pick again
        #                     P2PC = (randint(1, 10))
        #
        #             # if game is over, stop while loop
        #             if gameover == 1:
        #                 break
        #
        #             # if computer misses a ship
        #             if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 0:  # if he picks point and there is no ship
        #
        #                 # check if point has already been picked
        #                 while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point doesn't equal 0 then computer already picked that point
        #                     P2PR = (randint(1, 10))  # prompt computer to pick again
        #                     P2PC = (randint(1, 10))
        #                 SB2[P2PR - 1][P2PC - 1] = -1  # set SB2 equal to -1 to show miss
        #                 print('\nComputer missed your ships!\n\n')
        #
        #         elif gameDifficulty == 2:  # pro difficulty (chooses points around it)
        #             P2PR = (randint(1, 10))
        #             P2PC = (randint(1, 10))
        #
        #             # check if point already picked
        #             while SB2[P2PR - 1][P2PC - 1] != 0:
        #                 P2PR = (randint(1, 10))  # prompt computer to pick again
        #                 P2PC = (randint(1, 10))
        #
        #             # if computer hits ship
        #             while self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 5:
        #
        #                 # hit counter and sunk ship
        #                 if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1:
        #                     HCA1[4] = HCA1[4] + 1
        #                     if HCA1[4] == 3:  # if every point hit, ship is sunk
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your submarine\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2:
        #                     HCA1[3] = HCA1[3] + 1
        #                     if HCA1[3] == 2:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your patrol boat\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one(P2PR, P2PC) == 3:
        #                     HCA1[2] = HCA1[2] + 1
        #                     if HCA1[2] == 3:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your destroyer\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4:
        #                     HCA1[1] = HCA1[1] + 1
        #                     if HCA1[1] == 4:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your battleship\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 5:
        #                     HCA1[0] = HCA1[0] + 1
        #                     if HCA1[0] == 5:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your carrier\n\n')
        #                     else:
        #                         self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                         SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #
        #                 # if sum of hit counter list is 17, end the game
        #                 if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
        #                     gameover = 1
        #                     print('\nComputer wins! Better luck next time!\n\n')
        #
        #                 # if game is over, stop while loop
        #                 if gameover == 1:
        #                     break
        #
        #                 # prompt to pick until miss
        #                 while self.primary_board_player_one[P2PR - 1][P2PC - 1] != 0:
        #                     RNG = (randint(1, 4))
        #                     if RNG == 1:
        #                         P2PC = P2PC + 1
        #                         while P2PC > 10:
        #                             P2PC = P2PC - 2
        #                             if P2PC > 10 or P2PC < 1:
        #                                 P2PR = (randint(1, 10))
        #                                 P2PC = (randint(1, 10))
        #                     elif RNG == 2:
        #                         P2PR = P2PR + 1
        #                         while P2PR > 10:
        #                             P2PR = P2PR - 2
        #                             if P2PR > 10 or P2PR < 1:
        #                                 P2PR = (randint(1, 10))
        #                                 P2PC = (randint(1, 10))
        #                     elif RNG == 3:
        #                         P2PR = P2PR - 1
        #                         while P2PR < 1:
        #                             P2PR = P2PR + 2
        #                             if P2PR > 10 or P2PR < 1:
        #                                 P2PR = (randint(1, 10))
        #                                 P2PC = (randint(1, 10))
        #                     elif RNG == 4:
        #                         P2PC = P2PC - 1
        #                         while P2PC < 1:
        #                             P2PC = P2PC + 2
        #                             if P2PC > 10 or P2PC < 1:
        #                                 P2PR = (randint(1, 10))
        #                                 P2PC = (randint(1, 10))
        #
        #                 # check if point already picked
        #                 while SB2[P2PR - 1][P2PC - 1] != 0:  # if point already picked, just randomly pick
        #                     P2PR = (randint(1, 10))
        #                     P2PC = (randint(1, 10))
        #
        #             # if sum of hit counter list is 17, end the game
        #             if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
        #                 gameover = 1
        #                 print('\nComputer wins! Better luck next time!\n\n')
        #
        #             # if game is over, stop while loop
        #             if gameover == 1:
        #                 break
        #
        #             # if computer misses ship
        #             if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 0:  # if he picks point and there is no ship
        #
        #                 # check if point already picked
        #                 while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point doesn't equal 0 then computer already picked that point
        #                     P2PR = (randint(1, 10))  # prompt computer to pick again
        #                     P2PC = (randint(1, 10))
        #                 SB2[P2PR - 1][P2PC - 1] = -1  # set secondary board equal to -1 to show miss
        #                 print('\nComputer missed your ships!\n\n')
        #
        #         elif gameDifficulty == 3:  # god mode difficulty (insta kill)
        #             P2PR = (randint(1, 10))
        #             P2PC = (randint(1, 10))
        #
        #             # check if point already picked
        #             while SB2[P2PR - 1][P2PC - 1] != 0:
        #                 P2PR = (randint(1, 10))  # prompt computer to pick again
        #                 P2PC = (randint(1, 10))
        #
        #             # if computer hits ship
        #             while self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 5:
        #
        #                 # set variable equal to ship that was hit
        #                 ship_hit = self.primary_board_player_one[P2PR - 1][P2PC - 1]
        #
        #                 # hit counter and sunk ship
        #                 if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1:
        #                     HCA1[4] = HCA1[4] + 1
        #                     if HCA1[4] == 3:  # if every point hit, ship is sunk
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your submarine\n\n')
        #                     else:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2:
        #                     HCA1[3] = HCA1[3] + 1
        #                     if HCA1[3] == 2:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your patrol boat\n\n')
        #                     else:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3:
        #                     HCA1[2] = HCA1[2] + 1
        #                     if HCA1[2] == 3:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your destroyer\n\n')
        #                     else:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4:
        #                     HCA1[1] = HCA1[1] + 1
        #                     if HCA1[1] == 4:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your battleship\n\n')
        #                     else:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #                 elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 5:
        #                     HCA1[0] = HCA1[0] + 1
        #                     if HCA1[0] == 5:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer sunk your carrier\n\n')
        #                     else:
        #                         # pretty_print_list(self.primary_board_player_one)
        #                         print('\nComputer got a hit\n\n')
        #
        #                 # change values of PB1 and SB2
        #                 self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to show ship been hit
        #                 SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to 1 to show hit
        #
        #                 # if sum of hit counter list is 17, end the game
        #                 if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
        #                     gameover = 1
        #                 print('\nComputer wins! Better luck next time!\n\n')
        #
        #                 # if game is over, stop while loop
        #                 if gameover == 1:
        #                     break
        #
        #                 # insta kill ship
        #                 for k in range(1, 11):
        #                     for h in range(1, 11):
        #                         if self.primary_board_player_one[k - 1][h - 1] == ship_hit:
        #                             if ship_hit == 1:
        #                                 HCA1[4] = HCA1[4] + 1
        #                                 self.primary_board_player_one[k - 1][h - 1] = 9
        #                                 if HCA1[4] == 3:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer sunk your submarine\n\n')
        #                                 else:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer got a hit\n\n')
        #                             elif ship_hit == 2:
        #                                 HCA1[3] = HCA1[3] + 1
        #                                 self.primary_board_player_one[k - 1][h - 1] = 9
        #                                 if HCA1[3] == 2:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer sunk your patrol boat\n\n')
        #                                 else:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer got a hit\n\n')
        #                             elif ship_hit == 3:
        #                                 HCA1[2] = HCA1[2] + 1
        #                                 self.primary_board_player_one[k - 1][h - 1] = 9
        #                                 if HCA1[2] == 3:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer sunk your destroyer\n\n')
        #                                 else:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer got a hit\n\n')
        #                             elif ship_hit == 4:
        #                                 HCA1[1] = HCA1[1] + 1
        #                                 self.primary_board_player_one[k - 1][h - 1] = 9
        #                                 if HCA1[1] == 4:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer sunk your battleship\n\n')
        #                                 else:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer got a hit\n\n')
        #                             elif ship_hit == 5:
        #                                 HCA1[0] = HCA1[0] + 1
        #                                 self.primary_board_player_one[k - 1][h - 1] = 9
        #                                 if HCA1[0] == 5:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer sunk your carrier\n\n')
        #                                 else:
        #                                     # pretty_print_list(self.primary_board_player_one)
        #                                     print('\nComputer got a hit\n\n')
        #                         SB2[k - 1][h - 1] = 1 # makes sure insta kill is covered on SB2
        #
        #                 # prompt to pick until miss
        #                 P2PR = (randint(1, 10))
        #                 P2PC = (randint(1, 10))
        #
        #                 # check if point already picked
        #                 while SB2[P2PR - 1][P2PC - 1] != 0:
        #                     P2PR = (randint(1, 10))
        #                     P2PC = (randint(1, 10))
        #
        #             # if sum of hit counter list is 17, end the game
        #             if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
        #                 gameover = 1
        #                 print('\nComputer wins! Better luck next time!\n\n')
        #
        #             # if game is over, stop while loop
        #             if gameover == 1:
        #                 break
        #
        #             # if computer misses ship
        #             if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 0:  # if he picks point and there is no ship
        #
        #                 # check if point already picked
        #                 while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point does not equal 0 then point already picked
        #                     P2PR = (randint(1, 10))  # prompt computer to pick again
        #                     P2PC = (randint(1, 10))
        #
        #                 SB2[P2PR - 1][P2PC - 1] = -1  # set secondary board to -1 to show miss
        #                 print('\nComputer missed your ships!\n\n')
        # else:
        #     # display rules for 2 player
        #     print('\nYou have chose to play against another player. \nTake turns choosing points on your opponents 10x10 board \nin hopes of hitting a part of the ship. \nIf you hit every part of the ship it will be sunk and \nyou will continue picking points until you sink all ships. \nThe first player to sink all opponent ships wins. \n\nGoodluck, Have fun! \n\n')
        #
        #     # player 1 picking points
        #
        #     # create primary board for player 1
        #     self.primary_board_player_one = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #
        #     # carrier
        #
        #     # horizontal or vertical axis
        #     CA1 = int(input('Specify whether you would like your carrier to be horizontal(1) or vertical(2): '))  # carrier axis player one
        #     while CA1 != 1 and CA1 != 2:
        #         CA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for carrier
        #     CR1 = int(input('Specify what row you would like to place the carrier: '))  # carrier row player one
        #     while CR1 != 1 and CR1 != 2 and CR1 != 3 and CR1 != 4 and CR1 != 5 and CR1 != 6 and CR1 != 7 and CR1 != 8 and CR1 != 9 and CR1 != 10:
        #         CR1 = int(input('Please select a number between 1-10: '))
        #     CC1 = int(input('Specify what column you would like to place the carrier: '))  # carrier column player one
        #     while CC1 != 1 and CC1 != 2 and CC1 != 3 and CC1 != 4 and CC1 != 5 and CC1 != 6 and CC1 != 7 and CC1 != 8 and CC1 != 9 and CC1 != 10:
        #         CC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify that the ship will fit and place points
        #     if CA1 == 1:
        #         while CC1 > 6 or CC1 <= 0 or CC1 % 1 != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             CR1 = int(input('Try a row integer that is between 1 and 6: '))
        #             CC1 = int(input('Try a column integer that is between 1 and 6: '))
        #         self.primary_board_player_one[CR1 - 1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1 + 1] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1 + 2] = 5
        #         self.primary_board_player_one[CR1 - 1][CC1 + 3] = 5
        #     else:
        #         while CR1 > 6 or CR1 <= 0 or CR1 % 1 != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             CR1 = int(input('Try a row integer that is between 1 and 6: '))
        #             CC1 = int(input('Try a column integer that is between 1 and 6: '))
        #         self.primary_board_player_one[CR1 - 1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 + 1][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 + 2][CC1 - 1] = 5
        #         self.primary_board_player_one[CR1 + 3][CC1 - 1] = 5
        #
        #     # display board after each ship placement
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your carrier has been placed \n\n')
        #
        #     # battleship
        #
        #     # horizontal or vertical axis
        #     BA1 = int(input('Specify whether you would like your battleship to be horizontal(1) or vertical(2): '))  # battleship axis player one
        #     while BA1 != 1 and BA1 != 2:
        #         BA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for battleship
        #     BR1 = int(input('Specify what row you would like to place the battleship: ')) # battleship row player one
        #     while BR1 != 1 and BR1 != 2 and BR1 != 3 and BR1 != 4 and BR1 != 5 and BR1 != 6 and BR1 != 7 and BR1 != 8 and BR1 != 9 and BR1 != 10:
        #         BR1 = int(input('Please select a number between 1-10: '))
        #     BC1 = int(input('Specify what column you would like to place the battleship: ')) # battleship column player one
        #     while BC1 != 1 and BC1 != 2 and BC1 != 3 and BC1 != 4 and BC1 != 5 and BC1 != 6 and BC1 != 7 and BC1 != 8 and BC1 != 9 and BC1 != 10:
        #         BC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if BA1 == 1:
        #         while BC1 > 7 or BC1 <= 0 or BC1 % 1 != 0 or self.primary_board_player_one[BR1 - 1][BC1 - 1] != 0 or self.primary_board_player_one[BR1 - 1][BC1] != 0 or self.primary_board_player_one[BR1 - 1][BC1 + 1] != 0 or self.primary_board_player_one[BR1 - 1][BC1 + 2] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             BR1 = int(input('Try a row integer that is between 1 and 7: '))
        #             BC1 = int(input('Try a column integer that is between 1 and 7: '))
        #         self.primary_board_player_one[BR1 - 1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1 - 1][BC1] = 4
        #         self.primary_board_player_one[BR1 - 1][BC1 + 1] = 4
        #         self.primary_board_player_one[BR1 - 1][BC1 + 2] = 4
        #     else:
        #         while BR1 > 7 or BR1 <= 0 or BR1 % 1 != 0 or self.primary_board_player_one[BR1 - 1][BC1 - 1] != 0 or self.primary_board_player_one[BR1][BC1 - 1] != 0 or self.primary_board_player_one[BR1 + 1][BC1 - 1] != 0 or self.primary_board_player_one[BR1 + 2][BC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             BR1 = int(input('Try a row integer that is between 1 and 7: '))
        #             BC1 = int(input('Try a column integer that is between 1 and 7: '))
        #         self.primary_board_player_one[BR1 - 1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1 + 1][BC1 - 1] = 4
        #         self.primary_board_player_one[BR1 + 2][BC1 - 1] = 4
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your battleship has been placed \n\n')
        #
        #     # destroyer
        #
        #     # horizontal or vertical axis
        #     DA1 = int(input('Specify whether you would like your destroyer to be horizontal(1) or vertical(2): '))  # destroyer axis player one
        #     while DA1 != 1 and DA1 != 2:
        #         DA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for destroyer
        #     DR1 = int(input('Specify what row you would like to place the destroyer: ')) # destroyer row player one
        #     while DR1 != 1 and DR1 != 2 and DR1 != 3 and DR1 != 4 and DR1 != 5 and DR1 != 6 and DR1 != 7 and DR1 != 8 and DR1 != 9 and DR1 != 10:
        #         DR1 = int(input('Please select a number between 1-10: '))
        #     DC1 = int(input('Specify what column you would like to place the destroyer: ')) # destroyer column player one
        #     while DC1 != 1 and DC1 != 2 and DC1 != 3 and DC1 != 4 and DC1 != 5 and DC1 != 6 and DC1 != 7 and DC1 != 8 and DC1 != 9 and DC1 != 10:
        #         DC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if DA1 == 1:
        #         while DC1 > 8 or DC1 < 0 or DC1 % 1 != 0 or self.primary_board_player_one[DR1 - 1][DC1 - 1] != 0 or self.primary_board_player_one[DR1 - 1][DC1] != 0 or self.primary_board_player_one[DR1 - 1][DC1 + 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             DR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             DC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[DR1 - 1][DC1 - 1] = 3
        #         self.primary_board_player_one[DR1 - 1][DC1] = 3
        #         self.primary_board_player_one[DR1 - 1][DC1 + 1] = 3
        #     else:
        #         while DR1 > 8 or DR1 < 0 or DR1 % 1 != 0 or self.primary_board_player_one[DR1 - 1][DC1 - 1] != 0 or self.primary_board_player_one[DR1][DC1 - 1] != 0 or self.primary_board_player_one[DR1 + 1][DC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             DR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             DC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[DR1 - 1][DC1 - 1] = 3
        #         self.primary_board_player_one[DR1][DC1 - 1] = 3
        #         self.primary_board_player_one[DR1 + 1][DC1 - 1] = 3
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your destroyer has been placed \n\n')
        #
        #     # submarine
        #
        #     # horizontal or vertical axis
        #     SA1 = int(input('Specify whether you would like your submarine to be horizontal(1) or vertical(2): ')) # submarine axis player one
        #     while SA1 != 1 and SA1 != 2:
        #         SA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for submarine
        #     SR1 = int(input('Specify what row you would like to place the submarine: ')) # submarine row player one
        #     while SR1 != 1 and SR1 != 2 and SR1 != 3 and SR1 != 4 and SR1 != 5 and SR1 != 6 and SR1 != 7 and SR1 != 8 and SR1 != 9 and SR1 != 10:
        #         SR1 = int(input('Please select a number between 1-10: '))
        #     SC1 = int(input('Specify what column you would like to place the submarine: ')) # submarine column player one
        #     while SC1 != 1 and SC1 != 2 and SC1 != 3 and SC1 != 4 and SC1 != 5 and SC1 != 6 and SC1 != 7 and SC1 != 8 and SC1 != 9 and SC1 != 10:
        #         SC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if SA1 == 1:
        #         while SC1 > 8 or SC1 < 0 or SC1 % 1 != 0 or self.primary_board_player_one[SR1 - 1][SC1 - 1] != 0 or self.primary_board_player_one[SR1 - 1][SC1] != 0 or self.primary_board_player_one[SR1 - 1][SC1 + 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             SR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             SC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[SR1 - 1][SC1 - 1] = 1
        #         self.primary_board_player_one[SR1 - 1][SC1] = 1
        #         self.primary_board_player_one[SR1 - 1][SC1 + 1] = 1
        #     else:
        #         while SR1 > 8 or SR1 < 0 or SR1 % 1 != 0 or self.primary_board_player_one[SR1 - 1][SC1 - 1] != 0 or self.primary_board_player_one[SR1][SC1 - 1] != 0 or self.primary_board_player_one[SR1 + 1][SC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             SR1 = int(input('Try a row integer that is between 1 and 8: '))
        #             SC1 = int(input('Try a column integer that is between 1 and 8: '))
        #         self.primary_board_player_one[SR1 - 1][SC1 - 1] = 1
        #         self.primary_board_player_one[SR1][SC1 - 1] = 1
        #         self.primary_board_player_one[SR1 + 1][SC1 - 1] = 1
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your submarine has been placed \n\n')
        #
        #     # patrol boat
        #
        #     # horizontal or vertical axis
        #     PA1 = int(input('Specify whether you would like your patrol boat to be horizontal(1) or vertical(2): ')) # patrol boat axis player one
        #     while PA1 != 1 and PA1 != 2:
        #         PA1 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 1 to assign location for patrol boat
        #     PR1 = int(input('Specify what row you would like to place the patrol boat: '))  # patrol boat row player one
        #     while PR1 != 1 and PR1 != 2 and PR1 != 3 and PR1 != 4 and PR1 != 5 and PR1 != 6 and PR1 != 7 and PR1 != 8 and PR1 != 9 and PR1 != 10:
        #         PR1 = int(input('Please select a number between 1-10: '))
        #     PC1 = int(input('Specify what column you would like to place the patrol boat: '))  # patrol boat column player one
        #     while PC1 != 1 and PC1 != 2 and PC1 != 3 and PC1 != 4 and PC1 != 5 and PC1 != 6 and PC1 != 7 and PC1 != 8 and PC1 != 9 and PC1 != 10:
        #         PC1 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if PA1 == 1:
        #         while PC1 > 9 or PC1 < 0 or PC1 % 1 != 0 or self.primary_board_player_one[PR1 - 1][PC1 - 1] != 0 or self.primary_board_player_one[PR1 - 1][PC1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             PR1 = int(input('Try a row integer that is between 1 and 9: '))
        #             PC1 = int(input('Try a column integer that is between 1 and 9: '))
        #         self.primary_board_player_one[PR1 - 1][PC1 - 1] = 2
        #         self.primary_board_player_one[PR1 - 1][PC1] = 2
        #     else:
        #         while PR1 > 9 or PR1 < 0 or PR1 % 1 != 0 or self.primary_board_player_one[PR1 - 1][PC1 - 1] != 0 or self.primary_board_player_one[PR1][PC1 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             PR1 = int(input('Try a row integer that is between 1 and 9: '))
        #             PC1 = int(input('Try a column integer that is between 1 and 9: '))
        #         self.primary_board_player_one[PR1 - 1][PC1 - 1] = 2
        #         self.primary_board_player_one[PR1][PC1 - 1] = 2
        #
        #     # display the board
        #     # pretty_print_list(self.primary_board_player_one)
        #     print('Your patrol boat has been placed \n\n')
        #
        #     # clear (clears the output)
        #
        #     # switch to player 2 so he can pick ship placement
        #     print('Now that player 1 has finished placing his ships, it is your turn player 2!\n\n')
        #
        #     # create primary board player 2
        #     PB2 = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #
        #     # horizontal or vertical axis
        #     CA2 = int(input('Specify whether you would like your carrier to be horizontal(1) or vertical(2): '))  # carrier axis player two
        #     while CA2 != 1 and CA2 != 2:
        #         CA2 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 2 to assign location for carrier
        #     CR2 = int(input('Specify what row you would like to place the carrier: '))  # carrier row player two
        #     while CR2 != 1 and CR2 != 2 and CR2 != 3 and CR2 != 4 and CR2 != 5 and CR2 != 6 and CR2 != 7 and CR2 != 8 and CR2 != 9 and CR2 != 10:
        #         CR2 = int(input('Please select a number between 1-10: '))
        #     CC2 = int(input('Specify what column you would like to place the carrier: '))  # carrier column player two
        #     while CC2 != 1 and CC2 != 2 and CC2 != 3 and CC2 != 4 and CC2 != 5 and CC2 != 6 and CC2 != 7 and CC2 != 8 and CC2 != 9 and CC2 != 10:
        #         CC2 = int(input('Please select a number between 1-10: '))
        #
        #     # verify that the ship will fit and place points
        #     if CA2 == 1:
        #         while CC2 > 6 or CC2 <= 0 or CC2 % 1 != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             CR2 = int(input('Try a row integer that is between 1 and 6: '))
        #             CC2 = int(input('Try a column integer that is between 1 and 6: '))
        #         PB2[CR2 - 1][CC2 - 1] = 5
        #         PB2[CR2 - 1][CC2] = 5
        #         PB2[CR2 - 1][CC2 + 1] = 5
        #         PB2[CR2 - 1][CC2 + 2] = 5
        #         PB2[CR2 - 1][CC2 + 3] = 5
        #     else:
        #         while CR2 > 6 or CR2 <= 0 or CR2 % 1 != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             CR2 = int(input('Try a row integer that is between 1 and 6: '))
        #             CC2 = int(input('Try a column integer that is between 1 and 6: '))
        #         PB2[CR2 - 1][CC2 - 1] = 5
        #         PB2[CR2][CC2 - 1] = 5
        #         PB2[CR2 + 1][CC2 - 1] = 5
        #         PB2[CR2 + 2][CC2 - 1] = 5
        #         PB2[CR2 + 3][CC2 - 1] = 5
        #
        #     # display board
        #     # pretty_print_list(PB2)
        #     print('Your carrier has been placed \n\n')
        #
        #     # battleship
        #
        #     # horizontal or vertical axis
        #     BA2 = int(input('Specify whether you would like your battleship to be horizontal(1) or vertical(2): '))  # battleship axis player two
        #     while BA2 != 1 and BA2 != 2:
        #         BA2 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 2 to assign location for battleship
        #     BR2 = int(input('Specify what row you would like to place the battleship: ')) # battleship row player two
        #     while BR2 != 1 and BR2 != 2 and BR2 != 3 and BR2 != 4 and BR2 != 5 and BR2 != 6 and BR2 != 7 and BR2 != 8 and BR2 != 9 and BR2 != 10:
        #         BR2 = int(input('Please select a number between 1-10: '))
        #     BC2 = int(input('Specify what column you would like to place the battleship: ')) # battleship column player two
        #     while BC2 != 1 and BC2 != 2 and BC2 != 3 and BC2 != 4 and BC2 != 5 and BC2 != 6 and BC2 != 7 and BC2 != 8 and BC2 != 9 and BC2 != 10:
        #         BC2 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if BA2 == 1:
        #         while BC2 > 7 or BC2 <= 0 or BC2 % 1 != 0 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2 - 1][BC2] != 0 or PB2[BR2 - 1][BC2 + 1] != 0 or PB2[BR2 - 1][BC2 + 2] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             BR2 = int(input('Try a row integer that is between 1 and 7: '))
        #             BC2 = int(input('Try a column integer that is between 1 and 7: '))
        #         PB2[BR2 - 1][BC2 - 1] = 4
        #         PB2[BR2 - 1][BC2] = 4
        #         PB2[BR2 - 1][BC2 + 1] = 4
        #         PB2[BR2 - 1][BC2 + 2] = 4
        #     else:
        #         while BR2 > 7 or BR2 <= 0 or BR2 % 1 != 0 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2][BC2 - 1] != 0 or PB2[BR2 + 1][BC2 - 1] != 0 or PB2[BR2 + 2][BC2 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             BR2 = int(input('Try a row integer that is between 1 and 7: '))
        #             BC2 = int(input('Try a column integer that is between 1 and 7: '))
        #         PB2[BR2 - 1][BC2 - 1] = 4
        #         PB2[BR2][BC2 - 1] = 4
        #         PB2[BR2 + 1][BC2 - 1] = 4
        #         PB2[BR2 + 2][BC2 - 1] = 4
        #
        #     # display the board
        #     # pretty_print_list(PB2)
        #     print('Your battleship has been placed \n\n')
        #
        #     # destroyer
        #
        #     # horizontal or vertical axis
        #     DA2 = int(input('Specify whether you would like your destroyer to be horizontal(1) or vertical(2): '))  # destroyer axis player two
        #     while DA2 != 1 and DA2 != 2:
        #         DA2 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 2 to assign location for destroyer
        #     DR2 = int(input('Specify what row you would like to place the destroyer: '))  # destroyer row player two
        #     while DR2 != 1 and DR2 != 2 and DR2 != 3 and DR2 != 4 and DR2 != 5 and DR2 != 6 and DR2 != 7 and DR2 != 8 and DR2 != 9 and DR2 != 10:
        #         DR2 = int(input('Please select a number between 1-10: '))
        #     DC2 = int(input('Specify what column you would like to place the destroyer: '))  # destroyer column player two
        #     while DC2 != 1 and DC2 != 2 and DC2 != 3 and DC2 != 4 and DC2 != 5 and DC2 != 6 and DC2 != 7 and DC2 != 8 and DC2 != 9 and DC2 != 10:
        #         DC2 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if DA2 == 1:
        #         while DC2 > 8 or DC2 < 0 or DC2 % 1 != 0 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2 - 1][DC2] != 0 or PB2[DR2 - 1][DC2 + 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             DR2 = int(input('Try a row integer that is between 1 and 8: '))
        #             DC2 = int(input('Try a column integer that is between 1 and 8: '))
        #         PB2[DR2 - 1][DC2 - 1] = 3
        #         PB2[DR2 - 1][DC2] = 3
        #         PB2[DR2 - 1][DC2 + 1] = 3
        #     else:
        #         while DR2 > 8 or DR2 < 0 or DR2 % 1 != 0 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2][DC2 - 1] != 0 or PB2[DR2 + 1][DC2 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             DR2 = int(input('Try a row integer that is between 1 and 8: '))
        #             DC2 = int(input('Try a column integer that is between 1 and 8: '))
        #         PB2[DR2 - 1][DC2 - 1] = 3
        #         PB2[DR2][DC2 - 1] = 3
        #         PB2[DR2 + 1][DC2 - 1] = 3
        #
        #     # display the board
        #     # pretty_print_list(PB2)
        #     print('Your destroyer has been placed \n\n')
        #
        #     # submarine
        #
        #     # horizontal or vertical axis
        #     SA2 = int(input('Specify whether you would like your submarine to be horizontal(1) or vertical(2): '))  # submarine axis player two
        #     while SA2 != 1 and SA2 != 2:
        #         SA2 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 2 to assign location for submarine
        #     SR2 = int(input('Specify what row you would like to place the submarine: '))  # submarine row player two
        #     while SR2 != 1 and SR2 != 2 and SR2 != 3 and SR2 != 4 and SR2 != 5 and SR2 != 6 and SR2 != 7 and SR2 != 8 and SR2 != 9 and SR2 != 10:
        #         SR2 = int(input('Please select a number between 1-10: '))
        #     SC2 = int(input('Specify what column you would like to place the submarine: '))  # submarine column player two
        #     while SC2 != 1 and SC2 != 2 and SC2 != 3 and SC2 != 4 and SC2 != 5 and SC2 != 6 and SC2 != 7 and SC2 != 8 and SC2 != 9 and SC2 != 10:
        #         SC2 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if SA2 == 1:
        #         while SC2 > 8 or SC2 < 0 or SC2 % 1 != 0 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2 - 1][SC2] != 0 or PB2[SR2 - 1][SC2 + 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             SR2 = int(input('Try a row integer that is between 1 and 8: '))
        #             SC2 = int(input('Try a column integer that is between 1 and 8: '))
        #         PB2[SR2 - 1][SC2 - 1] = 1
        #         PB2[SR2 - 1][SC2] = 1
        #         PB2[SR2 - 1][SC2 + 1] = 1
        #     else:
        #         while SR2 > 8 or SR2 < 0 or SR2 % 1 != 0 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2][SC2 - 1] != 0 or PB2[SR2 + 1][SC2 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             SR2 = int(input('Try a row integer that is between 1 and 8: '))
        #             SC2 = int(input('Try a column integer that is between 1 and 8: '))
        #         PB2[SR2 - 1][SC2 - 1] = 1
        #         PB2[SR2][SC2 - 1] = 1
        #         PB2[SR2 + 1][SC2 - 1] = 1
        #
        #     # display the board
        #     # pretty_print_list(PB2)
        #     print('Your submarine has been placed \n\n')
        #
        #     # patrol boat
        #
        #     # horizontal or vertical axis
        #     PA2 = int(input('Specify whether you would like your patrol boat to be horizontal(1) or vertical(2): ')) # patrol boat axis player two
        #     while PA2 != 1 and PA2 != 2:
        #         PA2 = int(input('Please select either 1 or 2: '))
        #
        #     # ask player 2 to assign location for patrol boat
        #     PR2 = int(input('Specify what row you would like to place the patrol boat: '))  # patrol boat row player two
        #     while PR2 != 1 and PR2 != 2 and PR2 != 3 and PR2 != 4 and PR2 != 5 and PR2 != 6 and PR2 != 7 and PR2 != 8 and PR2 != 9 and PR2 != 10:
        #         PR2 = int(input('Please select a number between 1-10: '))
        #     PC2 = int(input('Specify what column you would like to place the patrol boat: '))  # patrol boat column player two
        #     while PC2 != 1 and PC2 != 2 and PC2 != 3 and PC2 != 4 and PC2 != 5 and PC2 != 6 and PC2 != 7 and PC2 != 8 and PC2 != 9 and PC2 != 10:
        #         PC2 = int(input('Please select a number between 1-10: '))
        #
        #     # verify ship will fit and place points
        #     if PA2 == 1:
        #         while PC2 > 9 or PC2 < 0 or PC2 % 1 != 0 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2 - 1][PC2] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             PR2 = int(input('Try a row integer that is between 1 and 9: '))
        #             PC2 = int(input('Try a column integer that is between 1 and 9: '))
        #         PB2[PR2 - 1][PC2 - 1] = 2
        #         PB2[PR2 - 1][PC2] = 2
        #     else:
        #         while PR2 > 9 or PR2 < 0 or PR2 % 1 != 0 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2][PC2 - 1] != 0:
        #             print('\nThis ship cannot fit in the location you have chosen.\n\n')
        #             PR2 = int(input('Try a row integer that is between 1 and 9: '))
        #             PC2 = int(input('Try a column integer that is between 1 and 9: '))
        #         PB2[PR2 - 1][PC2 - 1] = 2
        #         PB2[PR2][PC2 - 1] = 2
        #
        #     # display the board
        #     # pretty_print_list(PB2)
        #     print('Your patrol boat has been placed \n\n')
        #
        #     # clear (clears the output)
        #
        #     # create secondary board for player 1 and 2
        #     SB1 = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #     SB2 = [
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     ]
        #
        #     # create hit counter for each ship
        #
        #     # list of hit counters
        #     HCA1 = [0, 0, 0, 0, 0]
        #     HCA2 = [0, 0, 0, 0, 0]
        #     # 5,4,3,2,1 (5 = carrier, 4 = battleship, 3 = destroyer, 2 = patrol boat, 1 = submarine)
        #
        #     # create while loop so game continues until someone wins
        #     gameover = 0
        #     while gameover == 0:
        #
        #         # player 1 picks a point
        #         print('\nIT IS YOUR TURN PLAYER 1\n\n')
        #         P1PR = int(input('Pick a row you think one of the opponents ship is on: '))  # player one point row
        #         while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:  # make sure it is valid point
        #             P1PR = int(input('Please select an integer between 1-10: '))
        #             P1PC = int(input('Pick a column you think one of the opponents ship is on: '))  # player one point column
        #         while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:  # make sure it is valid point
        #             P1PC = int(input('Please select an integer between 1-10: '))
        #
        #         # verify that point hasn't been picked yet
        #         while SB1[P1PR - 1][P1PC - 1] != 0:  # if SB1 is not equal to 0 then point already picked
        #             print('\nYou have already picked that point\n\n')
        #             P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt user to pick again
        #             while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                 P1PR = int(input('Please select an integer between 1-10: '))
        #             P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                 P1PC = int(input('Please select an integer between 1-10: '))
        #
        #         # if player hits a ship
        #         while PB2[P1PR - 1][P1PC - 1] == 1 or PB2[P1PR - 1][P1PC - 1] == 2 or PB2[P1PR - 1][P1PC - 1] == 3 or PB2[P1PR - 1][P1PC - 1] == 4 or PB2[P1PR - 1][P1PC - 1] == 5:  # If he picks a point and ship is there
        #
        #             # check which ship it hit
        #             if PB2[P1PR - 1][P1PC - 1] == 1:  # I set the submarine points to one
        #                 HCA2[4] = HCA2[4] + 1
        #                 if HCA2[4] == 3:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe submarine has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 2:  # I set the patrol boat points to two
        #                 HCA2[3] = HCA2[3] + 1
        #                 if HCA2[3] == 2:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe patrol boat has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 3:  # I set the destroyer points to three
        #                 HCA2[2] = HCA2[2] + 1
        #                 if HCA2[2] == 3:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe destroyer has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 4:  # I set the battleship points to four
        #                 HCA2[1] = HCA2[1] + 1
        #                 if HCA2[1] == 4:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe battleship has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #             elif PB2[P1PR - 1][P1PC - 1] == 5:  # I set the carrier point to five
        #                 HCA2[0] = HCA2[0] + 1
        #                 if HCA2[0] == 5:  # if every point has been hit, the ship is sunk
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nThe carrier has been sunk!\n\n')
        #                 else:
        #                     PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
        #                     SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
        #                     # pretty_print_list(SB1)
        #                     print('\nHIT\n\n')
        #
        #             # if sum of hit counter list is 17, end the game
        #             if HCA2[0] + HCA2[1] + HCA2[2] + HCA2[3] + HCA2[4] == 17:
        #                 gameover = 1
        #                 # sound()
        #                 print('\nCongratulations player 1! YOU WON! You now have bragging rights over player 2 for the rest of your life!\n\n')
        #
        #             # if game is over, stop while loop
        #             if gameover == 1:
        #                 break
        #
        #             # prompt to keep choosing until a miss
        #             P1PR = int(input('Pick a row you think one of the opponents ship is on: '))
        #             while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                 P1PR = int(input('Please select an integer between 1-10: '))
        #             P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                 P1PC = int(input('Please select an integer between 1-10: '))
        #
        #             # check if point has already been picked
        #             while SB1[P1PR - 1][P1PC - 1] != 0:  # if secondary point not equal to 0 then point already picked
        #                 print('\nYou have already picked that point\n\n')
        #                 P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
        #                 while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                     P1PR = int(input('Please select an integer between 1-10: '))
        #                 P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #                 while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                     P1PC = int(input('Please select an integer between 1-10: '))
        #
        #         # if player misses a ship
        #         if PB2[P1PR - 1][P1PC - 1] == 0:  # if he picks a point and there is no ship
        #
        #             # check if point has already been picked
        #             while SB1[P1PR - 1][P1PC - 1] != 0: # if the secondary point doesn't equal 0 then point already picked
        #                 print('\nYou have already picked that point\n\n')
        #                 P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
        #                 while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
        #                     P1PR = int(input('Please select an integer between 1-10: '))
        #                 P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #                 while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
        #                     P1PC = int(input('Please select an integer between 1-10: '))
        #             SB1[P1PR - 1][P1PC - 1] = -1  # set SB1 to -1 to show miss
        #             print('\nMISS!\n\n')
        #             # pretty_print_list(SB1)
        #
        #         # tell player 2 to pick a point
        #         if gameover == 1:
        #             break
        #         print('\nIT IS YOUR TURN PLAYER 2\n\n')
        #         P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # player two point row
        #         while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:  # make sure valid point
        #             P2PR = int(input('Please select an integer between 1-10: '))
        #         P2PC = int(input('Pick a column you think one of the opponents ship is on: '))  # player two point column
        #         while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:  # make sure valid point
        #             P2PC = int(input('Please select an integer between 1-10: '))
        #
        #         # check if point already picked
        #         while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point not equal to 0 then he already picked that point
        #             print('\nYou have already picked that point\n\n')
        #             P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # prompt to pick again
        #             while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
        #                 P2PR = int(input('Please select an integer between 1-10: '))
        #             P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
        #                 P2PC = int(input('Please select an integer between 1-10: '))
        #
        #         # if player 2 hits ship
        #         while self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4 or self.primary_board_player_one[P2PR - 1][P2PC - 1] == 5:
        #
        #             # hit counter and sunk ship
        #             if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 1:
        #                 HCA1[4] = HCA1[4] + 1
        #                 if HCA1[4] == 3:  # if every point has been hit, ship is sunk
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 sunk player 1 submarine \n\n')
        #                 else:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 got a hit\n\n')
        #             elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 2:
        #                 HCA1[3] = HCA1[3] + 1
        #                 if HCA1[3] == 2:  # if every point has been hit, ship is sunk
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 sunk player 1 patrol boat\n\n')
        #                 else:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 got a hit\n\n')
        #             elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 3:
        #                 HCA1[2] = HCA1[2] + 1
        #                 if HCA1[2] == 3:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 sunk player 1 destroyer\n\n')
        #                 else:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 got a hit\n\n')
        #             elif self.primary_board_player_one[P2PR - 1][P2PC - 1] == 4:
        #                 HCA1[1] = HCA1[1] + 1
        #                 if HCA1[1] == 4:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 sunk player 1 battleship\n\n')
        #                 else:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 got a hit\n\n')
        #             elif self.primary_board_player_one(P2PR, P2PC)==5:
        #                 HCA1[0] = HCA1[0] + 1
        #                 if HCA1[0] == 5:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 sunk player 1 carrier\n\n')
        #                 else:
        #                     self.primary_board_player_one[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
        #                     SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
        #                     # pretty_print_list(self.primary_board_player_one)
        #                     print('\nPlayer 2 got a hit\n\n')
        #
        #             # if sum of hit counter list is 17, end the game
        #             if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
        #                 gameover = 1
        #                 print('\nCongratulations player 2! YOU WON! You now have bragging rights over player 1 for the rest of your life!\n\n')
        #
        #             # if game is over, stop while loop
        #             if gameover == 1:
        #                 break
        #
        #             # prompt to keep choosing until miss
        #             P2PR = int(input('Pick a row you think one of the opponents ship is on: '))
        #             while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
        #                 P2PR = int(input('Please select an integer between 1-10: '))
        #             P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
        #                 P2PC = int(input('Please select an integer between 1-10: '))
        #
        #             # check if point already picked
        #             while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point not equal to 0 then already picked point
        #                 print('\nYou have already picked that point\n\n')
        #                 P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # prompt to pick again
        #                 while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
        #                     P2PR = int(input('Please select an integer between 1-10: '))
        #                 P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #                 while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
        #                     P2PC = int(input('Please select an integer between 1-10: '))
        #
        #             SB2[P2PR - 1][P2PC - 1] = -1  # set secondary board equal to -1 to show miss
        #             print('\nMISS!\n\n')
        #             # pretty_print_list(SB2)
        #
        #         # if player misses ship
        #         if self.primary_board_player_one[P2PR - 1][P2PC - 1] == 0:  # if he picks point and no ship
        #
        #             # check if point already picked
        #             while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point not equal to 0 then point already picked
        #                 print('\nYou have already picked that point\n\n')
        #                 P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # prompt to pick again
        #             while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
        #                 P2PR = int(input('Please select an integer between 1-10: '))
        #             P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
        #             while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
        #                 P2PC = int(input('Please select an integer between 1-10: '))
        #
        #             SB2[P2PR - 1][P2PC - 1] = -1  # secondary board 10 -1 to show miss
        #             print('\nMISS!\n\n')
        #             # pretty_print_list(SB2)


