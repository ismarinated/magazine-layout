import unittest
import tkinter as tk
import sys
import os
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    @patch("tkinter.filedialog.askopenfilename", return_value="test.txt")
    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data="sample text")
    def test_select_file(self, mock_open, mock_askopenfilename):
        self.app.select_file()
        self.assertEqual(self.app.file_path, "test.txt")
        self.assertEqual(self.app.text, "sample text")
        self.assertEqual(self.app.file_path_label.cget("text"), "Выбранный файл: test.txt")
        self.assertEqual(self.app.open_button.cget("state"), "active")
        mock_open.assert_called_once_with("test.txt", "r", encoding="utf-8")

    @patch("tkinter.Toplevel")
    @patch("src.rectangle_drawer.RectangleDrawer")
    @patch("tkinter.filedialog.askopenfilename", return_value="test.txt")
    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data="sample text")
    @patch("tkinter.messagebox.showerror")
    def test_open_rectangle_window_with_file(self, mock_showerror, mock_open, mock_askopenfilename, mock_RectangleDrawer, mock_Toplevel):
        self.app.select_file()
        self.app.open_rectangle_window()
        mock_Toplevel.assert_called_once_with(self.root)

    @patch("tkinter.messagebox.showerror")
    def test_open_rectangle_window_without_file(self, mock_showerror):
        self.app.open_rectangle_window()
        mock_showerror.assert_called_once_with("Ошибка", "Сначала выберите файл.")

    @patch("tkinter.filedialog.asksaveasfilename", return_value="output.png")
    @patch("PIL.Image.Image.save")
    @patch("tkinter.messagebox.showinfo")
    def test_save_image(self, mock_showinfo, mock_save, mock_asksaveasfilename):
        self.app.final_image = Mock()
        self.app.save_image()
        self.app.final_image.save.assert_called_once_with("output.png")
        mock_showinfo.assert_called_once_with("Сохранение изображения", "Изображение сохранено как output.png")

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()