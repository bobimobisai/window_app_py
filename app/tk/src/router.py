from tkinter import ttk


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Multi-Page App")
        self.root.geometry("400x300")

        self.frame_stack = []

        self.create_main_page()

    def create_main_page(self):
        self.clear_frame()
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        ttk.Button(frame, text="Go to Page 1", command=self.show_page_1).pack(pady=10)
        ttk.Button(frame, text="Go to Page 2", command=self.show_page_2).pack(pady=10)

        self.frame_stack.append(frame)

    def show_page_1(self):
        self.clear_frame()
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="This is Page 1").pack(pady=10)
        ttk.Button(frame, text="Back to Home", command=self.create_main_page).pack(
            pady=10
        )

        self.frame_stack.append(frame)

    def show_page_2(self):
        self.clear_frame()
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="This is Page 2").pack(pady=10)
        ttk.Button(frame, text="Back to Home", command=self.create_main_page).pack(
            pady=10
        )

        self.frame_stack.append(frame)

    def clear_frame(self):
        while self.frame_stack:
            frame = self.frame_stack.pop()
            frame.destroy()
