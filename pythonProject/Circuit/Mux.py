class Mux:
    def __init__(self):
        self.value0 = 0
        self.value1 = 0
        self.signal = False
    def setValue0(self, value):
        self.value0 = value

    def setValue1(self, value):
        self.value1 = value

    def setSignal(self, signal):
        self.signal = signal

    def getValue(self):
        return self.value0 if not self.signal else self.value1
