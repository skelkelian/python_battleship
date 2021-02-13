from random import randint


class Computer:
    def __init__(self, config_name=None):
        self.hit_counter_computer = [0, 0, 0, 0, 0]  # when player hits a ship adjust this hit counter
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

    def get_hit_counter_computer(self):
        return self.hit_counter_computer

    def get_primary_board_computer(self):
        return self.primary_board_computer

    def pick_point_computer(self):
        row_picked_by_computer = randint(1, 10)
        column_picked_by_computer = randint(1, 10)
        return row_picked_by_computer, column_picked_by_computer
