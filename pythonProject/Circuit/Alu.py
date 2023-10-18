from abc import ABC, abstractmethod


class Alu(ABC):
    def __init__(self):
        self.result = 0

    @abstractmethod
    def ope(self, cod, op1, op2):
        pass


class MainAlu(Alu):

    def __init__(self):
        super().__init__()
        self.zero = 0

    def ope(self, cod, op1, op2):

        if cod == "add":
            self.result = op1 + op2
            return self.result
        if cod == "sub":
            self.result = op1 - op2
            return self.result


class AddAlu(Alu):

    def __init__(self):
        super().__init__()

    def ope(self, cod, op1, op2):
        self.result = op1 + op2
        return self.result
