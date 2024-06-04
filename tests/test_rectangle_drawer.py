import unittest
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from rectangle_drawer import RectangleDrawer

class TestRectangleDrawer(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.text = "Text"
        self.drawer = RectangleDrawer(self.root, self.text, self.mock_callback)
    
    def mock_callback(self, font_size, line_spacing, character_spacing, final_image):
        self.font_size = font_size
        self.line_spacing = line_spacing
        self.character_spacing = character_spacing
        self.final_image = final_image
    
    def test_initialization(self):
        self.assertEqual(self.drawer.text, self.text)
        self.assertEqual(self.drawer.callback, self.mock_callback)

if __name__ == "__main__":
    unittest.main()