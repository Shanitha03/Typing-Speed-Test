import tkinter as tk
import time
from tkinter import messagebox

text_to_type = "The quick brown fox jumps over the lazy dog."

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text_label = tk.Label(root, text=text_to_type, wraplength=400, font=("Arial", 12))
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_result)

        self.start_time = None

        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

    def start_test(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = time.time()
        self.entry.focus()

    def check_result(self, event):
        end_time = time.time()
        typed_text = self.entry.get()
        if typed_text.strip() == text_to_type:
            time_taken = end_time - self.start_time
            words = len(text_to_type.split())
            speed = round((words / time_taken) * 60, 2)
            self.result_label.config(text=f"Speed: {speed} WPM")
        else:
            self.result_label.config(text="Text doesn't match! Try again.")

root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
