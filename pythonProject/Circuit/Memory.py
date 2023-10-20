from abc import ABC, abstractmethod

class Memory(ABC):

    def __init__(self):
        self.content = {}

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def add(self, data):
        pass

    def getData(self, dir):
        return self.content[dir]

class DataMem(Memory):
    def __init__(self):
        super().__init__()
        self.table = {}
        self.free = 0
        self.create()


    def create(self):
        cont = 0
        for i in range(0, 10): #Todo: Cuantas iteraciones
            self.content[cont] = 0
            cont = cont+4

    def add(self, data):
        key = data[0]
        self.table[key] = self.free
        if data[1] == ".space":
            self.content[self.free] = None
        else:
            self.content[self.free] = data[2]

        self.free = self.free+4
class IntructionMem(Memory):
    def __init__(self):
        super().__init__()
        self.labels = {}
        self.create()
        self.free = 0

    def create(self):
        cont = 0
        for i in range(0, 10): #Todo: Cuantas iteraciones
            self.content[cont] = []
            cont = cont+4

    def add(self, instruction):
        self.content[self.free] = instruction
        self.free = self.free + 4

    def addLabel(self, instruction, label):

        for l in label:
            self.labels[l] = self.free
        self.add(instruction)

    def replacePseudoIntruc(self, list):
        intruc1 = list.pop(0)
        self.content[self.free-4]= intruc1
        for e in list:
            self.add(e)


class Registers(Memory):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.add(None)

    def add(self, data):
        self.content['$zero'] = 0
        self.content['$at'] = 0
        self.content['$v0'] = 0
        self.content['$v1'] = 0
        for i in range(0, 9):
            self.content[f'$a{i}'] = 0

        for i in range(0, 10):
            self.content[f'$t{i}'] = 0

        for i in range(0, 8):
            self.content[f'$s{i}'] = 0

        self.content['$k0'] = 0
        self.content['$k1'] = 0

        self.content['$gp'] = 0
        self.content['$sp'] = 0
        self.content['$fp'] = 0
        self.content['$ra'] = 0


    def load(self, data, register):
        self.content[register] = data