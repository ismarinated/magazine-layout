import tkinter as tk
from PIL import Image, ImageDraw
from text_fitting import draw_text_around_rectangle

class RectangleDrawer:
    def __init__(self, root, text, callback):
        self.root = root
        self.text = text
        self.callback = callback

    def draw_rectangle_window(self):
        self.root.title("Обозначьте места размещения иллюстраций")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        confirm_button = tk.Button(self.root, text="Подтвердить", command=self.on_confirm)
        confirm_button.pack(pady=10)

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

        self.start_x = self.start_y = self.end_x = self.end_y = None
        self.rectangles = []

    def on_canvas_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.current_rectangle_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def on_canvas_drag(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.canvas.coords(self.current_rectangle_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_canvas_release(self, event):
        self.end_x = event.x
        self.end_y = event.y
        start_x_fixed, start_y_fixed = min(self.start_x, self.end_x), min(self.start_y, self.end_y)
        end_x_fixed, end_y_fixed = max(self.start_x, self.end_x), max(self.start_y, self.end_y)
        self.canvas.coords(self.current_rectangle_id, start_x_fixed, start_y_fixed, end_x_fixed, end_y_fixed)
        self.rectangles.append((start_x_fixed, start_y_fixed, end_x_fixed, end_y_fixed))

    def on_confirm(self):
        image = Image.new("RGB", (800, 600), "white")
        draw = ImageDraw.Draw(image)

        start_x, start_y, end_x, end_y = self.rectangles[-1]
        font_size, line_spacing, character_spacing = draw_text_around_rectangle(draw, self.text, start_x, start_y, end_x, end_y)

        self.callback(font_size, line_spacing, character_spacing, image)

        image.show()

        self.root.destroy()
