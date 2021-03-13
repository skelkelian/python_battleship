# tests/runner.py
import unittest

# import your test modules
import test_player
import test_computer
import test_carrier

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_computer))
suite.addTests(loader.loadTestsFromModule(test_carrier))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
