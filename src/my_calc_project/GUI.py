import tkinter as tk
from my_calc_project.engine import Engine


class Gui:
    def __init__(self, window):
        self.win = window
        self.win.title("Calculator")
        self.win.geometry("300x370")
        self.win.minsize(300, 370)


        self.display_var = tk.StringVar()
        self.display_frame = tk.Frame(self.win, bd = 1, relief = "solid")
        self.display_frame.columnconfigure(0, weight = 1)
        self.display_frame.rowconfigure(0, weight = 1)
        self.display_label = tk.Label(self.display_frame, font = ("arial", 19), textvariable = self.display_var)
        self.display_label.grid(row = 0, column = 0, sticky = "e")
        self.display_frame.place(relx = 0.03, rely = 0.03, relwidth = 0.94, relheight = 0.20)


        self.button_container = tk.Frame(self.win, bd = 1, relief = "solid")

        for i in range(4):
            self.button_container.columnconfigure(i, weight = 1, uniform = "col_button_cont_group")

        for i in range(5):
            self.button_container.rowconfigure(i, weight = 1, uniform = "row_button_cont_group")

        self.number = 1
        for y in range(3):
            for x in range(3):
                self.number_button = tk.Button(
                        self.button_container,
                        text = str(self.number),
                        font = ("arial", 14),
                        bg = "#C8C8C8",
                        command = lambda i = self.number: self.click_button(str(i))
                        )
                self.number_button.grid(row = y, column = x, sticky = "nsew")
                self.number += 1

        self.button_zero = tk.Button(
                self.button_container,
                text = "0",
                font = ("arial", 14),
                bg = "#C8C8C8",
                command = lambda: self.click_button("0"))
        self.button_zero.grid(row = 3, column = 1, sticky = "nsew")

        self.button_dot = tk.Button(
                self.button_container,
                text = ".",
                font = ("arial", 14),
                bg = "#C8C8C8",
                command = lambda: self.click_button(".")
                )
        self.button_dot.grid(row = 4, column = 0, sticky = "nsew")

        self.button_open_bracket = tk.Button(
                self.button_container,
                text = "(",
                font = ("arial", 14),
                bg = "#C8C8C8",
                command = lambda: self.click_button("(")
                )
        self.button_open_bracket.grid(row = 3, column = 0, sticky = "nsew")

        self.button_close_bracket = tk.Button(
                self.button_container,
                text = ")",
                font = ("arial", 14),
                bg = "#C8C8C8",
                command = lambda: self.click_button(")"))
        self.button_close_bracket.grid(row = 3, column = 2, sticky = "nsew")

        self.button_delete = tk.Button(
                self.button_container,
                text = "delete",
                font = ("courier new", 11),
                bg = "#C8C8C8",
                command = lambda: self.click_button("delete")
                )
        self.button_delete.grid(row = 4, column = 2, sticky = "nsew")

        self.button_calculate = tk.Button(
                self.button_container,
                text = "=",
                font = ("arial", 18),
                bg = "#FFB547",
                command = lambda: self.click_button("calculate")
                )
        self.button_calculate.grid(row = 4, column = 3, sticky = "nsew")

        self.button_clear = tk.Button(
                self.button_container,
                text = "clear",
                font = ("courier new", 11),
                bg = "#C8C8C8",
                command = lambda: self.click_button("clear")
                )
        self.button_clear.grid(row = 4, column = 1, sticky = "nsew")

        self.button_divide = tk.Button(
                self.button_container,
                text = "/",
                font = ("arial", 18),
                bg = "#FFB547",
                command = lambda: self.click_button("/")
                )
        self.button_divide.grid(row = 3, column = 3, sticky = "nsew")

        self.button_multiply = tk.Button(
                self.button_container,
                text = "*",
                font = ("arial", 18),
                bg = "#FFB547",
                command = lambda: self.click_button("*")
                )
        self.button_multiply.grid(row = 2, column = 3, sticky = "nsew")

        self.button_minus = tk.Button(
                self.button_container,
                text = "-",
                font = ("arial", 18),
                bg = "#FFB547",
                command = lambda: self.click_button("-")
                )
        self.button_minus.grid(row = 1, column = 3, sticky = "nsew")

        self.button_plus = tk.Button(
                self.button_container,
                text = "+",
                font = ("arial", 18),
                bg = "#FFB547",
                command = lambda: self.click_button("+")
                )
        self.button_plus.grid(row = 0, column = 3, sticky = "nsew")


        self.button_container.place(relx = 0.03, rely = 0.25, relwidth = 0.94, relheight = 0.73)

        self.engine = Engine()


    def click_button(self, command):
        if command == "delete":
            self.engine.delete()
        
        elif command == "clear":
            self.engine.clear()
            
        elif command == "calculate":
            self.engine.calculate()

        else:
            self.engine.append(command)

        self.display_var.set(self.engine.get())
