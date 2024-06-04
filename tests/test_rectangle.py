import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        rect = Rectangle(10, 20, 30, 40)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 20)
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 40)

if __name__ == "__main__":
    unittest.main()
