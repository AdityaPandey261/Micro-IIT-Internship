import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        
        self.expression = ""
        
        # Entry widget to display the expression
        self.input_text = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.input_text, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set(self.expression)
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.input_text.set(self.expression)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set(self.expression)
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()