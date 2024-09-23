import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 24))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        button_layout = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row, buttons in enumerate(button_layout, start=1):
            for col, button in enumerate(buttons):
                self.create_button(button, row, col)

        self.create_button('Clear', 5, 0, 2, command=self.clear)
        self.create_button('Exit', 5, 2, 2, command=master.quit)
        self.configure_grid()

    def create_button(self, text, row, col, colspan=1, command=None):
        if command is None:
            command = lambda: self.click(text)
        tk.Button(self.master, text=text, command=command, width=5, height=2, font=('Arial', 18)).grid(
            row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky='nsew'
        )

    def configure_grid(self):
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    root.resizable(False, False)
    calculator = Calculator(root)
    root.mainloop()
