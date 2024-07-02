import tkinter as tk
from src.router import MyApp


def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
