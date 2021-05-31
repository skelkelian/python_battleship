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
from participant import Participant
import utils


class BattleShip:
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
        self.validation_flag_game = self.constants.get_constant_values('validation_flag_game')
        self.validation_flag_hit_or_miss_player = self.constants.get_constant_values('validation_flag_hit_or_miss_player')
        self.validation_flag_hit_or_miss_computer = self.constants.get_constant_values('validation_flag_hit_or_miss_computer')
        self.carrier = Carrier(config_name)
        self.cruiser = Cruiser(config_name)
        self.destroyer = Destroyer(config_name)
        self.patrol_boat = Patrol_Boat(config_name)
        self.submarine = Submarine(config_name)
        self.ship = Ship()
        self.player = Player()
        self.computer = Computer()

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
            self.carrier.validate_carrier_points()
            self.cruiser.validate_cruiser_points()
            self.destroyer.validate_destroyer_points()
            self.patrol_boat.validate_patrol_boat_points()
            self.submarine.validate_submarine_points()

            # COMPUTER
            self.carrier.validate_carrier_computer_points()
            self.cruiser.validate_cruiser_computer_points()
            self.destroyer.validate_destroyer_computer_points()
            self.patrol_boat.validate_patrol_boat_computer_points()
            self.submarine.validate_submarine_computer_points()
        else:
            self.game_difficulty = self.constants.get_constant_values('easy_difficulty')
            self.opponent_type = self.constants.get_constant_values('computer_opponent')

    def get_opponent_type(self):
        return self.opponent_type

    def get_game_difficulty(self):
        return self.game_difficulty

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
            self.validation_flag_game = False
        return self.validation_flag_game

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

    def place_all_ships(self):
        self.player.update_primary_board_player_one("carrier", self.carrier.get_carrier_values_player_one())
        self.player.update_primary_board_player_one("cruiser", self.cruiser.get_cruiser_values_player_one())
        self.player.update_primary_board_player_one("destroyer", self.destroyer.get_destroyer_values_player_one())
        self.player.update_primary_board_player_one("patrol_boat", self.patrol_boat.get_patrol_boat_values_player_one())
        self.player.update_primary_board_player_one("submarine", self.submarine.get_submarine_values_player_one())
        self.computer.update_primary_board_computer("carrier", self.carrier.get_carrier_values_computer())
        self.computer.update_primary_board_computer("cruiser", self.cruiser.get_cruiser_values_computer())
        self.computer.update_primary_board_computer("destroyer", self.destroyer.get_destroyer_values_computer())
        self.computer.update_primary_board_computer("patrol_boat", self.patrol_boat.get_patrol_boat_values_computer())
        self.computer.update_primary_board_computer("submarine", self.submarine.get_submarine_values_computer())

    def validate_all_ships(self):
        self.cruiser.validate_cruiser_overlap()
        self.destroyer.validate_destroyer_overlap()
        self.patrol_boat.validate_patrol_boat_overlap()
        self.submarine.validate_submarine_overlap()
        self.cruiser.validate_cruiser_computer_overlap()
        self.destroyer.validate_destroyer_computer_overlap()
        self.patrol_boat.validate_patrol_boat_computer_overlap()
        self.submarine.validate_submarine_computer_overlap()

    def start_game(self):
        self.place_all_ships()
        self.validate_all_ships()

    def play_game(self):
        game_over = False
        while game_over == False:
            self.start_game()
            self.participant.pick_point()
            self.player.hit_or_miss_player()
            while self.validation_flag_hit_or_miss_player is True:
                self.computer.get_hit_counter_computer()
                self.carrier.ship_sunk_carrier_computer(self.computer.get_hit_counter_computer)
                self.cruiser.ship_sunk_cruiser_computer(self.computer.get_hit_counter_computer)
                self.destroyer.ship_sunk_destroyer_computer(self.computer.get_hit_counter_computer)
                self.patrol_boat.ship_sunk_patrol_boat_computer(self.computer.get_hit_counter_computer)
                self.submarine.ship_sunk_submarine_computer(self.computer.get_hit_counter_computer)
                self.computer.game_over_computer()
                # if game is over change game_over to true and stop the game
            self.computer.hit_or_miss_computer()
            while self.validation_flag_hit_or_miss_computer is True:
                self.player.get_hit_counter_player()
                self.carrier.ship_sunk_carrier_player(self.player.get_hit_counter_player)
                self.cruiser.ship_sunk_cruiser_player(self.player.get_hit_counter_player)
                self.destroyer.ship_sunk_destroyer_player(self.player.get_hit_counter_player)
                self.patrol_boat.ship_sunk_patrol_boat_player(self.player.get_hit_counter_player)
                self.submarine.ship_sunk_submarine_player(self.player.get_hit_counter_player)
                self.player.game_over_player()
                # if game is over change game_over to true and stop the game

