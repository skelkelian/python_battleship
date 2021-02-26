from random import randint
from utils import Constants


class Participant:
    def __init__(self):
        self.constants = Constants()

    def pick_point(self):
        row_picked = randint(1, 10)
        column_picked = randint(1, 10)
        return row_picked, column_picked
