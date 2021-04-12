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
            self.carrier.validate_carrier_computer_points(self.config)
            self.cruiser.validate_cruiser_computer_points(self.config)
            self.destroyer.validate_destroyer_computer_points(self.config)
            self.patrol_boat.validate_patrol_boat_computer_points(self.config)
            self.submarine.validate_submarine_computer_points(self.config)
        else:
            self.game_difficulty = self.constants.get_constant_values('easy_difficulty')
            self.opponent_type = self.constants.get_constant_values('computer_opponent')

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
        if self.game_difficulty != self.constants.get_constant_values('easy_difficulty') and \
                self.game_difficulty != self.constants.get_constant_values('normal_difficulty') and \
                self.game_difficulty != self.constants.get_constant_values('god_difficulty'):
            self.game_difficulty = self.constants.get_constant_values('easy_difficulty')
            print('You have selected an invalid choice for game difficulty.' +
                  '\nThe game difficulty has defaulted to easy.' +
                  '\nNext time try to choose a value that is valid.')
            self.constants.validation_flag_game = False
        return self.constants.validation_flag_game

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
