import unittest
from PIL import Image, ImageDraw
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from text_fitting import draw_text_around_rectangle, calculate_free_space, find_optimal_text_settings, calculate_fit_score
from rectangle import Rectangle

class TestTextFitting(unittest.TestCase):
    def setUp(self):
        self.text = "test text"
        self.start_x = 0
        self.start_y = 0
        self.end_x = 100
        self.end_y = 50
        self.free_space = calculate_free_space(self.start_x, self.start_y, self.end_x, self.end_y)
    
    def test_calculate_free_space(self):
        free_space = calculate_free_space(0, 0, 100, 50)
        self.assertIsInstance(free_space, Rectangle)
        self.assertEqual(free_space.width, 800)
        self.assertEqual(free_space.height, 600)
    
    def test_find_optimal_text_settings(self):
        font_size, line_spacing, character_spacing = find_optimal_text_settings(self.free_space, self.text)
        self.assertIsInstance(font_size, int)
        self.assertIsInstance(line_spacing, float)
        self.assertIsInstance(character_spacing, float)
    
    def test_draw_text_around_rectangle(self):
        image = Image.new("RGB", (842, 595), "white")
        draw = ImageDraw.Draw(image)
        font_size, line_spacing, character_spacing = draw_text_around_rectangle(draw, self.text, self.start_x, self.start_y, self.end_x, self.end_y)
        self.assertIsInstance(font_size, int)
        self.assertIsInstance(line_spacing, float)
        self.assertIsInstance(character_spacing, float)

if __name__ == "__main__":
    unittest.main()