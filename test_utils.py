import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_get_dictionary_from_database(self):
        # create object of class Constants
        self.constants = utils.Constants()

        # when
        expected = {'computer_opponent': 1, 'player_opponent': 2, 'easy_difficulty': 1, 'normal_difficulty': 2,
                    'god_difficulty': 3, 'carrier': 5, 'cruiser': 4, 'destroyer': 3, 'patrol_boat': 2,
                    'submarine': 1, 'horizontal_axis': 1, 'vertical_axis': 2}

        # call method of object Constants
        observed = self.constants.get_dictionary_from_database(host='localhost', dbname='skelkelian')

        # assert
        self.assertEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
