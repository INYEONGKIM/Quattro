from TestModule.UserPlayerTest import UserPlayerTest
from TestModule.DeckTest import DeckTest
from TestModule.EndOfGameTest import EndOfGameTest
from TestModule.AnonymousPlayerTest import AnonymousPlayerTest
import unittest


def suite():
    suite = unittest.TestSuite()

    for fn in UserPlayerTest.method_names:
        suite.addTest(UserPlayerTest(fn.__name__))

    for fn in DeckTest.method_names:
        suite.addTest(DeckTest(fn.__name__))

    for fn in EndOfGameTest.method_names:
        suite.addTest(EndOfGameTest(fn.__name__))

    for fn in AnonymousPlayerTest.method_names:
        suite.addTest(AnonymousPlayerTest(fn.__name__))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
