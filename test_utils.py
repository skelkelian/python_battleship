import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_set_constants_from_database(self):
        # create object of class Constants
        self.constants = utils.Constants()

        # when
        expected = {'computer_opponent': 1, 'player_opponent': 2, 'easy_difficulty': 1, 'normal_difficulty': 2,
                    'god_difficulty': 3, 'carrier': 5, 'cruiser': 4, 'destroyer': 3, 'patrol_boat': 2,
                    'submarine': 1, 'horizontal_axis': 1, 'vertical_axis': 2, 'validation_flag_game': True,
                    'hit_counter_player_one': [0, 0, 0, 0, 0]}

        # call method of object Constants
        observed = self.constants.get_constants()

        # assert
        self.assertEqual(expected, observed)

    def test_get_constant_values(self):
        # create object of class Constants
        self.constants = utils.Constants()

        # when
        expected = 1

        # call method of object Constants
        observed = self.constants.get_constant_values('computer_opponent')

        # assert
        self.assertEqual(expected, observed)

    def test_get_constant_list(self):
        # create object of class Constants
        self.constants = utils.Constants()

        # when
        expected = 0

        # call method of object Constants
        observed = self.constants.get_constant_list('hit_counter_player_one', 'carrier')

        # assert
        self.assertEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
