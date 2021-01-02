from random import randint


class Ship:
    def __init__(self):
        self.hit_counter = [0, 0, 0, 0, 0]  # when computer hits a ship adjust this hit counter

    def get_hit_counter_player(self):
        return self.hit_counter

