class Engine():
    def __init__(self):
        self.acc = ""

    def append(self, symbol: str):
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
            return "Error! Press C and try again."
        else:
            return self.acc

