import tkinter as tk
from tkinter import filedialog, messagebox
from rectangle_drawer import RectangleDrawer

class App:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
    
    def setup_ui(self):
        self.main_window = tk.Frame(self.root)
        self.main_window.pack()
        
        self.frame = tk.Frame(self.main_window, padx=10, pady=10)
        self.frame.grid(row=0, column=0)

        self.label = tk.Label(self.frame, text="Выберите текстовый файл для обработки:", font=("Arial", 10, "bold"))
        self.label.grid(row=0, column=0, sticky="w", pady=5)

        self.select_button = tk.Button(self.frame, text="Выбрать файл", command=self.select_file)
        self.select_button.grid(row=0, column=1, pady=5, padx=(10, 0))

        self.file_path_label = tk.Label(self.frame, text="Выбранный файл: ")
        self.file_path_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=5)

        self.open_button = tk.Button(self.frame, text="Открыть окно разметки", command=self.open_rectangle_window, state="disabled")
        self.open_button.grid(row=2, column=0, columnspan=3, pady=5, padx=(10, 0))

        self.font_size_label = tk.Label(self.frame, text="Размер шрифта: ", font=("Arial", 10, "bold"))
        self.font_size_label.grid(row=3, column=0, sticky="w", pady=(20, 5))

        self.line_spacing_label = tk.Label(self.frame, text="Межстрочный интервал: ", font=("Arial", 10, "bold"))
        self.line_spacing_label.grid(row=4, column=0, sticky="w", pady=5)

        self.char_spacing_label = tk.Label(self.frame, text="Межсимвольный интервал: ", font=("Arial", 10, "bold"))
        self.char_spacing_label.grid(row=5, column=0, sticky="w", pady=5)

        self.save_button = tk.Button(self.frame, text="Сохранить изображение", command=self.save_image, state="disabled")
        self.save_button.grid(row=6, column=0, columnspan=3, pady=(20, 5))

        self.final_image = None
        self.file_path = ""

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_path:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
            self.file_path_label.config(text=f"Выбранный файл: {self.file_path}")
            self.open_button.config(state="active")
            self.rectangle_drawer = RectangleDrawer(self.root, self.text, self.callback)

    def open_rectangle_window(self):
        if self.file_path:
            rectangle_window = tk.Toplevel(self.root)
            rectangle_window.title("Обозначьте места размещения иллюстраций")
            rectangle_window.iconbitmap("templates/icon.ico")
            
            # Установить первое окно как вспомогательное для второго окна
            rectangle_window.transient(self.root)

            self.rectangle_drawer = RectangleDrawer(rectangle_window, self.text, self.callback)
            self.rectangle_drawer.draw_rectangle_window()
        else:
            messagebox.showerror("Ошибка", "Сначала выберите файл.")

    def save_image(self):
        if self.final_image:
            file_path = filedialog.asksaveasfilename(initialfile="Результат", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
            if file_path:
                self.final_image.save(file_path)
                messagebox.showinfo("Сохранение изображения", f"Изображение сохранено как {file_path}")
        else:
            messagebox.showwarning("Ошибка", "Нет изображения для сохранения.")

    def callback(self, font_size, line_spacing, character_spacing, final_image):
        self.font_size_label.config(text=f"Размер шрифта: {font_size}")
        self.line_spacing_label.config(text=f"Межстрочный интервал: {line_spacing}")
        self.char_spacing_label.config(text=f"Межсимвольный интервал: {character_spacing}")

        self.save_button.config(state="active")

        self.final_image = final_image

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
