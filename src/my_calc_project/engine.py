class Engine:
    def __init__(self):
        self.acc = ""
        self.single_char = "+-/*."

    def append(self, symbol: str):
        if self._get_last() in self.single_char and symbol in self.single_char:
            self.delete()
        self.acc = f"{self.acc}{symbol}"

    def delete(self):
        if self.acc:
            self.acc = self.acc[0:-1]

    def clear(self):
        self.acc = ""

    def get(self):
        return self.acc

    def calculate(self):
        try:
            self.acc = str(eval(self.acc))
        except:
            self.acc = "Error! Press clear."

    def _get_last(self):
        if self.acc:
            return self.acc[-1]
        else:
            return "Empty"
