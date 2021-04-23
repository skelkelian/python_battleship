import psycopg2
import sys


class Constants:

    def __init__(self):
        self.constants = dict()
        self.set_constants_from_database(host='localhost', dbname='skelkelian')

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
        # 5,4,3,2,1 [5 = carrier, 4 = cruiser, 3 = destroyer, 2 = patrol boat, 1 = submarine]
        # [carrier_max = 5, cruiser_max = 4 , destroyer_max = 3, patrol_boat_max = 2, submarine_max = 3]

        # VALIDATION PLAYER
        self.validation_flag_game = True
        self.validation_flag_carrier_player = True
        self.validation_flag_cruiser_player = True
        self.validation_flag_destroyer_player = True
        self.validation_flag_patrol_boat_player = True
        self.validation_flag_submarine_player = True
        self.validation_flag_cruiser_overlap_player = True
        self.validation_flag_destroyer_overlap_player = True
        self.validation_flag_patrol_boat_overlap_player = True
        self.validation_flag_submarine_overlap_player = True
        self.validation_flag_hit_or_miss_player = True
        self.validation_flag_hit_counter_player = True
        self.validation_flag_ship_sunk_carrier_player = False
        self.validation_flag_ship_sunk_cruiser_player = False
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
        self.validation_flag_cruiser_overlap_computer = True
        self.validation_flag_destroyer_overlap_computer = True
        self.validation_flag_patrol_boat_overlap_computer = True
        self.validation_flag_submarine_overlap_computer = True
        self.validation_flag_hit_or_miss_computer = True
        self.validation_flag_hit_counter_computer = True
        self.validation_flag_ship_sunk_carrier_computer = False
        self.validation_flag_ship_sunk_cruiser_computer = False
        self.validation_flag_ship_sunk_destroyer_computer = False
        self.validation_flag_ship_sunk_patrol_boat_computer = False
        self.validation_flag_ship_sunk_submarine_computer = False
        self.validation_flag_game_over_computer = False

    def get_constants(self):
        return self.constants

    def set_constants_from_database(self, host='localhost', dbname='skelkelian'):
        try:
            con = psycopg2.connect("host=" + host + " dbname=" + dbname)
            cur = con.cursor()
            cur.execute("SELECT * FROM battleship_constants")

            while True:
                row = cur.fetchone()

                if row == None:
                    break

                constant = row[0]
                datatype = row[1]
                value = row[2]

                if datatype == 'int':
                    value = int(value)
                elif datatype == 'bool':
                    if value == 'True':
                        value = True
                    else:
                        value = False
                else:
                    type_casted_list = []
                    for i in value.split(', '):
                        i = int(i)
                        type_casted_list.append(i)
                    value = type_casted_list

                self.constants[constant] = value

        except psycopg2.OperationalError as ex:
            if con:
                con.rollback()

            print("Connection failed: {0}".format(ex))
            sys.exit(1)

        finally:
            if con:
                con.close()

    def get_constant_values(self, key):
        value = None
        if key in self.constants:
            value = self.constants[key]
            # print(key + ": " + str(value))
        else:
            print("Key does not exist")
        return value

    def get_constant_list(self, key, ship_type):
        if ship_type == 'carrier':
            index = 0
        elif ship_type == 'cruiser':
            index = 1
        elif ship_type == 'destroyer':
            index = 2
        elif ship_type == 'patrol_boat':
            index = 3
        else:
            index = 4
        result = self.constants.get(key, 'empty')
        return result[index] if result != 'empty' else None

    def get_constant_bool(self, boolean):
        value = None
        if boolean in self.constants:
            value = self.constants[boolean]
        else:
            print("Key does not exist")
        return value
