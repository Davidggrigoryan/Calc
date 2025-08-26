import tkinter as tk


class Calculator(tk.Tk):
    """GUI calculator with light and dark themes."""

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.memory = 0.0
        self.theme = "light"
        self.colors = {
            "light": {
                "bg": "#ffffff",
                "display_bg": "#ffffff",
                "display_fg": "#000000",
                "button_bg": "#f2f2f2",
                "op_bg": "#e6e6e6",
                "button_fg": "#000000",
                "equals_bg": "#1976d2",
                "equals_fg": "#ffffff",
            },
            "dark": {
                "bg": "#1e1e1e",
                "display_bg": "#1e1e1e",
                "display_fg": "#ffffff",
                "button_bg": "#2b2b2b",
                "op_bg": "#3c3c3c",
                "button_fg": "#ffffff",
                "equals_bg": "#1565c0",
                "equals_fg": "#ffffff",
            },
        }
        self._create_widgets()
        self._apply_theme()
        self._bind_keys()

    def _create_widgets(self) -> None:
        tk.Label(self, text="CALCULATOR", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=4, pady=(10, 0)
        )
        self.display = tk.Entry(
            self,
            width=16,
            font=("Arial", 24),
            bd=0,
            relief="flat",
            justify="right",
        )
        self.display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.buttons = []
        layout = [
            ("MC", self._mc, 2, 0),
            ("M+", self._m_plus, 2, 1),
            ("M-", self._m_minus, 2, 2),
            ("/", lambda: self._append("/"), 2, 3),
            ("7", lambda: self._append("7"), 3, 0),
            ("8", lambda: self._append("8"), 3, 1),
            ("9", lambda: self._append("9"), 3, 2),
            ("*", lambda: self._append("*"), 3, 3),
            ("4", lambda: self._append("4"), 4, 0),
            ("5", lambda: self._append("5"), 4, 1),
            ("6", lambda: self._append("6"), 4, 2),
            ("-", lambda: self._append("-"), 4, 3),
            ("1", lambda: self._append("1"), 5, 0),
            ("2", lambda: self._append("2"), 5, 1),
            ("3", lambda: self._append("3"), 5, 2),
            ("+", lambda: self._append("+"), 5, 3),
            ("0", lambda: self._append("0"), 6, 0),
            (".", lambda: self._append("."), 6, 1),
            ("C", self._clear, 6, 2),
            ("=", self._calculate, 6, 3),
        ]

        for (text, cmd, row, column) in layout:
            btn = tk.Button(
                self,
                text=text,
                width=4,
                height=2,
                font=("Arial", 20),
                bd=0,
                command=cmd,
            )
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            self.buttons.append(btn)

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(2, 7):
            self.grid_rowconfigure(i, weight=1)

    def _apply_theme(self) -> None:
        colors = self.colors[self.theme]
        self.configure(bg=colors["bg"])
        self.display.configure(
            bg=colors["display_bg"],
            fg=colors["display_fg"],
            insertbackground=colors["display_fg"],
        )
        for btn in self.buttons:
            txt = btn["text"]
            if txt == "=":
                btn.configure(
                    bg=colors["equals_bg"],
                    fg=colors["equals_fg"],
                    activebackground=colors["equals_bg"],
                    activeforeground=colors["equals_fg"],
                )
            elif txt in {"/", "*", "-", "+", "C"}:
                btn.configure(
                    bg=colors["op_bg"],
                    fg=colors["button_fg"],
                    activebackground=colors["op_bg"],
                    activeforeground=colors["button_fg"],
                )
            else:
                btn.configure(
                    bg=colors["button_bg"],
                    fg=colors["button_fg"],
                    activebackground=colors["button_bg"],
                    activeforeground=colors["button_fg"],
                )

    def _toggle_theme(self) -> None:
        self.theme = "dark" if self.theme == "light" else "light"
        self._apply_theme()

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

    def _mc(self) -> None:
        self.memory = 0.0

    def _m_plus(self) -> None:
        try:
            self.memory += float(self.display.get() or 0)
        except ValueError:
            pass

    def _m_minus(self) -> None:
        try:
            self.memory -= float(self.display.get() or 0)
        except ValueError:
            pass

    def _bind_keys(self) -> None:
        for key in "0123456789+-*/.":
            self.bind(key, lambda e, val=key: self._append(val))
        self.bind("<Return>", lambda e: self._calculate())
        self.bind("<Escape>", lambda e: self._clear())
        self.bind("<Control-t>", lambda e: self._toggle_theme())


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
