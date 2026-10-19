class Engine:
    def __init__(self):
        self.acc = ""
        self.single_char = "+-/*."

    def append(self, symbol: str):
        if self.acc and self.acc[-1:] in self.single_char and symbol in self.single_char:
            self.delete()
        if self.acc == "Error! Press clear":
            self.clear()
        self.acc = f"{self.acc}{symbol}"

    def delete(self):
        if self.acc == "Error! Press clear":
            self.clear()
        if self.acc:
            self.acc = self.acc[0:-1]

    def clear(self):
        self.acc = ""

    def get(self):
        return self.acc

    def calculate(self):
        if not self.acc:
            return
        try:
            self.acc = str(eval(self.acc))
        except (SyntaxError, ZeroDivisionError, TypeError, NameError):
            self.acc = "Error! Press clear"
        else:
            self.acc = self.acc.removesuffix(".0")
