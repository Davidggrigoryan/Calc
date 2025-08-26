import tkinter as tk


class Calculator(tk.Tk):
    """Simple GUI calculator with basic arithmetic operations."""

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        self.display = tk.Entry(self, width=16, font=("Arial", 24), bd=2, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, column) in buttons:
            if text == '=':
                cmd = self._calculate
            else:
                cmd = lambda val=text: self._append(val)
            tk.Button(self, text=text, width=4, height=2, font=("Arial", 20),
                      command=cmd).grid(row=row, column=column, padx=2, pady=2)

        tk.Button(self, text='C', width=20, height=2, font=("Arial", 20),
                  command=self._clear).grid(row=5, column=0, columnspan=4, padx=2, pady=2)

    def _append(self, value: str) -> None:
        """Append a character to the display."""
        self.display.insert(tk.END, value)

    def _clear(self) -> None:
        """Clear the display."""
        self.display.delete(0, tk.END)

    def _calculate(self) -> None:
        """Evaluate the expression in the display."""
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def _bind_keys(self) -> None:
        for key in '0123456789+-*/.':
            self.bind(key, lambda e, val=key: self._append(val))
        self.bind('<Return>', lambda e: self._calculate())
        self.bind('<Escape>', lambda e: self._clear())


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
