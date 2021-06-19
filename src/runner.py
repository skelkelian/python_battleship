# tests/runner.py
import unittest
import os
os.chdir('/Users/skelkelian/Programming/official/python_battleship/src')

# import your test modules
from tests import test_carrier, test_battleship, test_computer, test_cruiser, test_destroyer, test_patrol_boat, \
    test_player, test_ship, test_submarine, test_utils

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
# suite.addTests(loader.loadTestsFromModule(test_player))
# suite.addTests(loader.loadTestsFromModule(test_computer))
suite.addTests(loader.loadTestsFromModule(test_carrier))
# suite.addTests(loader.loadTestsFromModule(test_cruiser))
# suite.addTests(loader.loadTestsFromModule(test_destroyer))
# suite.addTests(loader.loadTestsFromModule(test_battleship))
# suite.addTests(loader.loadTestsFromModule(test_patrol_boat))
# suite.addTests(loader.loadTestsFromModule(test_ship))
# suite.addTests(loader.loadTestsFromModule(test_submarine))
# suite.addTests(loader.loadTestsFromModule(test_utils))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
