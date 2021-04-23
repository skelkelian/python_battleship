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
                    'validation_flag_carrier_player': True, 'validation_flag_cruiser_player': True,
                    'validation_flag_destroyer_player': True, 'validation_flag_patrol_boat_player': True,
                    'validation_flag_submarine_player': True, 'validation_flag_cruiser_overlap_player': True,
                    'validation_flag_destroyer_overlap_player': True,
                    'validation_flag_patrol_boat_overlap_player': True,
                    'validation_flag_submarine_overlap_player': True, 'validation_flag_hit_or_miss_player': True,
                    'validation_flag_hit_counter_player': True, 'validation_flag_ship_sunk_carrier_player': False,
                    'validation_flag_ship_sunk_cruiser_player': False,
                    'validation_flag_ship_sunk_destroyer_player': False,
                    'validation_flag_ship_sunk_patrol_boat_player': False,
                    'validation_flag_ship_sunk_submarine_player': False, 'validation_flag_game_over_player': False,
                    'validation_flag_carrier_computer': True, 'validation_flag_battleship_computer': True,
                    'validation_flag_destroyer_computer': True, 'validation_flag_patrol_boat_computer': True,
                    'validation_flag_submarine_computer': True, 'validation_flag_cruiser_overlap_computer': True,
                    'validation_flag_destroyer_overlap_computer': True,
                    'validation_flag_patrol_boat_overlap_computer': True,
                    'validation_flag_submarine_overlap_computer': True, 'validation_flag_hit_or_miss_computer': True,
                    'validation_flag_hit_counter_computer': True, 'validation_flag_ship_sunk_carrier_computer': False,
                    'validation_flag_ship_sunk_cruiser_computer': False,
                    'validation_flag_ship_sunk_destroyer_computer': False,
                    'validation_flag_ship_sunk_patrol_boat_computer': False,
                    'validation_flag_ship_sunk_submarine_computer': False, 'validation_flag_game_over_computer': False,
                    'hit_counter_player_one': [0, 0, 0, 0, 0], 'hit_counter_computer': [0, 0, 0, 0, 0]}

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

    def test_get_constant_bool(self):
        # create object of class Constants
        self.constants = utils.Constants()

        # when
        expected = True

        # call method of object Constants
        observed = self.constants.get_constant_bool('validation_flag_game')

        # assert
        self.assertEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
