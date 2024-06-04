import unittest

from test_rectangle import TestRectangle
from test_text_fitting import TestTextFitting
from test_rectangle_drawer import TestRectangleDrawer
from test_app import TestApp


if __name__ == "__main__":
    loader = unittest.TestLoader()

    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestRectangle))
    suite.addTests(loader.loadTestsFromTestCase(TestTextFitting))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleDrawer))
    suite.addTests(loader.loadTestsFromTestCase(TestApp))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
