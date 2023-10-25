from abc import ABC, abstractmethod


class Alu(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ope(self, cod, op1, op2):
        pass


class MainAlu(Alu):

    def __init__(self):
        super().__init__()

    def ope(self, cod, op1, op2):
        if cod == "add":
            return op1 + op2
        if cod == "sub":
            return op1 - op2


class AddAlu(Alu):

    def __init__(self):
        super().__init__()

    def ope(self, cod, op1, op2):
        return op1 + op2
