from random import randint
from participant import Participant


class Player(Participant):
    def __init__(self, config_name=None):
        super().__init__()
        self.hit_counter = [0, 0, 0, 0, 0]  # when computer hits a ship adjust this hit counter
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

    def get_hit_counter_player(self):
        return self.hit_counter

    def get_primary_board_player_one(self):
        return self.primary_board_player_one

    def pick_point_player_one(self):
        row_picked_by_player = randint(1, 10)
        column_picked_by_player = randint(1, 10)
        return row_picked_by_player, column_picked_by_player
