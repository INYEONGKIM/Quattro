from TestModule.UserPlayerTest import UserPlayerTest
from TestModule.DeckTest import DeckTest
import unittest


def suite():
    suite = unittest.TestSuite()

    for fn in UserPlayerTest.method_names:
        suite.addTest(UserPlayerTest(fn.__name__))

    for fn in DeckTest.method_names:
        suite.addTest(DeckTest(fn.__name__))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
