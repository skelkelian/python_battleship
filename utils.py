class Constants:
    def __init__(self):
        # OPPONENT TYPE
        self.COMPUTER_OPPONENT = 1
        self.PLAYER_OPPONENT = 2

        # GAME DIFFICULTY
        self.EASY_DIFFICULTY = 1
        self.NORMAL_DIFFICULTY = 2
        self.GOD_DIFFICULTY = 3

        # SHIP IDENTIFICATION
        self.CARRIER = 5
        self.BATTLESHIP = 4
        self.DESTROYER = 3
        self.PATROL_BOAT = 2
        self.SUBMARINE = 1

        # AXIS
        self.HORIZONTAL_AXIS = 1
        self.VERTICAL_AXIS = 2

        # HIT COUNTER
        self.HIT_COUNTER_PLAYER_ONE = [0, 0, 0, 0, 0]  # when computer hits a ship adjust this hit counter
        self.HIT_COUNTER_COMPUTER = [0, 0, 0, 0, 0]  # when player hits a ship adjust this hit counter
        # if sum of hit counters is 17 then game is over
        # 5,4,3,2,1 [5 = carrier, 4 = battleship, 3 = destroyer, 2 = patrol boat, 1 = submarine]
        # [carrier_max = 5, battleship_max = 4 , destroyer_max = 3, patrol_boat_max = 2, submarine_max = 3]

        # VALIDATION PLAYER
        self.validation_flag_game = True
        self.validation_flag_carrier_player = True
        self.validation_flag_battleship_player = True
        self.validation_flag_destroyer_player = True
        self.validation_flag_patrol_boat_player = True
        self.validation_flag_submarine_player = True
        self.validation_flag_battleship_overlap_player = True
        self.validation_flag_destroyer_overlap_player = True
        self.validation_flag_patrol_boat_overlap_player = True
        self.validation_flag_submarine_overlap_player = True
        self.validation_flag_hit_or_miss_player = True
        self.validation_flag_hit_counter_player = True
        self.validation_flag_ship_sunk_carrier_player = False
        self.validation_flag_ship_sunk_battleship_player = False
        self.validation_flag_ship_sunk_destroyer_player = False
        self.validation_flag_ship_sunk_patrol_boat_player = False
        self.validation_flag_ship_sunk_submarine_player = False
        self.validation_flag_game_over_player = False

        # VALIDATION COMPUTER
        self.validation_flag_carrier_computer = True
        self.validation_flag_battleship_computer = True
        self.validation_flag_destroyer_computer = True
        self.validation_flag_patrol_boat_computer = True
        self.validation_flag_submarine_computer = True
        self.validation_flag_battleship_overlap_computer = True
        self.validation_flag_destroyer_overlap_computer = True
        self.validation_flag_patrol_boat_overlap_computer = True
        self.validation_flag_submarine_overlap_computer = True



