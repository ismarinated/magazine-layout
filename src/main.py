import tkinter as tk
from app import App

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Верстка журнала")
    root.iconbitmap("../templates/icon.ico")
    app = App(root)
    root.mainloop()
