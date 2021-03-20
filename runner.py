# tests/runner.py
import unittest

# import your test modules
import test_player
import test_computer
import test_carrier
import test_cruiser
import test_destroyer
import test_battleship
import test_patrol_boat

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_computer))
suite.addTests(loader.loadTestsFromModule(test_carrier))
suite.addTests(loader.loadTestsFromModule(test_cruiser))
suite.addTests(loader.loadTestsFromModule(test_destroyer))
suite.addTests(loader.loadTestsFromModule(test_battleship))
suite.addTests(loader.loadTestsFromModule(test_patrol_boat))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
